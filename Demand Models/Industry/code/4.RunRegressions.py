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
def run_prediction(models, economies, df):
        df_list =[]
        # run predictions
        for economy, model in models.items():
                prediction = model.predict(df.loc[economy,:])
                df_name = pd.DataFrame(np.exp(prediction), columns=['Predicted Steel Consumption'])
                df_name['Economy'] = economy
                df_list.append(df_name)
        
        # combine individual economy dataframes to one dataframe
        dfResults = pd.concat(df_list, sort=True).reset_index(drop=True)

        # add year column
        df_years = df.reset_index().sort_values(by=['Economy','Year']).reset_index(drop=True).drop(['lnGDPpercap'], axis=1)
        df_merged = pd.merge(dfResults,df_years, how='left', left_index=True, right_index=True)
        df_merged = df_merged.drop('Economy_y', axis=1)

        # reorder columns
        df_merged = df_merged[['Economy_x','Year','Predicted Steel Consumption']].reset_index(drop=True)
        df_merged.rename(columns={'Economy_x':'Economy'}, inplace=True)
        return df_merged

# make predictions using historical values of GDP per capita
#df3 = df1[['Year','lnGDPpercap']]
df3 = df1.drop('lnConspercap', axis=1)
HistoricalPredictionResults = run_prediction(SteelRegressionModel, economies, df3)

# define function to plot using matplotlib
def plot_results(economies, df1, df2):
        fig = plt.figure(figsize=[8,16])

        for economy,num in zip(economies, range(1,20)):
                df11=df1[df1['Economy']==economy]
                df21=df2[df2['Economy']==economy]
                ax = fig.add_subplot(7,3,num)
                ax.plot(df11['Year'], df11[['Predicted Steel Consumption']],'r')
                ax.plot(df21['Year'], df21[['Predicted Steel Consumption']],'b')
                ax.set_title(economy)

                #plt.tight_layout()
        plt.show()
##################################
# end of functions
##################################

# Perform regressions
# read in data from csv
SteelHistoricalPrepared = pd.read_csv(r'Demand Models\Industry\data\modified\SteelHistoricalPrepared.csv').sort_values(by=['Economy','Year']).reset_index(drop=True)
GDPPop7thFuturePrepared = pd.read_csv(r'Demand Models\Industry\data\modified\GDPPop7thFuturePrepared.csv').sort_values(by=['Economy','Year']).reset_index(drop=True)

# get list of economies and create economy-model pairs
economies = SteelHistoricalPrepared.Economy.unique()
models = {economy: LinearRegression() for economy in economies}

# set Economy as index and set target vector by dropping all other columns except lnGDPpercap and lnConspercap
df1 = (SteelHistoricalPrepared.set_index('Economy')
       .drop(['GDP','SteelConsumption','Population','GDPpercap','Conspercap'], axis=1))

# run regression
SteelRegressionModel = run_regression(models, economies, df1)

# make predictions using future values of GDP per capita
FuturelnGDPpercap = (GDPPop7thFuturePrepared.set_index('Economy')
                                                   .drop(['GDP','Population','GDPpercap'], axis=1))     

FutureProjectionResults = run_prediction(SteelRegressionModel, economies, FuturelnGDPpercap)
#FutureProjectionResults.reset_index(drop=True).sort_values('Economy')

# plot historical and future predictions
plot_results(economies, HistoricalPredictionResults, FutureProjectionResults)

# combine results
SteelResultsCombined = pd.concat([HistoricalPredictionResults,FutureProjectionResults])

# write results to csv
HistoricalPredictionResults.to_csv(r'Demand Models\Industry\data\results\HistoricalPredictionResults.csv', index=False)
FutureProjectionResults.to_csv(r'Demand Models\Industry\data\results\FutureProjectionResults.csv', index=False)
SteelResultsCombined.to_csv(r'Demand Models\Industry\data\results\SteelResultsCombined.csv', index=False)