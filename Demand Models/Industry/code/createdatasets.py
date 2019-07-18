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

