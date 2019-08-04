# RunRegressions.py
# create linear regrssion models for all 21 economies

# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import sys
import datetime as dt

print("Script started. -- Current date/time:", dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# import regression functions from RegressionFunctions.py
sys.path.insert(0, 'Demand Models/Industry/code')
from RegressionFunctions import run_regression, run_prediction, plot_results

# Perform regressions
# read in data from csv
SteelHistoricalPrepared = pd.read_csv(r'Demand Models/Industry/data/modified/SteelHistoricalPrepared.csv')
GDPPop7thFuturePrepared = pd.read_csv(r'Demand Models/Industry/data/modified/GDPPop7thFuturePrepared.csv')

# get list of economies and create economy-model pairs
economies = SteelHistoricalPrepared.Economy.unique()
models = {economy: LinearRegression() for economy in economies}

# set Economy as index and set target vector by dropping all other columns except lnGDPpercap and lnConspercap
df1 = (SteelHistoricalPrepared.set_index('Economy')
       .drop(['GDP','SteelConsumption','Population','GDPpercap','Conspercap'], axis=1))

# run regression
SteelRegressionModel = run_regression(models, economies, df1)

print('/nGenerated regression. Please wait for plotting./n')

# define future GDP per capita (ln) for future predictions
FutureX = (GDPPop7thFuturePrepared.set_index('Economy')
                                                   .drop(['GDP','Population','GDPpercap'], axis=1))     

# make predictions using historical values of GDP per capita
HistoricalX = df1.drop('lnConspercap', axis=1)
HistoricalPredictionResults = run_prediction(SteelRegressionModel, economies, HistoricalX)
FuturePredictionResults = run_prediction(SteelRegressionModel, economies, FutureX)

# add population to historcal and future results
# read historical data from csv and store as dataframe
Pop7thHistorical = pd.read_csv(r'Macro/data/results/Pop7thHistorical.csv')
Pop7thFuture = pd.read_csv(r'Macro/data/results/Pop7thFuture.csv')

# add population to historical and future prediction results
HistoricalPredictionResults = pd.merge(HistoricalPredictionResults, Pop7thHistorical, how='left', on=['Economy','Year'])
FuturePredictionResults = pd.merge(FuturePredictionResults, Pop7thFuture, how='left', on=['Economy','Year'])

# compute historical and future steel consumption
HistoricalPredictionResults['Predicted Steel Consumption'] = HistoricalPredictionResults['Predicted Steel Consumption per capita'].mul(HistoricalPredictionResults['Population']).div(1000)
FuturePredictionResults['Predicted Steel Consumption'] = FuturePredictionResults['Predicted Steel Consumption per capita'].mul(FuturePredictionResults['Population']).div(1000)


# plot historical and future predictions
plot_results(economies, HistoricalPredictionResults, FuturePredictionResults)

# combine results
SteelResultsCombined = pd.concat([HistoricalPredictionResults,FuturePredictionResults])

# write results to csv
HistoricalPredictionResults.to_csv(r'Demand Models/Industry/data/results/HistoricalPredictionResults.csv', index=False)
FuturePredictionResults.to_csv(r'Demand Models/Industry/data/results/FuturePredictionResults.csv', index=False)
SteelResultsCombined.to_csv(r'Demand Models/Industry/data/results/SteelResultsCombined.csv', index=False)

print("Results are saved. -- Current date/time:", dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))