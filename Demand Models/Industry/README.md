# Industry model

## Contents
This folder contains the code and data to run the steel model.

### code folder
The code runs in the following order
#### 1.MakeTidy.py
-Reshape steel production data in Tidy format
#### 2.createdatasets.py
- Combine historical steel production, historical GDP and historical population to one file and remove negative numbers
- Combine GDP and population projection data to one file
#### 3.ComputeFeatures.py
- Compute historical GDP per capita, production per capita and take natural logs for regression
- Compute projected GDP per capita and take natural logs for regression
#### 4.RunRegressions.py
- Project production per capita with linear regression of historical production per capita and GDP per capita
- Run regression for all economies
- Plot production per capita result for all economies 

### data folder
#### raw
- *IS_production7th.csv*
  Steel historical production data from 7th Edition
#### modified
- *TidySteel.csv* 
  Steel historical production data from 7th Edition in Tidy format
- *SteelHistorical.csv*
  Steel historical production, historical GDP and historical population data
- *GDPPop7thFuture.csv*
  GDP projection and population projection data
- *SteelHistoricalPrepared.csv*
  Historical GDP per capita, historical production per capita
  Historical GDP per capita with natural logs, historical production per capita with natural logs
- *GDPPop7thFuturePrepared.csv*
  GDP per capita projection and GDP per capita with natural logs projection
- *XX_EconomyPrediction.csv*
  Projected production per capita and with natural logs
  Projected GDP per capita for 21 economies
#### results
- *HistoricalPredictionResults.csv*
  Historical production per capita and with natural logs
  Historical GDP per capita
- *FutureProjectionResults.csv*
  Projected production per capita and with natural logs
  Projected GDP per capita
- *SteelResultsCombined.csv*
  Historical production per capita and with natural logs
  Historical GDP per capita
  Projected production per capita and with natural logs
  Projected GDP per capita

end