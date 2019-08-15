import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import datetime as dt
import os
import subprocess

# check that data file exists
PATH='EGEDA/results/TidyEGEDA.csv'
if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
    print("Using TidyEGEDA.csv")
else:
    print ("Creating TidyEGEDA.csv")
    ## run CleanEGEDAdata.py
    run = 'python EGEDA\code\CleanEGEDAdata.py'
    subprocess.run(run, shell=False)

print("\nScript started. -- Current date/time:", dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# choose where to save the final image file
figurename = 'TPES'

dfResults = pd.read_csv(r'EGEDA\results\TidyEGEDA.csv')
economies = dfResults.Economy.unique()
#economies = ['CT','VN']

dfPlot = dfResults[['Economy','Year','Fuel Code','07. Total Primary Energy Supply']]
dfPlot = dfPlot[dfPlot['07. Total Primary Energy Supply']>0].dropna()
table = pd.pivot_table(dfPlot, values='07. Total Primary Energy Supply', index=['Economy', 'Year'], columns=['Fuel Code'], aggfunc=np.sum)
table.reset_index(level=['Economy','Year'], inplace=True)
table.drop(columns=['Tot'], inplace=True)

# Initialize the figure
plt.style.use('tableau-colorblind10')

# multiple line plot
fig = plt.figure(figsize=[16,12])
for economy,num in zip(economies, range(1,22)):
    print('Creating plot for %s...' %economy)
    ax = fig.add_subplot(3,7,num)
    df11=table[table['Economy']==economy]
    # plot 
    for column in df11.drop(['Economy','Year'], axis=1):
        plt.plot(df11['Year'], df11[column], marker='', linewidth=1.5)
        ax.set_title(economy)
        plt.ylabel('TPES [MTOE]')
        plt.sharey=True
        plt.tight_layout()
    
# Same limits for everybody!
    plt.xlim(1980,2016)
    plt.ylim(0,250000)
fig.legend( list(df11.drop(['Economy','Year'], axis=1)),  loc='bottom right', ncol=5 )

#plt.legend(list(df11), loc=4, frameon=False)
plt.show()
fig.savefig(figurename,dpi=200)
print('Figure saved as %s' % figurename)
print("\nFINISHED. -- Current date/time:", dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
