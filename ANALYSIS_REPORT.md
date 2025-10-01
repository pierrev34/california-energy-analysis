# California Energy Generation Analysis (2014-2024)

## 📋 Project Overview

This project analyzes California's electricity generation transition from 2014 to 2024, examining the evolution of the state's energy mix across different power generation categories. The analysis reveals trends in renewable energy adoption, fossil fuel dependency changes, and overall generation capacity growth.

### Key Objectives

- **Track Energy Transition**: Monitor California's shift towards cleaner energy sources
- **Identify Trends**: Analyze year-over-year changes in generation by category
- **Provide Insights**: Generate actionable insights for energy policy and planning
- **Visualize Data**: Create interactive visualizations for better understanding

## Data Summary

### Dataset Information
- **Source**: U.S. Energy Information Administration (EIA)
- **Geographic Scope**: California state-wide electricity generation
- **Specific Query**: "Net generation for California" - All fuels (utility-scale)
- **Time Period**: 2014 - 2024 (11 years of complete data)
- **Units**: Thousand megawatthours (MWh)
- **Categories**: 5 major electricity generation sectors

### Data Categories Analyzed
1. **All fuels (utility-scale) : electric power** - Primary electricity generation sector
2. **All fuels (utility-scale) : electric utility** - Traditional utility company generation
3. **All fuels (utility-scale) : independent power producers** - Non-utility commercial generation
4. **All fuels (utility-scale) : electric utility non-cogen** - Non-cogeneration utility facilities
5. **All fuels (utility-scale) : electric utility cogen** - Cogeneration (combined heat and power) facilities

## Key Findings

### Overall Trends (2014-2024)

| Metric | Value | Change |
|--------|-------|--------|
| **Total Generation** | 5,309,680 MWh | +11.0% |
| **Peak Year** | 2023 (529,678 MWh) | - |
| **Lowest Year** | 2016 (460,053 MWh) | - |
| **Compound Growth** | - | +1.0% annually |

### Category Performance Highlights

#### Strong Growth Categories
- **Electric Utility Non-Cogen**: +26.6% increase (19.0% → 21.7% share)
- **Independent Power Producers**: +12.2% increase (23.3% → 23.5% share)

#### Declining Categories
- **Electric Utility Cogen**: -51.7% decrease (4.3% → 1.9% share)
- **Electric Utility**: -0.4% decrease (15.1% → 14.7% share)

#### Stable Categories
- **Electric Power**: Remained dominant (~38% share throughout period)

## Visualizations

### Interactive Charts Generated

1. **Stacked Area Chart** - Energy mix evolution over time
   - Shows percentage contribution of each category by year
   - Interactive tooltips with detailed generation data
   - Color-coded by energy category

2. **Trend Lines Chart** - Individual category trajectories
   - Line chart showing absolute generation trends
   - Point markers for each data point
   - Interactive hover details

3. **Summary Statistics** - Total generation by category
   - Bar chart of cumulative generation (2014-2024)
   - Sorted by total contribution
   - Interactive tooltips

### Visualization Files
- `output/stacked_area_interactive.html` - Main energy mix visualization
- `output/trend_lines_interactive.html` - Category trend analysis
- `output/summary_stats_interactive.html` - Total generation summary

## Detailed Analysis

### Category Breakdown

#### Electric Power (Dominant Category)
- **Total Generation**: 2,043,855 MWh (38.5% of total)
- **Trend**: Stable at ~38-39% throughout period
- **Peak Year**: 2023 (202,437 MWh)
- **Growth**: +10.6% overall

#### Independent Power Producers (Growing Segment)
- **Total Generation**: 1,221,969 MWh (23.0% of total)
- **Trend**: Steady growth trajectory
- **Peak Year**: 2024 (123,208 MWh)
- **Growth**: +12.2% overall

#### Electric Utility Non-Cogen (Fastest Growing)
- **Total Generation**: 1,065,700 MWh (20.1% of total)
- **Trend**: Strongest growth pattern
- **Peak Year**: 2023 (113,254 MWh)
- **Growth**: +26.6% overall

#### Electric Utility (Declining)
- **Total Generation**: 821,886 MWh (15.5% of total)
- **Trend**: Gradual decline
- **Peak Year**: 2017 (90,422 MWh)
- **Growth**: -8.2% overall

#### Electric Utility Cogen (Steepest Decline)
- **Total Generation**: 156,270 MWh (2.9% of total)
- **Trend**: Significant decline throughout period
- **Peak Year**: 2014 (20,208 MWh)
- **Growth**: -51.7% overall

### Year-by-Year Analysis

| Year | Total Generation (MWh) | Growth Rate | Dominant Category |
|------|------------------------|-------------|-------------------|
| 2014 | 471,427 | - | Electric Power (38.4%) |
| 2015 | 466,762 | -1.0% | Electric Power (38.4%) |
| 2016 | 460,053 | -1.4% | Electric Power (39.2%) |
| 2017 | 478,869 | +4.1% | Electric Power (39.6%) |
| 2018 | 462,123 | -3.5% | Electric Power (38.8%) |
| 2019 | 473,246 | +2.4% | Electric Power (39.2%) |
| 2020 | 462,701 | -2.2% | Electric Power (38.2%) |
| 2021 | 481,762 | +4.1% | Electric Power (37.6%) |
| 2022 | 499,725 | +3.7% | Electric Power (37.7%) |
| 2023 | 529,678 | +6.0% | Electric Power (38.2%) |
| 2024 | 523,334 | -1.2% | Electric Power (38.2%) |

## Energy Transition Insights

### Renewable Energy Trends
- **Overall Progress**: Moderate growth in cleaner energy segments
- **Challenges**: Fossil fuel dependency remains significant (~60% combined)
- **Opportunities**: Non-cogen utilities showing strong expansion potential

### Policy Implications
1. **Support Non-Cogen Growth**: Policies encouraging non-cogeneration facilities expansion
2. **Address Cogen Decline**: Investigate causes of cogeneration facility reductions
3. **Maintain Electric Power Stability**: Ensure continued reliability of primary generation

## 🛠 Technical Implementation

### Project Structure
```
california-energy-analysis/
├── main.py                 # Main pipeline script
├── src/
│   ├── analysis.py        # Core analysis module
│   └── visualization.py   # Visualization generation
├── data/
│   └── eia_california_generation_annual.csv
├── output/                # Generated files
│   ├── analysis_results.json
│   ├── processed_data.csv
│   └── *.html             # Interactive visualizations
└── docs/                  # Documentation
```

### Technologies Used
- **Python 3.12**: Core programming language
- **Pandas**: Data manipulation and analysis
- **Altair**: Interactive visualization library
- **Jupyter**: Notebook environment support
- **EIA API**: Data source integration

### Code Quality Features
- **Modular Design**: Separated analysis and visualization logic
- **Type Hints**: Enhanced code readability and IDE support
- **Comprehensive Documentation**: Detailed docstrings and comments
- **Error Handling**: Robust error handling and user feedback
- **Clean Architecture**: Well-organized, maintainable codebase

## Usage Instructions

### Quick Start
```bash
# Clone the repository
git clone <repository-url>
cd california-energy-analysis

# Install dependencies
pip install pandas altair matplotlib jupyter

# Run complete analysis
python main.py

# View results
open output/stacked_area_interactive.html
```

### Advanced Usage
```bash
# Run analysis only (no visualizations)
python main.py --skip-viz

# Custom data path
python main.py --data-path custom_data.csv
```

### Development Setup
```bash
# Install development dependencies
pip install -r requirements.txt

# Run tests (if implemented)
python -m pytest

# Generate documentation
python docs/generate_docs.py
```

## 📁 Output Files

### Data Files
- `output/processed_data.csv` - Clean, processed dataset
- `output/analysis_results.json` - Complete statistical analysis

### Visualization Files
- `output/stacked_area_interactive.html` - Main energy mix visualization
- `output/trend_lines_interactive.html` - Category trend analysis
- `output/summary_stats_interactive.html` - Summary statistics

## Future Enhancements

### Potential Improvements
1. **Real-time Data Integration**: Connect to live EIA API feeds
2. **Comparative Analysis**: Add other states for comparison
3. **Predictive Modeling**: Implement forecasting algorithms
4. **Enhanced Visualizations**: Add more chart types and animations
5. **Interactive Dashboard**: Create web-based dashboard interface

### Research Extensions
1. **Carbon Intensity Analysis**: Calculate emissions per category
2. **Cost Analysis**: Incorporate generation cost data
3. **Regional Breakdown**: Analyze by utility service areas
4. **Weather Correlation**: Study weather impact on generation

## References and Data Sources

- **U.S. Energy Information Administration**: https://www.eia.gov/electricity/data/browser/
- **California Energy Commission**: https://www.energy.ca.gov/
- **EPA Emissions Data**: https://www.epa.gov/power-sector

## Contributing

### Development Guidelines
- Follow PEP 8 style guidelines
- Add type hints for all functions
- Include comprehensive docstrings
- Write tests for new functionality
- Update documentation for changes

### Issue Reporting
- Use GitHub Issues for bug reports
- Include detailed reproduction steps
- Provide sample data when relevant
- Tag issues appropriately (bug, enhancement, question)

## License

This project uses publicly available EIA data and is intended for educational and research purposes. The code is released under the MIT License.

---

*Generated on: October 2025*
*Analysis Period: 2014-2024*
*Total Data Points Analyzed: 55*
