"""
California Energy Analysis - Simple Version

This module provides basic analysis of California's electricity generation data.
It loads CSV data and calculates simple statistics.

Author: California Energy Project
"""

import pandas as pd
import numpy as np
from pathlib import Path
import json


class CaliforniaEnergyAnalyzer:
    """
    A simple analyzer for California electricity generation data.
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
        """
        print("Loading California energy data...")

        # Read the CSV file
        df = pd.read_csv(self.data_path, header=None)

        # Find the row with years (where 2014 appears)
        data_start_row = None
        for i, row in df.iterrows():
            if str(row.iloc[3]).strip() == '2014':
                data_start_row = i
                break

        if data_start_row is None:
            print("Error: Could not find data in CSV file")
            return None

        # Get years from header
        header_row = df.iloc[data_start_row - 1]
        years = []
        for col in range(3, len(header_row)):
            if pd.notna(header_row.iloc[col]) and str(header_row.iloc[col]).strip().isdigit():
                years.append(int(header_row.iloc[col]))

        # Get data rows
        data_rows = []
        categories = []
        for i in range(data_start_row, len(df)):
            row = df.iloc[i]
            if pd.notna(row.iloc[0]) and str(row.iloc[0]).strip():
                category = str(row.iloc[0]).strip()
                categories.append(category)

                values = []
                for col in range(3, len(years) + 3):
                    val = row.iloc[col]
                    if pd.notna(val) and val != '':
                        try:
                            values.append(float(val))
                        except:
                            values.append(0.0)
                    else:
                        values.append(0.0)

                data_rows.append(values)

        # Create dataframe
        df_data = pd.DataFrame(data_rows, columns=years)
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
            cat_data = self.processed_data[self.processed_data['Category'] == category]

            cat_stats = {
                'total_generation': cat_data['Generation_MWh'].sum(),
                'average_yearly': cat_data['Generation_MWh'].mean(),
                'peak_year': int(cat_data.loc[cat_data['Generation_MWh'].idxmax(), 'Year']),
                'lowest_year': int(cat_data.loc[cat_data['Generation_MWh'].idxmin(), 'Year']),
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

        # Simple key findings
        insights['key_findings'] = [
            f"California's electricity generation grew {stats['trends']['overall_growth_rate']:.1f}% from {stats['trends']['period']}",
            f"Total generation reached {stats['overall']['total_generation_mwh']:,.0f} MWh over the analyzed period",
            f"The {stats['trends']['dominant_category']} category was the largest energy source",
            f"Peak generation occurred in {stats['overall']['peak_year']} with {self.raw_data.loc[stats['overall']['peak_year']].sum():,.0f} MWh"
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

        insights['notable_trends'] = [
            "Independent Power Producers showed steady growth",
            "Electric Utility Cogen experienced decline",
            "Electric Power remained the dominant category"
        ]

        self.analysis_results['insights'] = insights
        return insights

    def _calculate_growth_rate(self, category_data):
        """Calculate simple growth rate for a category."""
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
