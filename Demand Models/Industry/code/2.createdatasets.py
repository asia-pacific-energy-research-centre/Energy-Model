# createdatasets.py
# join together GDP, population, and consumption

# import math and data table functions
import numpy as np
import pandas as pd
import sys
import datetime as dt

print("Script started. -- Current date/time:", dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# run Macro script to create Macro data
sys.path.insert(0, 'Macro/code')
import MakeMacroTidy

# read data from csv and store as dataframe
TidySteel = pd.read_csv(r'Demand Models\Industry\data\modified\TidySteel.csv')
GDP7thHistorical = pd.read_csv(r'Macro\data\results\GDP7thHistorical.csv')
Pop7thHistorical = pd.read_csv(r'Macro\data\results\Pop7thHistorical.csv')

# combine datasets
SteelHistorical = pd.merge(TidySteel, GDP7thHistorical, Pop7thHistorical, how='left', on=['Economy','Year'])
# SteelHistorical = pd.merge(SteelHistorical,Pop7thHistorical,how='left',on=['Economy','Year'])

# remove negative numbers and NaNs
SteelHistorical[SteelHistorical.SteelConsumption < 0] = np.NaN
SteelHistorical = SteelHistorical.sort_values(by=['Economy','Year']).reset_index(drop=True)
SteelHistorical = SteelHistorical.dropna().reset_index(drop=True)

# combine future GDP and population, drop the world value
GDP7thFuture = pd.read_csv(r'Macro\data\results\GDP7thFuture.csv')
Pop7thFuture = pd.read_csv(r'Macro\data\results\Pop7thFuture.csv')

GDPPop7thFuture = pd.merge(GDP7thFuture,Pop7thFuture,how='left',on=['Economy','Year']).dropna().sort_values(by=['Economy','Year']).reset_index(drop=True)

# save dataframes to csv
SteelHistorical.to_csv(r'Demand Models\Industry\data\modified\SteelHistorical.csv', index=False)
GDPPop7thFuture.to_csv(r'Demand Models\Industry\data\modified\GDPPop7thFuture.csv', index=False)

print("Results are saved. -- Current date/time:", dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))