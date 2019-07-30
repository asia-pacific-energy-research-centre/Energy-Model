# RunRegressions.py
# create linear models for all 21 economies

# step 1: create dictionary of model instances
# step 2: loop over economy, model pairs

# for future:
# https://www.dataquest.io/blog/settingwithcopywarning/

# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# define functions to perform regressions and predictions, and to plot results
# loop over economy-model pairs to fit regression
def run_regression(models, economies, df):
        for economy, model in models.items():
                (model.fit(df.loc[economy, :]
                      .drop('lnConspercap', axis=1),
                    df.loc[economy, 'lnConspercap']))
        return models            

# create function for performing prediction and writing results
# loop over economy-model pairs to make prediction and write prediction to csv, one for each economy
def run_prediction(models, economies, years, df):
        filelist = []
        for economy, model in models.items():
                prediction = model.predict(df.loc[economy,:])
                results = years[years.Economy == economy]
                results['prediction'] = prediction
                results['Consumptionpercap'] = np.exp(prediction)
                newfilename = '%sPrediction.csv' %economy
                results.to_csv(r'Demand Models\Industry\data\modified\%s' %newfilename, header=True)
                filelist.append(newfilename)

        # read in all csv and combine to one df
        df_list =[]
        for economy in economies:
                newfilename = '%sPrediction.csv' %economy
                df_list.append(pd.read_csv(r'Demand Models\Industry\data\modified\%s' %newfilename))
        dfResults = pd.concat(df_list).drop('Unnamed: 0', axis=1)
        dfResults['GDPpercap'] = SteelHistoricalPrepared['GDPpercap']
#        dfResults.to_csv(r'data\results\SteelPredictionsAll.csv')
        
        return dfResults

# define function to plot using matplotlib
def plot_results(economies, df1, df2):
        fig = plt.figure(figsize=[8,16])

        for economy,num in zip(economies, range(1,20)):
                df11=df1[df1['Economy']==economy]
                df21=df2[df2['Economy']==economy]
                ax = fig.add_subplot(7,3,num)
                ax.plot(df11['Year'], df11[['Consumptionpercap']],'r')
                ax.plot(df21['Year'], df21[['Consumptionpercap']],'b')
                ax.set_title(economy)

                #plt.tight_layout()
        plt.show()
##################################
# end of functions
##################################

# Perform regressions
# read in data from csv
SteelHistoricalPrepared = pd.read_csv(r'Demand Models\Industry\data\modified\SteelHistoricalPrepared.csv')
GDPPop7thFuturePrepared = pd.read_csv(r'Demand Models\Industry\data\modified\GDPPop7thFuturePrepared.csv')

# get list of economies and create economy-model pairs
economies = SteelHistoricalPrepared.Economy.unique()
models = {economy: LinearRegression() for economy in economies}

# set Economy as index and set target vector by dropping all other columns except lnGDPpercap and lnConspercap
df1 = (SteelHistoricalPrepared.set_index('Economy')
                                 .drop(['GDP','SteelConsumption','Population','GDPpercap','Conspercap'], axis=1))

# run regression
SteelRegressionModel = run_regression(models, economies, df1)

# make predictions using historical values of GDP per capita
HistoricalYears = SteelHistoricalPrepared[['Economy','Year']]
HistoricallnGDPpercap = (SteelHistoricalPrepared.set_index('Economy')
                                 .drop(['GDP','SteelConsumption','Population','GDPpercap','Conspercap','lnConspercap'], axis=1))
HistoricalPredictionResults = run_prediction(SteelRegressionModel, economies, HistoricalYears, HistoricallnGDPpercap)
HistoricalPredictionResults.reset_index(drop=True).sort_values('Economy')

# make predictions using future values of GDP per capita
FutureYears = GDPPop7thFuturePrepared[['Economy','Year']]
FuturelnGDPpercap = (GDPPop7thFuturePrepared.set_index('Economy')
                                                   .drop(['GDP','Population','GDPpercap'], axis=1))     
FutureProjectionResults = run_prediction(SteelRegressionModel, economies, FutureYears, FuturelnGDPpercap)
FutureProjectionResults.reset_index(drop=True).sort_values('Economy')

# plot historical and future predictions
plot_results(economies, HistoricalPredictionResults, FutureProjectionResults)

# combine results
SteelResultsCombined = pd.concat([HistoricalPredictionResults,FutureProjectionResults])

# write results to csv
HistoricalPredictionResults.to_csv(r'Demand Models\Industry\data\results\HistoricalPredictionResults.csv', index=False)
FutureProjectionResults.to_csv(r'Demand Models\Industry\data\results\FutureProjectionResults.csv', index=False)
SteelResultsCombined.to_csv(r'Demand Models\Industry\data\results\SteelResultsCombined.csv', index=False)

