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
Plotylabel = 'TPES [MTOE]'
dfResults = pd.read_csv(r'EGEDA\results\TidyEGEDA.csv')
economies = dfResults['Economy'].unique()

# select what to plot
# select a column
df = dfResults[['Economy','Year','Fuel Code','07. Total Primary Energy Supply']]
df = df[df['07. Total Primary Energy Supply']>0].dropna()
# select fuel codes
df = df[df['Fuel Code'].isin(['Coal', 'Oil', 'PetP','Gas','RenH','Nuc','RenNRE','Oth','Heat','TotRen'])]

# pivot to make fuels as columns because matplotlib will plot each column as a variable
df = pd.pivot_table(df, values='07. Total Primary Energy Supply', index=['Economy', 'Year'], columns=['Fuel Code'], aggfunc=np.sum)
df.reset_index(level=['Economy','Year'], inplace=True)

# Plot

# Create the 'figure'
plt.style.use('tableau-colorblind10')

# multiple line plot
fig, axes = plt.subplots(nrows=3, ncols=7, sharex=False, sharey=True, figsize=(16,12))
for ax, economy,num in zip(axes.flatten(), economies, range(1,22)):
    print('Creating plot for %s...' %economy)
    df11=df[df['Economy']==economy]

    for column in df11.drop(['Economy','Year'], axis=1):
        ax.plot(df11['Year'], df11[column])
        ax.set_title(economy)
        ax.set_ylabel(Plotylabel)
    # Same limits for everybody!
    #ax.set_ylim(0,2500000)   
    #ax.label_outer()

# place legend outside of plots
fig.legend( list(df.drop(['Economy','Year'], axis=1)), bbox_to_anchor=(0,0,1,0.25), loc='lower center', ncol=9)
#plt.tight_layout()    # tight_layout does not work with bbox_to_anchor
fig.savefig(figurename,dpi=200)
print('Figure saved as %s' % figurename)
print('Preparing to show the figure...')
plt.show()
print("\nFINISHED. -- Current date/time:", dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))