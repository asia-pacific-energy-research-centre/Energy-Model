# ComputeFeatures.py
# compute per capita and natural logs for regression

# import math and table functions
import pandas as pd
import numpy as np 

# read datasets from csv
SteelHistorical = pd.read_csv(r'data\modified\SteelHistorical.csv')
GDPPop7thFuture = pd.read_csv(r'data\modified\GDPPop7thFuture.csv')

# compute per capita then take natural logs
SteelHistorical['GDPpercap'] = SteelHistorical['GDP'].div(SteelHistorical['Population'])
SteelHistorical['Prodpercap'] = SteelHistorical['SteelProduction'].div(SteelHistorical['Population'])

SteelHistorical['lnGDPpercap'] = np.log(SteelHistorical['GDPpercap'])
SteelHistorical['lnProdpercap'] = np.log(SteelHistorical['Prodpercap'])

GDPPop7thFuture['GDPpercap'] = GDPPop7thFuture['GDP'].div(GDPPop7thFuture['Population'])
GDPPop7thFuture['lnGDPpercap'] = np.log(GDPPop7thFuture['GDPpercap'])

# write prepared data to csv
SteelHistorical.to_csv(r'data\modified\SteelHistoricalPrepared.csv', index=False)   
GDPPop7thFuture.to_csv(r'data\modified\GDPPop7thFuturePrepared.csv', index=False)