# statsEGEDA.py
# Compute some useful statistics from EGEDA data

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
from CommonFunctions import run_regression, run_prediction, plot2, cagr, calcCAGR, calcYOY

# check that data file exists
PATH='data\processed\TidyEGEDA.csv'
if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
    print("Using TidyEGEDA.csv")
else:
    print ("Creating TidyEGEDA.csv")
    ## run CleanEGEDAdata.py
    run = 'python code\CleanEGEDAdata.py'
    subprocess.run(run, shell=False)


# CAGR
# choose dataframe and features
dfResults = pd.read_csv(r'data\processed\TidyEGEDA.csv')
df = dfResults[['Economy','Year','Fuel Code','01. Indigenous Production']]
df = pd.pivot_table(df, values='01. Indigenous Production', index=['Economy', 'Year'], columns=['Fuel Code'], aggfunc=np.sum)
df.reset_index(level=['Economy','Year'], inplace=True)
df.replace({0:np.NaN}, inplace=True)
economies = dfResults['Economy'].unique()

dfCAGR = calcCAGR(df,economies)
dfCAGR.rename({'A':'Economy','B':'Fuel Code','C':'CAGR'}, axis=1,inplace=True)
CAGR = dfCAGR.to_csv(r'data\processed\Production CAGR.csv', index=False)

# display in human readable layout
dfCAGR.set_index(['Economy','Fuel Code'], inplace=True, drop=True)
dfCAGR = dfCAGR.unstack(['Fuel Code']).reset_index()
dfCAGR.fillna(0, inplace=True)

# YOY percent change
# choose dataframe and features
dfResults = pd.read_csv(r'data\processed\TidyEGEDA.csv')
df = dfResults[['Economy','Year','Fuel Code','01. Indigenous Production']]
economies = dfResults['Economy'].unique()
df = pd.pivot_table(df, values='01. Indigenous Production', index=['Economy', 'Year'], columns=['Fuel Code'], aggfunc=np.sum)

dfYOY = calcYOY(df,economies)
dfYOY = dfYOY.to_csv(r'data\processed\Production YOY.csv', index=False)
