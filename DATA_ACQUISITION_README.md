# Data Acquisition Instructions for EIA California Energy Data

## Manual Download Instructions

To obtain the California electricity generation data from the EIA website, follow these steps:

1. **Navigate to the EIA Data Browser**:
   - Go to: https://www.eia.gov/electricity/data/browser/

2. **Select Data Series**:
   - In the "Data Series" section, select "Net generation"

3. **Select Geography**:
   - In the "Geography" section, select "California"

4. **Select Sector**:
   - In the "Sector" section, select "Electric Power Sector"

5. **Select Fuel Type**:
   - In the "Fuel Type" section, select "All fuel types"

6. **Select Time Period**:
   - In the "Time Period" section:
     - Select "Annual"
     - Set Start Year: 2014
     - Set End Year: Latest available (2024 or current year)

7. **Download the Data**:
   - Click the "Download" button
   - Select "CSV" format
   - Save the file as `eia_california_generation_annual.csv` in the project directory

8. **Expected Data Structure**:
   The downloaded CSV should contain columns including:
   - Year
   - Fuel Type
   - Net Generation (MWh)
   - Other metadata columns

## Alternative: Using EIA API (Advanced)

If you prefer to use the EIA API programmatically, you would need to:

1. Register for an EIA API key at: https://www.eia.gov/opendata/
2. Use the API endpoint for electricity generation data
3. The specific series for California electricity generation by fuel type would need to be identified through the API browser

## Data Validation

After downloading, verify that your CSV file contains:
- Annual data from 2014 onwards
- Multiple fuel types (Solar, Wind, Natural Gas, Coal, etc.)
- Net Generation values in MWh
- California-specific data only

The next phase will process this CSV file to create the energy transition visualization.
