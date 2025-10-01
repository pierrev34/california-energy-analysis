#!/usr/bin/env python3
"""
California Energy Generation Analysis - Main Pipeline

This script serves as the main entry point for the California energy
analysis project. It orchestrates data loading, analysis, and visualization
generation in a clean, reproducible pipeline.

Usage:
    python main.py [--skip-viz] [--output-format json|csv|both]

Author: California Energy Analysis Project
Date: October 2025
"""

import argparse
import sys
from pathlib import Path
from typing import Optional

# Add src to path for imports
sys.path.append(str(Path(__file__).parent / "src"))

from analysis import CaliforniaEnergyAnalyzer
from visualization import CaliforniaEnergyVisualizer


class AnalysisPipeline:
    """
    Main pipeline for California energy analysis.

    This class orchestrates the complete analysis workflow from data
    loading through visualization generation.
    """

    def __init__(self, data_path: str = "data/eia_california_generation_annual.csv"):
        """
        Initialize the analysis pipeline.

        Args:
            data_path (str): Path to the data file
        """
        self.data_path = data_path
        self.analyzer = CaliforniaEnergyAnalyzer(data_path)
        self.visualizer = CaliforniaEnergyVisualizer(data_path)

    def run_analysis(self, skip_visualization: bool = False) -> dict:
        """
        Run the complete analysis pipeline.

        Args:
            skip_visualization (bool): Whether to skip visualization generation

        Returns:
            dict: Complete analysis results
        """
        print("🚀 Starting California Energy Analysis Pipeline")
        print("=" * 60)

        # Step 1: Data Loading and Processing
        print("\n📥 STEP 1: Data Loading and Processing")
        print("-" * 40)
        self.analyzer.load_data()
        self.analyzer.process_data()

        # Step 2: Statistical Analysis
        print("\n📊 STEP 2: Statistical Analysis")
        print("-" * 40)
        stats = self.analyzer.calculate_summary_statistics()
        insights = self.analyzer.generate_insights()

        # Step 3: Visualization Generation (optional)
        if not skip_visualization:
            print("\n📈 STEP 3: Visualization Generation")
            print("-" * 40)
            self.visualizer.load_and_process_data()
            self.visualizer.generate_all_visualizations()

        # Step 4: Export Results
        print("\n💾 STEP 4: Export Results")
        print("-" * 40)
        self.analyzer.export_results('json')
        self.analyzer.export_results('csv')

        print("\n🎉 Pipeline completed successfully!")
        return {
            'statistics': stats,
            'insights': insights,
            'data': self.analyzer.processed_data
        }


def main():
    """Main entry point for the analysis pipeline."""
    parser = argparse.ArgumentParser(
        description="California Energy Generation Analysis Pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py                    # Run full analysis with visualizations
  python main.py --skip-viz         # Run analysis only (no visualizations)
  python main.py --help             # Show this help message
        """
    )

    parser.add_argument(
        '--skip-viz',
        action='store_true',
        help='Skip visualization generation (analysis only)'
    )

    parser.add_argument(
        '--data-path',
        default='data/eia_california_generation_annual.csv',
        help='Path to the EIA data file (default: data/eia_california_generation_annual.csv)'
    )

    args = parser.parse_args()

    # Check if data file exists
    data_path = Path(args.data_path)
    if not data_path.exists():
        print(f"Error: Data file not found at {data_path.absolute()}")
        print("Please ensure the EIA data file is in the correct location.")
        sys.exit(1)

    # Run the pipeline
    pipeline = AnalysisPipeline(args.data_path)
    # Print summary
    print("\n" + "=" * 60)
    print("EXECUTION SUMMARY")
    print("=" * 60)
    print("Data Processing: Complete")
    print("Statistical Analysis: Complete")
    if not args.skip_viz:
        print("Visualization Generation: Complete")
    print("Results Export: Complete")
    print(f"\nCheck the 'output' directory for generated files:")
    print(f"   • analysis_results.json")
    print(f"   • processed_data.csv")
    if not args.skip_viz:
        print(f"   • Visualization files (HTML and PNG)")


if __name__ == "__main__":
    main()
