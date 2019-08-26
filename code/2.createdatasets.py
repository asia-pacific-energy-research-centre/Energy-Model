# createdatasets.py
# join together GDP, population, and consumption

# import math and data table functions
import numpy as np
import pandas as pd
import datetime as dt
import subprocess

print("Script started. -- Current date/time:", dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

## run Macro script to create Macro data
runMacro = 'python Macro\code\MakeMacroTidy.py'
subprocess.run(runMacro, shell=False)

# read data from csv and store as dataframe
TidySteel = pd.read_csv(r'Demand Models\Industry\data\modified\TidySteel.csv')
GDP7thHistorical = pd.read_csv(r'Macro\data\results\GDP7thHistorical.csv')
Pop7thHistorical = pd.read_csv(r'Macro\data\results\Pop7thHistorical.csv')

# combine datasets
SteelHistorical = pd.merge(GDP7thHistorical, TidySteel, how='left', on=['Economy','Year'])
SteelHistorical = pd.merge(SteelHistorical,Pop7thHistorical,how='left',on=['Economy','Year'])

# Replace negative numbers with NaN
# Instead of dropping NaN, 'impute' the values by using mean, median, min, etc
# this replaces the NaN for BD, PNG, and RUS with min values across all economies
# Note that the BD, PNG values are too high - need to impute by economy
SteelHistorical.loc[SteelHistorical['SteelConsumption'] < 0,'SteelConsumption'] = np.NaN
#SteelHistorical.fillna(SteelHistorical[['SteelConsumption']].mean(), inplace=True)

i = SteelHistorical[['SteelConsumption']].min()
SteelHistorical.loc[SteelHistorical['Economy'].isin(['BD','PNG'])] = SteelHistorical.loc[SteelHistorical['Economy'].isin(['BD','PNG'])].fillna(i)
j = SteelHistorical.loc[SteelHistorical['Economy']=='RUS','SteelConsumption'].mean()
SteelHistorical.loc[SteelHistorical['Economy'].isin(['RUS'])] = SteelHistorical.loc[SteelHistorical['Economy'].isin(['RUS'])].fillna(j)

# combine future GDP and population, drop the world value
GDP7thFuture = pd.read_csv(r'Macro\data\results\GDP7thFuture.csv')
Pop7thFuture = pd.read_csv(r'Macro\data\results\Pop7thFuture.csv')

GDPPop7thFuture = pd.merge(GDP7thFuture,Pop7thFuture,how='left',on=['Economy','Year']).reset_index(drop=True)

# save dataframes to csv
SteelHistorical.to_csv(r'Demand Models\Industry\data\modified\SteelHistorical.csv', index=False)
GDPPop7thFuture.to_csv(r'Demand Models\Industry\data\modified\GDPPop7thFuture.csv', index=False)

print("Results are saved. -- Current date/time:", dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))