# createdatasets.py
# join together GDP, population, and production

# import math and data table functions
import numpy as np
import pandas as pd

# read data from csv and store as dataframe
TidySteel = pd.read_csv(r'data\modified\TidySteel.csv')
GDP7thHistorical = pd.read_csv(r'C:\GitHub\Energy-Model\SharedData\GDP7thHistorical.csv')
Pop7thHistorical = pd.read_csv(r'C:\GitHub\Energy-Model\SharedData\Pop7thHistorical.csv')

# combine datasets
SteelHistorical = pd.merge(GDP7thHistorical, TidySteel, how='left', on=['Economy','Year'])
SteelHistorical = pd.merge(SteelHistorical,Pop7thHistorical,how='left',on=['Economy','Year'])

# remove negative numbers and NaNs
SteelHistorical[SteelHistorical.SteelProduction < 0] = np.NaN
SteelHistorical.dropna(inplace=True)

# combine future GDP and population, drop the world value
GDP7thFuture = pd.read_csv(r'C:\GitHub\Energy-Model\SharedData\GDP7thFuture.csv')
Pop7thFuture = pd.read_csv(r'C:\GitHub\Energy-Model\SharedData\Pop7thFuture.csv')

GDPPop7thFuture = pd.merge(GDP7thFuture,Pop7thFuture,how='left',on=['Economy','Year']).dropna()

# save dataframes to csv
SteelHistorical.to_csv(r'data\modified\SteelHistorical.csv', index=False)
GDPPop7thFuture.to_csv(r'data\modified\GDPPop7thFuture.csv', index=False)