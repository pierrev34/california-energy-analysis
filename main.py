#!/usr/bin/env python3
"""
California Energy Analysis - Fuel-Based Analysis

This script analyzes California's electricity generation by fuel type from 2014-2024.
It auto-detects EIA CSV files, processes fuel categories, and generates insights
about the energy transition with corrected visualizations.

Usage: python main.py

Features:
- Auto-detects CSV in data/ folder
- Cleans and aggregates fuel categories
- Exports data, analysis results, and corrected stacked area chart
- Provides concise summary of key energy transition trends

Author: California Energy Analysis Project
"""

import pandas as pd
import matplotlib.pyplot as plt
import sys
from pathlib import Path

# Add src to path for imports
sys.path.append(str(Path(__file__).parent / "src"))

from analysis import CaliforniaEnergyAnalyzer


def main():
    """Main function to run the fuel-based energy analysis."""
    print("🔋 California Energy Analysis (2014-2024)")
    print("=" * 50)

    # Locate a data CSV automatically (prefer a fuel-based export if present)
    data_dir = Path("data")
    candidates = []
    if data_dir.exists():
        # Prefer common EIA naming that indicates net generation by fuel
        preferred_names = [
            "Net_generation_for_California.csv",
            "eia_california_generation_annual.csv",
        ]
        for name in preferred_names:
            p = data_dir / name
            if p.exists():
                candidates.append(p)
        # Fallback: any CSV in data/
        if not candidates:
            candidates = sorted(data_dir.glob("*.csv"))

    if not candidates:
        print("Error: No CSV data found in ./data")
        print("Place your EIA CSV export in the data/ folder and rerun.")
        return

    data_path = candidates[0]

    # Create analyzer and run analysis
    analyzer = CaliforniaEnergyAnalyzer(str(data_path))

    print("\n📊 Loading and analyzing fuel data...")
    analyzer.load_data()
    analyzer.process_data()
    stats = analyzer.calculate_summary_statistics()
    insights = analyzer.generate_insights()

    # Show basic results
    print("\n" + "=" * 50)
    print("🔍 ANALYSIS RESULTS")
    print("=" * 50)

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

    # Save results and generate chart
    print("\n💾 Exporting results and generating chart...")
    analyzer.export_results('json')
    analyzer.export_results('csv')
    analyzer.generate_stacked_area_png("output/energy_mix.png")

    print("\n✅ Analysis complete! Check the 'output' folder for:")
    print("   • processed_data.csv - Clean fuel data by year")
    print("   • analysis_results.json - Complete statistical analysis")  
    print("   • energy_mix.png - Corrected stacked area chart")


if __name__ == "__main__":
    main()
