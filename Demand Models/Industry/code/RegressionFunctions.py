# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# define functions to perform regressions and predictions, and to plot results
# loop over economy-model pairs to fit regression
def run_regression(models, economies, df, x, y):
        for economy, model in models.items():
                (model.fit(df.loc[economy, x],
                    df.loc[economy, y]))
        return models            

# create function for performing prediction and writing results
# loop over economy-model pairs to make prediction and write prediction to csv, one for each economy
def run_prediction(models, economies, df, ResultsColumn):
        df_list =[]
        # run predictions
        for economy, model in models.items():
                prediction = model.predict(df.loc[economy,:])
                df_name = pd.DataFrame(np.exp(prediction), columns=ResultsColumn)
                df_name['Economy'] = economy
                df_list.append(df_name)
        
        # combine individual economy dataframes to one dataframe
        dfResults = pd.concat(df_list, sort=True).reset_index(drop=True)

        # add year column
        df_years = df.reset_index().sort_values(by=['Economy','Year']).reset_index(drop=True).drop(['lnGDPpercap'], axis=1)
        # i had problem with merging. There might be an actual issue here. Worth checking.
        df_merged = pd.merge(dfResults,df_years, how='left', left_index=True, right_index=True)
        df_merged = df_merged.drop('Economy_y', axis=1)

        # rename columns
        #df_merged = df_merged[['Economy_x','Year']].reset_index(drop=True)
        df_merged.rename(columns={'Economy_x':'Economy'}, inplace=True)
        return df_merged

# define function to plot using matplotlib
def plot_results(economies, df1, df2, figurename, PlotColumns, Plotylabel):
    fig = plt.figure(figsize=[16,12])
    plt.style.use('tableau-colorblind10')    
    for economy,num in zip(economies, range(1,22)):
        print('Creating plot for %s...' %economy)
        df11=df1[df1['Economy']==economy]
        df21=df2[df2['Economy']==economy]
        ax = fig.add_subplot(3,7,num)
        ax.plot(df11['Year'], df11[PlotColumns])
        ax.plot(df21['Year'], df21[PlotColumns])
        ax.set_title(economy)
        
        plt.xlim(1980,2050)
        plt.ylim(0,1000000)  
        
        # add y-axis label
        plt.ylabel(Plotylabel)    
        
        # add tight layout function
        plt.tight_layout()
    # show graphic
    plt.show()
    fig.savefig(figurename,dpi=200)
    print('Figure saved as %s' % figurename)

def plot2(economies, df, figurename, Plotylabel):
    
    # Create the 'figure'
    plt.style.use('tableau-colorblind10')
    
    # multiple line plot
    fig, axes = plt.subplots(nrows=3, ncols=7, sharex=False, sharey=False, figsize=(16,12))
    for ax, economy,num in zip(axes.flatten(), economies, range(1,22)):
        print('Creating plot for %s...' %economy)
        df11=df[df['Economy']==economy]
    
        for column in df11.drop(['Economy','Year'], axis=1):
            ax.plot(df11['Year'], df11[column], marker='', linewidth=1.5, label=economy)
            ax.set_title(economy)
            ax.set_ylabel(Plotylabel)
        # Same limits for everybody!
        ax.set_ylim(0,1000000)   
        ax.label_outer()
    
    #plt.tight_layout()
    fig.legend( list(df.drop(['Economy','Year'], axis=1)), bbox_to_anchor=(0,0,1,0.25), loc='lower center', ncol=9)
    fig.savefig(figurename,dpi=200)
    print('Figure saved as %s' % figurename)
    print('Preparing to show the figure...')
    plt.show()


