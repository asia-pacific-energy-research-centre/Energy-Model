# plotEGEDA.py
# Plot data from EGEDA dataset
# To use, replace the Product Code with one of interest.
# Example used '07. Total Primary Energy Supply'

# import libraries
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import datetime as dt
import os
import sys
import subprocess

# import regression functions from RegressionFunctions.py
sys.path.insert(0, 'code')
from CommonFunctions import run_regression, run_prediction, plot2

# check that data file exists
PATH='data\processed\TidyEGEDA.csv'
if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
    print("Using TidyEGEDA.csv")
else:
    print ("Creating TidyEGEDA.csv")
    ## run CleanEGEDAdata.py
    run = 'python code\CleanEGEDAdata.py'
    subprocess.run(run, shell=False)

print("\nScript started. -- Current date/time:", dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# import EGEDA dataset
dfResults = pd.read_csv(r'data\processed\TidyEGEDA.csv')
economies = dfResults['Economy'].unique()

# select a column to plot
df = dfResults[['Economy','Year','Fuel Code','07. Total Primary Energy Supply']]
df = df[df['07. Total Primary Energy Supply']>0].dropna()

# select fuel codes
df = df[df['Fuel Code'].isin(['Coal', 'Oil', 'PetP','Gas','RenH','Nuc','RenNRE','Oth','Heat','TotRen'])]

# pivot to make fuels as columns because matplotlib will plot each column as a variable
df = pd.pivot_table(df, values='07. Total Primary Energy Supply', index=['Economy', 'Year'], columns=['Fuel Code'], aggfunc=np.sum)
df.reset_index(level=['Economy','Year'], inplace=True)

# Plot
# Change sharex and sharey to True or False
figurename = 'reports\TPES.png'
Plotylabel = 'TPES [MTOE]'
sharex = True
sharey = True
plot2(economies, df, figurename, Plotylabel, sharex, sharey)
