# Steel Consumption model

## Contents
This folder contains the code and data to run the steel model.

### code folder
The code runs in the following order:

#### 1.MakeTidy.py
- Reshape steel consumption data in Tidy format.
- The `modified` and `results` folders are created by this script.
#### 2.createdatasets.py
- Combine historical steel consumption, GDP and population to one file and remove negative numbers.
- Combine projected GDP and population to one file.
- Runs `MakeMacroTidy.py` to generate the GDP and population datasets.
#### 3.ComputeFeatures.py
- Compute historical GDP per capita, consumption per capita and take natural logs for regression.
- Compute projected GDP per capita and take natural logs for regression.
#### 4.RunRegressions.py
- Run regressions using historical and future values created in previous steps.
- This file calls functions created in `RegressionFunctions.py`.

#### RegressionFunctions.py
File containing user-created functions to:
- Generate linear regression model for all 21 economies.
- Generate predicted consumption for all 21 economies.
- Plot historical and projected consumption result for all 21 economies.

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
  - Projected GDP per capita and with natural logs
  - Projected consumption per capita and with natural logs
#### 3.results
These files are created from running the code4.
- *HistoricalPredictionResults.csv*
  - Historical consumption per capita
  - Historical population
  - Historical consumption
- *FuturePredictionResults.csv*
  - Projected consumption per capita
  - Projected population
  - Porjected consumption
- *SteelResultsCombined.csv*
  - Historical and projected consumption per capita
  - Historical and projected population
  - Historical and projected consumption  
