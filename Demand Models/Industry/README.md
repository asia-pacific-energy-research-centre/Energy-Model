# Steel model

## Contents
This folder contains the code and data to run the steel model.

### code folder
The code runs in the following order

#### 1.MakeTidy.py
- Reshape steel consumption data in Tidy format.
#### 2.createdatasets.py
- Combine historical steel consumption, GDP and population to one file and remove negative numbers.
- Combine projected GDP and population to one file.
#### 3.ComputeFeatures.py
- Compute historical GDP per capita, consumption per capita and take natural logs for regression.
- Compute projected GDP per capita and take natural logs for regression.
#### 4.RunRegressions.py
- Compute projected consumption per capita with linear regression of historical consumption per capita and historical GDP per capita.
- Run regression for all economies.
- Plot historical and projected consumption per capita result for all economies.

### data folder
Each file has data for all economies unless else specified.

#### 1.raw
- *IS_consumption7th.csv*
  - Historical steel consumption data from 7th Edition
#### 2.modified
These files are created from running the code1-4.
- *TidySteel.csv* 
  - Historical steel consumption data from 7th Edition in Tidy format
- *SteelHistorical.csv*
  - Historical steel consumption, GDP and population data
- *GDPPop7thFuture.csv*
  - Projected GDP and population data
- *SteelHistoricalPrepared.csv*
  - Historical steel consumption, GDP and population
  - Historical GDP per capita and with natural logs
  - Historical consumption per capita and with natural logs
- *GDPPop7thFuturePrepared.csv*
  - Projected GDP and population data
  - Projected GDP per capita and with natural logs
  - Projected population per capita and with natural logs
- *XX_EconomyPrediction.csv* 
  - 19 projection files are created for each economy: 01_AUS to 21_VN (Note: 02_BD and 13_PNG are excluded because of data unavailability
  - Projected GDP per capita and with natural logs
  - Projected consumption per capita and with natural logs
#### 3.results
These files are created from running the code4.
- *HistoricalPredictionResults.csv*
  - Historical GDP per capita
  - Historical consumption per capita and with natural logs
- *FutureProjectionResults.csv*
  - Projected GDP per capita
  - Projected consumption per capita and with natural logs
- *SteelResultsCombined.csv*
  - Historical GDP per capita
  - Historical consumption per capita and with natural logs
  - Projected GDP per capita
  - Projected consumption per capita and with natural logs
  
