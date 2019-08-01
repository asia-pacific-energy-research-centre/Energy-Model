# regression functions

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
        # i had problem with merging. There might be an actual issue here. Worth checking.
        df_merged = pd.merge(dfResults,df_years, how='left', left_index=True, right_index=True)
        df_merged = df_merged.drop('Economy_y', axis=1)

        # reorder columns
        df_merged = df_merged[['Economy_x','Year','Predicted Steel Consumption']].reset_index(drop=True)
        df_merged.rename(columns={'Economy_x':'Economy'}, inplace=True)
        return df_merged

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