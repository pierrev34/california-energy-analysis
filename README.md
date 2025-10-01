# California Energy Generation Analysis (2014-2024)

A comprehensive analysis of California's electricity generation transition, featuring interactive visualizations, statistical analysis, and actionable insights for energy policy and planning.

## Project Overview

This project analyzes California's electricity generation data from 2014-2024, tracking the evolution of the state's energy mix across different power generation categories. The analysis reveals trends in renewable energy adoption, fossil fuel dependency changes, and overall generation capacity growth.

## Analysis Results

### Key Findings (2014-2024)

| Metric | Value | Trend |
|--------|-------|-------|
| Total Generation | 5.3M MWh | +11.0% growth |
| Peak Year | 2023 | 529,678 MWh |
| Dominant Category | Electric Power | ~38% share |
| Fastest Growing | Non-Cogen Utilities | +26.6% |

### Category Performance

- Electric Utility Non-Cogen: Strongest growth (+26.6%)
- Independent Power Producers: Steady growth (+12.2%)
- Electric Utility Cogen: Steepest decline (-51.7%)
- Electric Power: Stable dominance (~38% share)

## Visualizations

### Interactive Charts

1. Stacked Area Chart - Energy mix evolution over time
   - Interactive percentage breakdown by category
   - Hover tooltips with detailed generation data

2. Trend Lines - Individual category trajectories
   - Year-over-year generation trends
   - Category comparison visualization

3. Summary Statistics - Total generation by category
   - Cumulative generation (2014-2024)
   - Visual category ranking

### Viewing Visualizations

All visualizations are saved as interactive HTML files in the output/ directory:

```bash
# Open main energy mix visualization
open output/stacked_area_interactive.html

# Open trend analysis
open output/trend_lines_interactive.html

# Open summary statistics
open output/summary_stats_interactive.html
```

## Advanced Usage

### Command Line Options

```bash
# Run analysis only (skip visualizations)
python main.py --skip-viz

# Use custom data file
python main.py --data-path path/to/custom_data.csv

# Get help
python main.py --help
```

### Module Usage

```python
# Import analysis modules
from src.analysis import CaliforniaEnergyAnalyzer
from src.visualization import CaliforniaEnergyVisualizer

# Run custom analysis
analyzer = CaliforniaEnergyAnalyzer()
analyzer.load_data()
analyzer.process_data()
results = analyzer.generate_insights()

# Generate custom visualizations
visualizer = CaliforniaEnergyVisualizer()
visualizer.generate_all_visualizations()
```

## License

This project is released under the MIT License. The EIA data is publicly available and used for educational and research purposes.

---

Last Updated: October 2025
Data Coverage: 2014-2024 (11 years, 55 data points)
