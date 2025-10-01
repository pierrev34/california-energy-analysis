# California Energy Analysis (2014-2024)

## Project Overview

This project looks at how California's electricity production changed from 2014 to 2024. We examine different types of power plants and how they've grown or declined over time.

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

## Key Results

### Overall Trends (2014-2024)

| Metric | Value | Change |
|--------|-------|--------|
| **Total Power** | 5,309,680 MWh | +11.0% |
| **Best Year** | 2023 (529,678 MWh) | - |
| **Worst Year** | 2016 (460,053 MWh) | - |
| **Growth Rate** | - | +1.0% per year |

### How Each Power Type Performed

#### Growing Power Types
- **Electric Utility Non-Cogen**: +26.6% (19.0% → 21.7% of total)
- **Independent Power Producers**: +12.2% (23.3% → 23.5% of total)

#### Declining Power Types
- **Electric Utility Cogen**: -51.7% (4.3% → 1.9% of total)
- **Electric Utility**: -0.4% (15.1% → 14.7% of total)

#### Steady Power Types
- **Electric Power**: Stayed around 38% of total power

## Charts We Created

### Types of Charts
1. **Stacked Area Chart** - Shows how each power type changed over time
2. **Trend Lines** - Shows each power type's individual path
3. **Summary Bars** - Shows total power from each type (2014-2024)

### Chart Files
- `output/stacked_area_interactive.html` - Main energy mix chart
- `output/trend_lines_interactive.html` - Individual power type trends
- `output/summary_stats_interactive.html` - Total power summary

## Detailed Analysis

### Electric Power (Biggest Source)
- **Total**: 2,043,855 MWh (38.5% of all power)
- **Trend**: Very steady at 38-39%
- **Best Year**: 2023 (202,437 MWh)
- **Growth**: +10.6% overall

#### Independent Power Producers (Growing Fast)
- **Total**: 1,221,969 MWh (23.0% of all power)
- **Trend**: Steady growth
- **Best Year**: 2024 (123,208 MWh)
- **Growth**: +12.2% overall

#### Electric Utility Non-Cogen (Fastest Growth)
- **Total**: 1,065,700 MWh (20.1% of all power)
- **Trend**: Strongest growth pattern
- **Best Year**: 2023 (113,254 MWh)
- **Growth**: +26.6% overall

#### Electric Utility (Going Down)
- **Total**: 821,886 MWh (15.5% of all power)
- **Trend**: Slow decline
- **Best Year**: 2017 (90,422 MWh)
- **Growth**: -8.2% overall

#### Electric Utility Cogen (Biggest Decline)
- **Total**: 156,270 MWh (2.9% of all power)
- **Trend**: Major decline
- **Best Year**: 2014 (20,208 MWh)
- **Growth**: -51.7% overall

### Year-by-Year Power Production

| Year | Total Power (MWh) | Growth | Main Power Type |
|------|-------------------|--------|-----------------|
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

## What This Means for Energy

### Clean Energy Trends
- **Progress**: Some growth in cleaner power types
- **Challenge**: Still lots of fossil fuel power (~60%)
- **Opportunity**: Non-cogen utilities growing well

### What We Should Do
1. **Support Non-Cogen Growth**: Help these efficient plants expand
2. **Fix Cogen Decline**: Figure out why these plants are struggling
3. **Keep Electric Power Stable**: Make sure main power sources stay reliable

## How We Built This

### Project Structure
```
california-energy-analysis/
├── main.py                 # Main analysis script
├── src/
│   ├── analysis.py        # Data analysis code
│   └── visualization.py   # Chart creation code
├── data/
│   └── energy_data.csv    # Raw data file
├── output/                # Results and charts
└── docs/                  # Documentation
```

### Tools We Used
- **Python**: Main programming language
- **Pandas**: For working with data
- **Altair**: For making interactive charts
- **EIA Data**: Where we got the energy information

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

## What We Learned

This analysis shows California's energy system is slowly changing. Electric Power stays dominant while some newer types grow and older types decline. The data helps us understand trends and make better energy decisions.

## References

- **U.S. Energy Information Administration**: https://www.eia.gov/electricity/data/browser/
- **California Energy Commission**: https://www.energy.ca.gov/

---
*Analysis Period: 2014-2024*
*Total Data Points: 55*
