#!/usr/bin/env python3
"""
California Energy Analysis - Simple Version

This script analyzes California's electricity generation data from 2014-2024.
It loads the data, creates some basic charts, and shows key insights.

Usage: python main.py

Author: California Energy Project
"""

import pandas as pd
import matplotlib.pyplot as plt
import sys
from pathlib import Path

# Add src to path for imports
sys.path.append(str(Path(__file__).parent / "src"))

from analysis import CaliforniaEnergyAnalyzer


def main():
    """Main function to run the energy analysis."""
    print("Starting California Energy Analysis")
    print("=" * 40)

    # Check if data file exists
    data_path = Path("data/eia_california_generation_annual.csv")
    if not data_path.exists():
        print(f"Error: Can't find data file at {data_path}")
        print("Please download the EIA data file first.")
        return

    # Create analyzer and run analysis
    analyzer = CaliforniaEnergyAnalyzer(str(data_path))

    print("Loading and analyzing data...")
    analyzer.load_data()
    analyzer.process_data()
    stats = analyzer.calculate_summary_statistics()
    insights = analyzer.generate_insights()

    # Show basic results
    print("\n" + "=" * 40)
    print("ANALYSIS RESULTS")
    print("=" * 40)

    print("\nOverall:")
    print(f"  Total energy generated: {stats['overall']['total_generation_mwh']:,.0f} MWh")
    print(f"  Years analyzed: {stats['overall']['years_analyzed']}")
    print(f"  Growth rate: {stats['trends']['overall_growth_rate']:.1f}%")

    print("\nTop energy categories:")
    for category, cat_stats in list(stats['by_category'].items())[:3]:
        print(f"  {category}: {cat_stats['total_generation']:,.0f} MWh")

    print("\nKey insights:")
    for insight in insights['key_findings'][:3]:
        print(f"  • {insight}")

    # Save results
    print("\nSaving results...")
    analyzer.export_results('csv')

    print("\nDone! Check the 'output' folder for results.")
    print("Open output/processed_data.csv to see the data.")


if __name__ == "__main__":
    main()
