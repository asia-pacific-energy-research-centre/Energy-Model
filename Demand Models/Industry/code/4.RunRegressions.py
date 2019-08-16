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
from matplotlib.ticker import MultipleLocator, FixedLocator, FixedFormatter

print("Script started. -- Current date/time:", dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# import regression functions from RegressionFunctions.py
sys.path.insert(0, 'Demand Models/Industry/code')
from RegressionFunctions import run_regression, run_prediction, plot_results

# Perform regressions
# read in data from csv
SteelHistoricalPrepared = pd.read_csv(r'Demand Models\Industry\data\modified\SteelHistoricalPrepared.csv')
GDPPop7thFuturePrepared = pd.read_csv(r'Demand Models\Industry\data\modified\GDPPop7thFuturePrepared.csv')

# get list of economies and create economy-model pairs
economies = SteelHistoricalPrepared.Economy.unique()
models = {economy: LinearRegression() for economy in economies}

# set Economy as index 
df1 = SteelHistoricalPrepared.set_index('Economy')
# set explanatory variable x and dependent variable y
x = ['Year','lnGDPpercap'] # data that has relationship with y
y = ['lnConspercap'] # what you want to know

# run regression
SteelRegressionModel = run_regression(models, economies, df1, x, y)

print('\nGenerated regression. Please wait for plotting.\n')

# make predictions using historical values of GDP per capita
HistoricalX = df1[['Year','lnGDPpercap']]
ResultsColumn = ['Predicted Steel Consumption per capita']
HistoricalPredictionResults = run_prediction(SteelRegressionModel, economies, HistoricalX, ResultsColumn)

# make predictions using FUTURE values of GDP per capita
FutureX = GDPPop7thFuturePrepared.set_index('Economy')[['Year','lnGDPpercap']]
FuturePredictionResults = run_prediction(SteelRegressionModel, economies, FutureX, ResultsColumn)

# -- Compute steel consumption (instead of per capita)
# read historical and future population data from csv
Pop7thHistorical = pd.read_csv(r'Macro\data\results\Pop7thHistorical.csv')
Pop7thFuture = pd.read_csv(r'Macro\data\results\Pop7thFuture.csv')

# add population column to historical and future prediction results
HistoricalPredictionResults = pd.merge(HistoricalPredictionResults, Pop7thHistorical, how='left', on=['Economy','Year'])
FuturePredictionResults = pd.merge(FuturePredictionResults,Pop7thFuture, how='left',on=['Economy','Year'])

# compute steel consumption
HistoricalPredictionResults['Predicted Steel Consumption'] = HistoricalPredictionResults['Predicted Steel Consumption per capita'].mul(HistoricalPredictionResults['Population']).div(1000)
FuturePredictionResults['Predicted Steel Consumption'] = FuturePredictionResults['Predicted Steel Consumption per capita'].mul(FuturePredictionResults['Population']).div(1000)

# combine results
SteelResultsCombined = pd.concat([HistoricalPredictionResults,FuturePredictionResults])

# write results to csv
HistoricalPredictionResults.to_csv(r'Demand Models\Industry\data\results\HistoricalPredictionResults.csv', index=False)
FuturePredictionResults.to_csv(r'Demand Models\Industry\data\results\FuturePredictionResults.csv', index=False)
SteelResultsCombined.to_csv(r'Demand Models\Industry\data\results\SteelResultsCombined.csv', index=False)

print("Results are saved. -- Current date/time:", dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Plotting using the EGEDA plot code
figurename = 'Demand Models\Industry\steel consumption.png'
Plotylabel = 'thousand tonnes'

# create dataframe with Historical results in one column and Future in another
df1 = HistoricalPredictionResults.drop(['Predicted Steel Consumption per capita','Population'], axis=1)
df2 = FuturePredictionResults.drop(['Predicted Steel Consumption per capita','Population'], axis=1)
df1.rename(columns={'Predicted Steel Consumption':'Historical'},inplace=True)
df2.rename(columns={'Predicted Steel Consumption':'Future'},inplace=True)
dfPlot = pd.merge(df1,df2,how='outer')

# Create the 'figure'
plt.style.use('tableau-colorblind10')

# multiple line plot
fig, axes = plt.subplots(nrows=3, ncols=7, sharex=False, sharey=False, figsize=(16,12))
#x_locator = FixedLocator([1990, 2016,  2030, 2050])
for ax, economy,num in zip(axes.flatten(), economies, range(1,22)):
    print('Creating plot for %s...' %economy)
    df11=dfPlot[dfPlot['Economy']==economy]

    for column in df11.drop(['Economy','Year'], axis=1):
        ax.plot(df11['Year'], df11[column], marker='', linewidth=1.5, label=economy)
        ax.set_title(economy)
        ax.set_ylabel(Plotylabel)
        #ax.xaxis.set_major_locator(x_locator)
    # Same limits for everybody!
    ax.set_ylim(0,1000000)   
    ax.label_outer()

plt.tight_layout()
fig.legend( list(dfPlot.drop(['Economy','Year'], axis=1)),  loc='lower center', ncol=9)
fig.savefig(figurename,dpi=200)
print('Figure saved as %s' % figurename)
print('Preparing to show the figure...')
plt.show()