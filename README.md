# California Energy Analysis (2014-2024)

## Project Overview

This project analyzes California's electricity production from 2014 to 2024, examining how different types of power plants have grown or declined over time.

### What We Want to Learn
- How California's energy mix is changing
- Which types of power are growing or shrinking
- Basic trends in electricity production
- Simple charts to understand the data better

## Data Summary

### Where the Data Comes From
- **Source**: U.S. Energy Information Administration (EIA)
- **Location**: California statewide
- **Type**: Total electricity generation by power plant type
- **Time Period**: 2014-2024 (11 years)
- **Units**: Thousand megawatt-hours (MWh)
- **Categories**: 5 main types of power plants

### Types of Power Plants We Analyze
1. **Electric Power** - Main power companies
2. **Electric Utility** - Traditional utility companies
3. **Independent Power Producers** - Non-utility commercial power
4. **Electric Utility Non-Cogen** - Power plants not using waste heat
5. **Electric Utility Cogen** - Power plants using waste heat

## Key Findings

### Overall Energy Trends Show Modest Growth with Shifting Mix

California's electricity generation grew 11% from 2014 to 2024, but the composition of power sources changed significantly. Total generation reached 5.3 million MWh with 2023 being the peak year at 529,678 MWh.

**Overall Generation Trends (2014-2024):**

| Year | Total Power (MWh) | Growth Rate | Dominant Category |
|------|-------------------|-------------|-------------------|
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

The data reveals volatile year-to-year changes with an overall upward trend of 1% annually, though 2023-2024 showed a slight decline.

### Electric Power Remains Dominant Despite Market Evolution

Electric Power consistently represented ~38% of California's electricity throughout the decade, demonstrating remarkable stability in the face of changing market conditions.

**Category Performance Summary:**

| Category | Total Generation | Share | Growth Rate | Trend |
|----------|------------------|-------|-------------|-------|
| Electric Power | 2,043,855 MWh | 38.5% | +10.6% | Stable dominance |
| Independent Power Producers | 1,221,969 MWh | 23.0% | +12.2% | Steady growth |
| Electric Utility Non-Cogen | 1,065,700 MWh | 20.1% | +26.6% | Fastest growing |
| Electric Utility | 821,886 MWh | 15.5% | -8.2% | Declining |
| Electric Utility Cogen | 156,270 MWh | 2.9% | -51.7% | Steepest decline |

### Growth Categories Show Promise for Energy Transition

Two categories demonstrated significant growth over the decade:

**Electric Utility Non-Cogen** emerged as the fastest-growing segment with a 26.6% increase, expanding from 19.0% to 21.7% market share. This suggests efficient, modern power plant designs are gaining traction.

**Independent Power Producers** showed steady 12.2% growth, increasing from 23.3% to 23.5% of total generation, indicating continued viability of non-utility commercial power production.

### Declining Sectors Reveal Market Pressures

**Electric Utility Cogen** experienced the most dramatic decline at -51.7%, dropping from 4.3% to just 1.9% of market share. This suggests combined heat and power facilities face significant operational or economic challenges.

**Electric Utility** showed moderate decline of -8.2%, reducing from 15.1% to 14.7% share, indicating traditional utility models may be losing ground to more specialized approaches.

## Visualizations

### Interactive Charts

The analysis generated three key visualizations to illustrate these trends:

1. **Stacked Area Chart** (`output/stacked_area_interactive.html`) - Shows how each power type's contribution changed over time
2. **Trend Lines** (`output/trend_lines_interactive.html`) - Displays individual category trajectories
3. **Summary Statistics** (`output/summary_stats_interactive.html`) - Presents cumulative generation by category

## Implications and Insights

### Energy Transition Progress

The data shows California's energy sector is undergoing gradual but uneven transformation. While total generation grew 11%, the shift toward newer power plant designs (particularly non-cogeneration facilities) suggests modernization efforts are bearing fruit.

### Market Dynamics

The stability of Electric Power (maintaining ~38% dominance) alongside growth in Independent Power Producers indicates a maturing market where traditional and alternative power sources coexist. However, the sharp decline in cogeneration facilities raises questions about the viability of combined heat and power systems.

### Policy Considerations

These findings suggest policymakers should:
1. **Support Non-Cogen Growth** - Encourage expansion of efficient, modern power plant designs
2. **Investigate Cogen Decline** - Understand why combined heat and power facilities are struggling
3. **Monitor Electric Power Stability** - Ensure continued reliability of the dominant power source

## How to Use This

### Quick Start
```bash
# Get the project
git clone <repository-url>
cd california-energy-analysis

# Install basic packages
pip install pandas altair matplotlib jupyter

# Run the analysis
python main.py

# Look at results
open output/stacked_area_interactive.html
```

### Other Options
```bash
# Just analyze data (no charts)
python main.py --skip-viz

# Use different data file
python main.py --data-path my_data.csv
```

## References

- **U.S. Energy Information Administration**: https://www.eia.gov/electricity/data/browser/
- **California Energy Commission**: https://www.energy.ca.gov/

---
*Analysis Period: 2014-2024*
*Total Data Points: 55*
