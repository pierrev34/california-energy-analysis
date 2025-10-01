"""
California Energy Generation Analysis - Visualization Module

This module creates interactive and static visualizations of California's
electricity generation data from 2014-2024.

Author: California Energy Analysis Project
Date: October 2025
"""

import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Enable Altair to render in Jupyter-like environments
alt.data_transformers.enable('json')


class CaliforniaEnergyVisualizer:
    """
    A class for creating visualizations of California energy generation data.

    This class handles data loading, processing, and visualization creation
    for the California electricity generation dataset.
    """

    def __init__(self, data_path: str = "data/eia_california_generation_annual.csv"):
        """
        Initialize the visualizer with data path.

        Args:
            data_path (str): Path to the EIA data file
        """
        self.data_path = Path(data_path)
        self.data = None
        self.processed_data = None

    def load_and_process_data(self) -> pd.DataFrame:
        """
        Load and process the raw EIA data into a clean format.

        Returns:
            pd.DataFrame: Processed dataframe ready for visualization
        """
        print("Loading and processing California energy data...")

        # Read the CSV file, handling the specific EIA format
        df = pd.read_csv(self.data_path, header=None)

        # Find the row with actual data (where years start)
        data_start_row = None
        for i, row in df.iterrows():
            if str(row.iloc[3]).strip() == '2014':
                data_start_row = i
                break

        if data_start_row is None:
            raise ValueError("Could not find data start row in CSV file")

        # Extract years from header
        header_row = df.iloc[data_start_row - 1]
        years = []
        for col in range(3, len(header_row)):
            if pd.notna(header_row.iloc[col]) and str(header_row.iloc[col]).strip().isdigit():
                years.append(int(header_row.iloc[col]))

        # Extract data rows
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

        # Convert to long format for easier plotting
        self.processed_data = df_data.reset_index().melt(
            id_vars=['Year'],
            var_name='Category',
            value_name='Generation_MWh'
        )
        return self.processed_data

    def create_stacked_area_chart(self) -> alt.Chart:
        """
        Create an interactive stacked area chart.

        Returns:
            alt.Chart: Interactive Altair chart
        """
        print("Creating stacked area chart...")

        # Calculate percentages for better visualization
        totals = self.processed_data.groupby('Year')['Generation_MWh'].sum()
        data_with_pct = self.processed_data.copy()
        data_with_pct['Percentage'] = data_with_pct.apply(
            lambda row: (row['Generation_MWh'] / totals[row['Year']]) * 100,
            axis=1
        )

        # Color scheme for categories (will be set dynamically)
        # Categories are now loaded from the CSV file
        categories = self.processed_data['Category'].unique().tolist()

        color_scale = alt.Scale(
            domain=categories,
            range=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
        )

        # Create the chart
        chart = alt.Chart(data_with_pct).mark_area().encode(
            x=alt.X('Year:O', title='Year'),
            y=alt.Y('Percentage:Q', title='Percentage of Total Generation (%)'),
            color=alt.Color('Category:N',
                          scale=color_scale,
                          legend=alt.Legend(title="Energy Category")),
            tooltip=[
                alt.Tooltip('Year:O', title='Year'),
                alt.Tooltip('Category:N', title='Category'),
                alt.Tooltip('Generation_MWh:Q', title='Generation (MWh)', format=',.0f'),
                alt.Tooltip('Percentage:Q', title='Percentage', format='.2f')
            ]
        ).properties(
            width=800,
            height=500,
            title="California Electricity Generation by Category (2014-2024)"
        ).configure_title(
            fontSize=18,
            fontWeight='bold'
        )

        return chart

    def create_trend_lines(self) -> alt.Chart:
        """
        Create line charts showing trends for each category.

        Returns:
            alt.Chart: Line chart showing individual category trends
        """
        print("Creating trend analysis chart...")

        # Calculate year-over-year growth rates
        yearly_data = self.processed_data.copy()
        yearly_data['Year'] = pd.to_datetime(yearly_data['Year'], format='%Y')

        # Create line chart for absolute values
        lines = alt.Chart(yearly_data).mark_line(point=True).encode(
            x=alt.X('Year:T', title='Year'),
            y=alt.Y('Generation_MWh:Q', title='Generation (thousand MWh)'),
            color=alt.Color('Category:N',
                          legend=alt.Legend(title="Energy Category")),
            tooltip=[
                alt.Tooltip('Year:T', title='Year'),
                alt.Tooltip('Category:N', title='Category'),
                alt.Tooltip('Generation_MWh:Q', title='Generation (MWh)', format=',.0f')
            ]
        ).properties(
            width=800,
            height=400,
            title="California Electricity Generation Trends (2014-2024)"
        )

        return lines

    def create_summary_stats_chart(self) -> alt.Chart:
        """
        Create a bar chart of total generation by category.

        Returns:
            alt.Chart: Bar chart of total generation per category
        """
        print("Creating summary statistics chart...")

        # Calculate totals per category
        category_totals = self.processed_data.groupby('Category')['Generation_MWh'].sum().reset_index()

        bars = alt.Chart(category_totals).mark_bar().encode(
            x=alt.X('Category:N', title='Energy Category', sort='-y'),
            y=alt.Y('Generation_MWh:Q', title='Total Generation (thousand MWh)'),
            color=alt.Color('Category:N',
                          legend=None),
            tooltip=[
                alt.Tooltip('Category:N', title='Category'),
                alt.Tooltip('Generation_MWh:Q', title='Total Generation (MWh)', format=',.0f')
            ]
        ).properties(
            width=600,
            height=400,
            title="Total California Electricity Generation by Category (2014-2024)"
        )

        return bars

    def generate_all_visualizations(self, output_dir: str = "output") -> None:
        """
        Generate all visualizations and save them to files.

        Args:
            output_dir (str): Directory to save visualizations
        """
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)

        print(f"Saving visualizations to {output_path.absolute()}")

        # Load data if not already loaded
        if self.processed_data is None:
            self.load_and_process_data()

        # Generate and save each chart
        charts = {
            'stacked_area': self.create_stacked_area_chart(),
            'trend_lines': self.create_trend_lines(),
            'summary_stats': self.create_summary_stats_chart()
        }

        # Save as HTML (interactive)
        for name, chart in charts.items():
            html_file = output_path / f'{name}_interactive.html'
            chart.save(str(html_file))
            print(f"  Saved {html_file}")

        # Save as PNG (static)
        for name, chart in charts.items():
            try:
                png_file = output_path / f'{name}_static.png'
                chart.save(str(png_file), ppi=300)
                print(f"  Saved {png_file}")
            except Exception as e:
                print(f"  Warning: Could not save PNG for {name}: {e}")


def main():
    """Main function to run the visualization generation."""
    print("Starting California Energy Visualization Generation")
    print("=" * 60)

    # Initialize visualizer
    visualizer = CaliforniaEnergyVisualizer()

    # Generate all visualizations
    visualizer.generate_all_visualizations()

    print("\nAll visualizations generated successfully!")
    print("Check the 'output' directory for HTML and PNG files.")


if __name__ == "__main__":
    main()
