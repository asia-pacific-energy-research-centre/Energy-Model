# SteelDemand.py
# Steel Demand Model

# import math and data table functions
import numpy as np
import pandas as pd
import os
import sys
import subprocess
import datetime as dt
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from matplotlib.ticker import MultipleLocator, FixedLocator, FixedFormatter

# import regression functions from RegressionFunctions.py
sys.path.insert(0, 'code')
from CommonFunctions import run_regression, run_prediction, plot2

print("Script started. -- Current date/time:", dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# create directories for modified and results data
paths = {'path1':'data\modified','path2':'data\modified','path3':'data\processed', 'path4':'results', 'path5':'reports'}
for key, value in paths.items(): 
        try:
            os.makedirs(value)
        except OSError:
            print ("Directory %s exists." % value)
        else:
            print ("Successfully created the directory %s " % value)

## run Macro script to create Macro data
runMacro = 'python code\MakeMacroTidy.py'
subprocess.run(runMacro, shell=False)

# STEP 1: read in raw steel data
RawSteelData = pd.read_csv(r'data\raw\Industry\IS_consumption7th.csv')
TidySteel = RawSteelData.set_index('Economy').stack().reset_index(name='SteelConsumption')
TidySteel.rename(columns={'level_1':'Year'}, inplace=True)
TidySteel.astype({'Year': 'int64'}).dtypes

# replace economies using APEC approved abbreviations
EconomyNames = {
    '01_AUS':'AUS',
    '02_BD':'BD',
    '03_CDA':'CDA',
    '04_CHL':'CHL',
    '05_PRC':'PRC',
    '06_HKC':'HKC',
    '07_INA':'INA',
    '08_JPN':'JPN',
    '09_ROK':'KOR',
    '10_MAS':'MAS',
    '11_MEX':'MEX',
    '12_NZ':'NZ',
    '13_PNG':'PNG',
    '14_PE':'PE',
    '15_RP':'RP',
    '16_RUS':'RUS',
    '17_SIN':'SIN',
    '18_CT':'CT',
    '19_THA':'THA',
    '20_USA':'USA',
    '21_VN':'VN'}

TidySteel.replace(EconomyNames, inplace=True)
TidySteel.astype({'Year': 'int64'})

# write to csv
TidySteel.to_csv(r'data/modified/TidySteel.csv', index=False)

# STEP 2
# read data from csv and store as dataframe
TidySteel = pd.read_csv(r'data\modified\TidySteel.csv')

# import historical GDP and population
GDP7thHistorical = pd.read_csv(r'data\processed\GDP7thHistorical.csv')
Pop7thHistorical = pd.read_csv(r'data\processed\Pop7thHistorical.csv')

# combine historical data in to one dataframe
SteelHistorical = pd.merge(GDP7thHistorical, TidySteel, how='left', on=['Economy','Year'])
SteelHistorical = pd.merge(SteelHistorical,Pop7thHistorical,how='left',on=['Economy','Year'])

# Replace negative numbers with NaN
# The 7th Edition steel data used negative numbers to indicate NaNs.
# Instead of dropping NaN, 'impute' the values by using mean, median, min, etc
# this replaces the NaN for BD, PNG, and RUS with min values across all economies
# Note that the BD, PNG values are too high - need to impute by economy
SteelHistorical.loc[SteelHistorical['SteelConsumption'] < 0,'SteelConsumption'] = np.NaN
#SteelHistorical.fillna(SteelHistorical[['SteelConsumption']].mean(), inplace=True)

i = SteelHistorical[['SteelConsumption']].min()
SteelHistorical.loc[SteelHistorical['Economy'].isin(['BD','PNG'])] = SteelHistorical.loc[SteelHistorical['Economy'].isin(['BD','PNG'])].fillna(i)
j = SteelHistorical.loc[SteelHistorical['Economy']=='RUS','SteelConsumption'].mean()
SteelHistorical.loc[SteelHistorical['Economy'].isin(['RUS'])] = SteelHistorical.loc[SteelHistorical['Economy'].isin(['RUS'])].fillna(j)

# combine future GDP and population, drop the world value
GDP7thFuture = pd.read_csv(r'data\processed\GDP7thFuture.csv')
Pop7thFuture = pd.read_csv(r'data\processed\Pop7thFuture.csv')

GDPPop7thFuture = pd.merge(GDP7thFuture,Pop7thFuture,how='left',on=['Economy','Year']).reset_index(drop=True)

# compute per capita then take natural logs
SteelHistorical['GDPpercap'] = SteelHistorical['GDP'].div(SteelHistorical['Population'])
SteelHistorical['Conspercap'] = SteelHistorical['SteelConsumption'].div(SteelHistorical['Population'])

SteelHistorical['lnGDPpercap'] = np.log(SteelHistorical['GDPpercap'])
SteelHistorical['lnConspercap'] = np.log(SteelHistorical['Conspercap'])

GDPPop7thFuture['GDPpercap'] = GDPPop7thFuture['GDP'].div(GDPPop7thFuture['Population'])
GDPPop7thFuture['lnGDPpercap'] = np.log(GDPPop7thFuture['GDPpercap'])

# write prepared data to csv
SteelHistorical.to_csv(r'data\modified\SteelHistoricalPrepared.csv', index=False)   
GDPPop7thFuture.to_csv(r'data\modified\GDPPop7thFuturePrepared.csv', index=False)

# STEP 3: perform regressions
# read in data from csv
SteelHistoricalPrepared = pd.read_csv(r'data\modified\SteelHistoricalPrepared.csv')
GDPPop7thFuturePrepared = pd.read_csv(r'data\modified\GDPPop7thFuturePrepared.csv')

# get list of economies and create economy-model pairs
economies = SteelHistoricalPrepared.Economy.unique()
models = {economy: LinearRegression() for economy in economies}

# set Economy as index
df1 = SteelHistoricalPrepared.set_index('Economy')

# set explanatory variable x and dependent variable y
# x = data that has relationship with y
# y = what you want to know
x = ['Year','lnGDPpercap']
y = ['lnConspercap']

# STEP 4: run regression
# run_regression is a function from CommonFunctions.py
SteelRegressionModel = run_regression(models, economies, df1, x, y)

print('\nGenerated regression. Please wait for plotting.\n')

# make predictions using historical values of GDP per capita
HistoricalX = df1[['Year','lnGDPpercap']]
ResultsColumn = ['Predicted Steel Consumption per capita']
HistoricalPredictionResults = run_prediction(SteelRegressionModel, economies, HistoricalX, ResultsColumn)

# STEP 5: make future predictions
print('\nMaking predictions...\n')
# make predictions using FUTURE values of GDP per capita
FutureX = GDPPop7thFuturePrepared.set_index('Economy')[['Year','lnGDPpercap']]
FuturePredictionResults = run_prediction(SteelRegressionModel, economies, FutureX, ResultsColumn)

# Compute steel consumption (instead of per capita)
# add population column to historical and future prediction results
HistoricalPredictionResults = pd.merge(HistoricalPredictionResults, Pop7thHistorical, how='left', on=['Economy','Year'])
FuturePredictionResults = pd.merge(FuturePredictionResults,Pop7thFuture, how='left',on=['Economy','Year'])

# compute steel consumption by multiplyingPer Capita consumption by population
HistoricalPredictionResults['Predicted Steel Consumption'] = HistoricalPredictionResults['Predicted Steel Consumption per capita'].mul(HistoricalPredictionResults['Population']).div(1000000)
FuturePredictionResults['Predicted Steel Consumption'] = FuturePredictionResults['Predicted Steel Consumption per capita'].mul(FuturePredictionResults['Population']).div(1000000)

print('\nFinished predictions!\n')

# combine results in to one dataframe
SteelResultsCombined = pd.concat([HistoricalPredictionResults,FuturePredictionResults])

# write results to csv
HistoricalPredictionResults.to_csv(r'data\processed\HistoricalPredictionResults.csv', index=False)
FuturePredictionResults.to_csv(r'data\processed\FuturePredictionResults.csv', index=False)
SteelResultsCombined.to_csv(r'data\processed\SteelResultsCombined.csv', index=False)

# STEP 6 - plot results
# set file name
# Use sharex and sharey = True or False to share those axes
figurename = 'reports\steel consumption.png'
Plotylabel = 'million tonnes'
sharex = True
sharey = True

# create dataframe with Historical results in one column and Future in another
df1 = HistoricalPredictionResults.drop(['Predicted Steel Consumption per capita','Population'], axis=1)
df2 = FuturePredictionResults.drop(['Predicted Steel Consumption per capita','Population'], axis=1)
df1.rename(columns={'Predicted Steel Consumption':'Historical'},inplace=True)
df2.rename(columns={'Predicted Steel Consumption':'Future'},inplace=True)
dfPlot = pd.merge(df1,df2,how='outer')

# Create the figure
# plot2 is a function from CommonFunctions.py
print('Preparing to show the figure...')
plot2(economies, dfPlot, figurename, Plotylabel, sharex, sharey)
print('Figure saved as %s' % figurename)

# Finished
print("\nFINISHED. -- Current date/time:", dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print('\nSteel consumption demand saved in the folder %s' %paths['path3'])