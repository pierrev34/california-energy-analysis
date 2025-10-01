"""
California Energy Analysis - Fuel-Based Analysis

This module provides comprehensive analysis of California's electricity generation 
by fuel type from 2014-2024. It automatically parses EIA CSV exports, cleans 
fuel categories, and generates insights about the energy transition.

Features:
- Auto-detects CSV structure and year columns
- Maps raw fuel descriptions to clean parent categories  
- Computes growth rates, totals, and volatility by fuel
- Exports corrected stacked area charts and data summaries

Author: California Energy Analysis Project
"""

import pandas as pd
import numpy as np
from pathlib import Path
import json


class CaliforniaEnergyAnalyzer:
    """
    Comprehensive analyzer for California electricity generation by fuel type.
    
    Handles EIA CSV parsing, fuel category cleaning, statistical analysis,
    and visualization generation for California's energy transition analysis.
    """

    def __init__(self, data_path="data/eia_california_generation_annual.csv"):
        """
        Initialize the analyzer.

        Args:
            data_path (str): Path to the data file
        """
        self.data_path = Path(data_path)
        self.raw_data = None
        self.processed_data = None
        self.analysis_results = {}

    def load_data(self):
        """
        Load the raw EIA data from CSV file.

        Supports both older EIA CSV exports and the newer format where the
        header row contains years starting at column index 3, followed by
        rows where column 0 is the category (fuel type) and columns >=3 are values.
        """
        print("Loading California energy data...")

        # Find header line index by scanning raw text (robust to metadata lines)
        header_idx = None
        with open(self.data_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            if '"description"' in line and '"units"' in line and '"source key"' in line:
                header_idx = i
                break

        if header_idx is None:
            print("Error: Could not find header row with description/units/source key")
            return None

        # Read again with the detected header row
        df_full = pd.read_csv(self.data_path, header=header_idx, engine='python')

        # Identify year columns (numeric column names)
        year_cols = []
        for col in df_full.columns:
            try:
                if str(col).strip().isdigit():
                    year_cols.append(int(str(col).strip()))
            except Exception:
                continue

        if not year_cols:
            print("Error: No year columns found in CSV header")
            return None

        # Build matrix: rows = years, columns = fuel categories (from description)
        categories = []
        data_rows = []
        for _, row in df_full.iterrows():
            desc = str(row.get('description', '')).strip()
            if not desc:
                continue
            values = []
            non_zero = False
            for y in year_cols:
                val = row.get(str(y), None)
                try:
                    num = float(val)
                except Exception:
                    num = 0.0
                if num != 0.0:
                    non_zero = True
                values.append(num)
            if non_zero:
                categories.append(desc)
                data_rows.append(values)

        df_data = pd.DataFrame(data_rows, columns=year_cols)
        df_data['Category'] = categories
        df_data = df_data.set_index('Category').T
        df_data.index.name = 'Year'

        self.raw_data = df_data
        print(f"Loaded data: {df_data.shape[0]} years, {df_data.shape[1]} categories")
        return df_data

    def process_data(self):
        """
        Process raw data into analysis-ready format.
        """
        if self.raw_data is None:
            self.load_data()

        print("Processing data...")

        # Convert to long format
        processed = self.raw_data.reset_index().melt(
            id_vars=['Year'],
            var_name='Category',
            value_name='Generation_MWh'
        )

        # Convert year to integer
        processed['Year'] = processed['Year'].astype(int)
        # Ensure numeric and fill missing
        processed['Generation_MWh'] = pd.to_numeric(processed['Generation_MWh'], errors='coerce').fillna(0.0)

        # Calculate yearly totals
        yearly_totals = processed.groupby('Year')['Generation_MWh'].sum()
        processed['Total_Yearly_Generation'] = processed['Year'].map(yearly_totals)
        processed['Percentage'] = (processed['Generation_MWh'] / processed['Total_Yearly_Generation']) * 100

        self.processed_data = processed
        print(f"Processed {len(processed)} data points")
        return processed

    def calculate_summary_statistics(self):
        """
        Calculate basic summary statistics.
        """
        if self.processed_data is None:
            self.process_data()

        print("Calculating statistics...")

        stats = {
            'overall': {},
            'by_category': {},
            'trends': {}
        }

        # Overall statistics
        total_generation = self.processed_data['Generation_MWh'].sum()
        years_count = self.processed_data['Year'].nunique()
        categories_count = self.processed_data['Category'].nunique()

        stats['overall'] = {
            'total_generation_mwh': total_generation,
            'years_analyzed': years_count,
            'categories_tracked': categories_count,
            'avg_yearly_generation': total_generation / years_count,
            'peak_year': int(self.processed_data.groupby('Year')['Generation_MWh'].sum().idxmax()),
            'lowest_year': int(self.processed_data.groupby('Year')['Generation_MWh'].sum().idxmin())
        }

        # Per-category statistics
        for category in self.processed_data['Category'].unique():
            cat_data = self.processed_data[self.processed_data['Category'] == category].copy()
            # drop rows where both year or value are missing
            cat_data = cat_data.dropna(subset=['Year', 'Generation_MWh'])
            if cat_data.empty:
                continue
            total_gen = cat_data['Generation_MWh'].sum()
            if total_gen == 0:
                continue
            # robust peak/lowest year lookup
            peak_idx = cat_data['Generation_MWh'].idxmax()
            low_idx = cat_data['Generation_MWh'].idxmin()
            peak_year_val = int(cat_data.loc[peak_idx, 'Year'])
            low_year_val = int(cat_data.loc[low_idx, 'Year'])

            cat_stats = {
                'total_generation': total_gen,
                'average_yearly': cat_data['Generation_MWh'].mean(),
                'peak_year': peak_year_val,
                'lowest_year': low_year_val,
                'volatility': cat_data['Generation_MWh'].std(),
                'growth_rate': self._calculate_growth_rate(cat_data)
            }
            stats['by_category'][category] = cat_stats

        # Simple trend analysis
        first_year = self.processed_data['Year'].min()
        last_year = self.processed_data['Year'].max()

        overall_growth = ((self.raw_data.loc[last_year].sum() / self.raw_data.loc[first_year].sum()) - 1) * 100

        stats['trends'] = {
            'overall_growth_rate': overall_growth,
            'period': f"{first_year}-{last_year}",
            'dominant_category': self._find_dominant_category(),
            'most_volatile_category': self._find_most_volatile_category()
        }

        self.analysis_results['statistics'] = stats
        return stats

    def generate_insights(self):
        """
        Generate basic insights from the data.
        """
        if 'statistics' not in self.analysis_results:
            self.calculate_summary_statistics()

        print("Generating insights...")

        stats = self.analysis_results['statistics']
        insights = {
            'key_findings': [],
            'notable_trends': [],
            'category_highlights': [],
            'recommendations': []
        }

        # Simple key findings (fuel-focused, data-driven)
        dominant = stats['trends']['dominant_category']
        peak_year = stats['overall']['peak_year']
        peak_val = self.raw_data.loc[peak_year].sum()

        insights['key_findings'] = [
            f"Net generation grew {stats['trends']['overall_growth_rate']:.1f}% from {stats['trends']['period']}",
            f"Total generation over the period: {stats['overall']['total_generation_mwh']:,.0f} MWh",
            f"Most influential fuel category on average: {dominant}",
            f"Peak total generation in {peak_year}: {peak_val:,.0f} MWh"
        ]

        # Category insights
        for category, cat_stats in stats['by_category'].items():
            if cat_stats['growth_rate'] > 5:
                trend = "growing"
            elif cat_stats['growth_rate'] > -5:
                trend = "stable"
            else:
                trend = "declining"

            insights['category_highlights'].append({
                'category': category,
                'trend': trend,
                'growth_rate': cat_stats['growth_rate'],
                'total_contribution': cat_stats['total_generation']
            })

        # Notable trends (computed): top growth, top decline, most volatile
        by_growth = sorted(
            ((c, v['growth_rate']) for c, v in stats['by_category'].items()),
            key=lambda x: x[1], reverse=True
        )
        top_grow = by_growth[0] if by_growth else (None, 0)
        by_decline = sorted(
            ((c, v['growth_rate']) for c, v in stats['by_category'].items()),
            key=lambda x: x[1]
        )
        top_decline = by_decline[0] if by_decline else (None, 0)

        insights['notable_trends'] = []
        if top_grow[0] is not None:
            insights['notable_trends'].append(
                f"Fastest growth: {top_grow[0]} ({top_grow[1]:+.1f}%)"
            )
        if top_decline[0] is not None:
            insights['notable_trends'].append(
                f"Largest decline: {top_decline[0]} ({top_decline[1]:+.1f}%)"
            )
        insights['notable_trends'].append(
            f"Most volatile: {stats['trends']['most_volatile_category']}"
        )

        self.analysis_results['insights'] = insights
        return insights

    def _calculate_growth_rate(self, category_data):
        """Calculate simple growth rate for a category over the period."""
        first_value = category_data['Generation_MWh'].iloc[0]
        last_value = category_data['Generation_MWh'].iloc[-1]
        years = len(category_data)

        if first_value > 0 and years > 1:
            return ((last_value / first_value) ** (1 / (years - 1)) - 1) * 100
        return 0.0

    def _find_dominant_category(self):
        """Find the category with highest average share."""
        avg_percentages = self.processed_data.groupby('Category')['Percentage'].mean()
        return avg_percentages.idxmax()

    def _find_most_volatile_category(self):
        """Find the category with highest volatility."""
        volatility = self.processed_data.groupby('Category')['Generation_MWh'].std()
        return volatility.idxmax()

    def export_results(self, output_format='json'):
        """
        Export analysis results to file.
        """
        if not self.analysis_results:
            self.generate_insights()

        print(f"Exporting results as {output_format.upper()}...")

        if output_format.lower() == 'json':
            output_file = "output/analysis_results.json"
            with open(output_file, 'w') as f:
                json.dump(self.analysis_results, f, indent=2, default=str)
            print(f"  Results exported to {output_file}")

        elif output_format.lower() == 'csv':
            # Export processed data
            output_file = "output/processed_data.csv"
            self.processed_data.to_csv(output_file, index=False)
            print(f"  Data exported to {output_file}")

    # ---------- Helper methods for cleaned fuel view and chart ----------
    def _clean_fuel_name(self, raw: str) -> str:
        """Map raw EIA description strings to cleaner parent fuel names.

        Heuristics:
        - Strip the leading "All sectors : " prefix if present
        - Collapse detailed solar rows to parent "All Utility-Scale Solar"
        - Keep aggregate "all fuels (utility-scale)" as-is for context
        - Title-case simple fuels (e.g., Natural Gas)
        """
        name = raw.strip()
        if name.lower().startswith("all sectors : "):
            name = name[len("all sectors : ") :].strip()

        lower = name.lower()
        if "all fuels (utility-scale)" in lower:
            return "All Fuels (Utility-Scale)"

        # Solar hierarchy: collapse to one parent
        if "all utility-scale solar" in lower:
            return "All Utility-Scale Solar"
        if "utility-scale photovoltaic" in lower or "photovoltaic" in lower:
            return "All Utility-Scale Solar"
        if "solar thermal" in lower:
            return "All Utility-Scale Solar"
        if "all solar" in lower:
            return "All Utility-Scale Solar"

        # Make common fuels nicer
        mapping = {
            "natural gas": "Natural Gas",
            "coal": "Coal",
            "nuclear": "Nuclear",
            "other renewables": "Other Renewables",
            "conventional hydroelectric": "Hydroelectric",
            "other gases": "Other Gases",
            "petroleum liquids": "Petroleum Liquids",
            "petroleum coke": "Petroleum Coke",
        }
        for key, val in mapping.items():
            if key in lower:
                return val
        # Fallback: basic cleanup/case
        return name.replace("  ", " ").strip().title()

    def aggregate_fuels(self) -> pd.DataFrame:
        """Return aggregated totals by cleaned fuel name across years.

        Returns a dataframe with columns: Fuel, Total_MWh, Growth_Rate.
        """
        if self.processed_data is None:
            self.process_data()

        df = self.processed_data.copy()
        df["CleanFuel"] = df["Category"].apply(self._clean_fuel_name)

        # Aggregate per year per clean fuel to avoid double counting within a year
        yearly = (
            df.groupby(["Year", "CleanFuel"], as_index=False)["Generation_MWh"].sum()
        )

        # Totals over period
        totals = yearly.groupby("CleanFuel")["Generation_MWh"].sum().rename("Total_MWh")

        # Build simple growth per fuel
        growth_list = {}
        for fuel, grp in yearly.groupby("CleanFuel"):
            grp_sorted = grp.sort_values("Year")
            first = grp_sorted["Generation_MWh"].iloc[0]
            last = grp_sorted["Generation_MWh"].iloc[-1]
            years = len(grp_sorted)
            if first > 0 and years > 1:
                gr = ((last / first) ** (1 / (years - 1)) - 1) * 100
            else:
                gr = 0.0
            growth_list[fuel] = gr

        out = (
            totals.to_frame()
            .assign(Growth_Percent=lambda s: s.index.map(lambda k: growth_list.get(k, 0.0)))
            .reset_index()
            .rename(columns={"CleanFuel": "Fuel"})
            .sort_values("Total_MWh", ascending=False)
        )
        return out

    def generate_stacked_area_png(self, output_path: str = "output/energy_mix.png") -> None:
        """Create a stacked area chart of generation by cleaned fuel and save PNG."""
        import matplotlib.pyplot as plt

        if self.processed_data is None:
            self.process_data()

        df = self.processed_data.copy()
        df["CleanFuel"] = df["Category"].apply(self._clean_fuel_name)

        # CRITICAL: Remove aggregate totals to avoid stacking total with parts
        df_fuels = df[df["CleanFuel"] != "All Fuels (Utility-Scale)"].copy()
        
        # Pivot to Year x Fuel matrix (MWh) - individual fuels only
        pivot = (
            df_fuels.groupby(["Year", "CleanFuel"])['Generation_MWh']
              .sum()
              .unstack(fill_value=0)
              .sort_index()
        )

        # Keep top 6 individual fuels by total, group rest as "Other"
        totals = pivot.sum(axis=0).sort_values(ascending=False)
        keep = totals.head(6).index.tolist()
        plot_df = pivot[keep].copy()
        if len(totals) > len(keep):
            plot_df["Other"] = pivot.drop(columns=keep, errors='ignore').sum(axis=1)

        plt.figure(figsize=(12, 7))
        ax = plot_df.plot.area(colormap='tab10', alpha=0.8)
        plt.ylabel("Generation (Thousand MWh)")
        plt.xlabel("Year")
        plt.title("California Energy Mix by Fuel Type (2014–2024)")
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(output_path, dpi=160, bbox_inches='tight')
        plt.close()
        print(f"  Stacked area chart saved to {output_path}")

    def print_analysis_summary(self):
        """Print a simple summary of the analysis."""
        if not self.analysis_results:
            self.generate_insights()

        print("\n" + "="*60)
        print("CALIFORNIA ENERGY GENERATION ANALYSIS SUMMARY")
        print("="*60)

        stats = self.analysis_results['statistics']
        insights = self.analysis_results['insights']

        # Overall metrics
        print("\nOVERALL METRICS:")
        print(f"   Period Analyzed: {stats['trends']['period']}")
        print(f"   Total Generation: {stats['overall']['total_generation_mwh']:,.0f} MWh")
        print(f"   Growth Rate: {stats['trends']['overall_growth_rate']:+.1f}%")
        print(f"   Peak Year: {stats['overall']['peak_year']}")

        # Key findings
        print("\nKEY FINDINGS:")
        for finding in insights['key_findings']:
            print(f"   • {finding}")

        # Category highlights
        print("\nCATEGORY HIGHLIGHTS:")
        for highlight in insights['category_highlights']:
            print(f"   • {highlight['category']}: {highlight['trend']} ({highlight['growth_rate']:+.1f}%)")

        print("\n" + "="*60)


def main():
    """Main function to run the complete analysis."""
    print("Starting California Energy Analysis")
    print("=" * 50)

    # Initialize and run analysis
    analyzer = CaliforniaEnergyAnalyzer()
    analyzer.load_data()
    analyzer.process_data()
    analyzer.calculate_summary_statistics()
    analyzer.generate_insights()

    # Display results
    analyzer.print_analysis_summary()

    # Export results
    analyzer.export_results('json')
    analyzer.export_results('csv')

    print("\nAnalysis complete! Check 'output' directory for exported files.")


if __name__ == "__main__":
    main()
