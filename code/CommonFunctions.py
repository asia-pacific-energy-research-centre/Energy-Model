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
                years = df['Year']
                years.reset_index(drop=True, inplace=True)
                prediction = model.predict(df.loc[economy,:])
                df_name = pd.DataFrame(np.exp(prediction), columns=ResultsColumn)
                df_name.insert(loc=0,column='Year',value=years)
                df_name.insert(loc=0,column='Economy',value=economy)
                df_list.append(df_name)

        # combine individual economy dataframes to one dataframe
        dfResults = pd.concat(df_list, sort=True)
        return dfResults

def plot2(economies, df, figurename, Plotylabel):
    
    # Create the 'figure'
    plt.style.use('tableau-colorblind10')
    
    # multiple line plot
    fig, axes = plt.subplots(nrows=3, ncols=7, sharex=True, sharey=False, figsize=(16,12))
    for ax, economy,num in zip(axes.flatten(), economies, range(1,22)):
        print('Creating plot for %s...' %economy)
        df11=df[df['Economy']==economy]
    
        for column in df11.drop(['Economy','Year'], axis=1):
            ax.plot(df11['Year'], df11[column], marker='', linewidth=1.5, label=economy)
            ax.set_title(economy)
            ax.set_ylabel(Plotylabel)
        ax.label_outer()
    
    #plt.tight_layout()
    fig.legend( list(df.drop(['Economy','Year'], axis=1)), bbox_to_anchor=(0,0,1,0.25), loc='lower center', ncol=9)
    fig.savefig(figurename,dpi=200)
    print('Figure saved as %s' % figurename)
    print('Preparing to show the figure...')
    plt.show()

def cagr(start_value, end_value, num_periods):
    return (end_value / start_value) ** (1 / (num_periods - 1)) - 1

def calcCAGR(df,economies):
    df_list = []
    for economy in economies.flatten():
        df11 = df[df['Economy']==economy]
        for col in df11.drop(['Economy','Year'], axis=1):        
            start_value = float(df11[col].iloc[0])
            end_value = float(df11[col].iloc[-1])
            num_periods = len(df11[col])
            cagr_result = cagr(start_value, end_value, num_periods)
            df_list.append((economy,col,cagr_result))
    df = pd.DataFrame(df_list, columns=['A','B','C'])
    return df

def calcYOY(df,economies):
    df_list = []
    for economy in economies.flatten():
        df11 = df.loc[economy]
        yoy = df11.pct_change()
        yoy.reset_index(inplace=True)
        yoy.insert(loc=0,column='Economy',value=economy)
        df_list.append(yoy)
    dfPC = pd.concat(df_list)
    return dfPC
