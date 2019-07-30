# MakeTidy.py
# Take Steel subsector production data from the 7th and reshape in Tidy format
# https://stackoverflow.com/questions/45066873/pandas-melt-with-multiple-value-vars

# import math and data table functions
import numpy as np
import pandas as pd
from functools import reduce

RawPowerDataAsia = pd.read_csv(r'Power Model\data\MI_WorldElectricPowerPlants_Asia_March2019_v1.csv')
RawPowerDataNAmerica = pd.read_csv(r'Power Model\data\MI_WorldElectricPowerPlants_NorthAmerica_March2019_v1.csv')
RawPowerDataOther = pd.read_csv(r'Power Model\data\MI_WorldElectricPowerPlants_Other_March2019_v1.csv')
RawPowerData.head()

# Merge all three Platts database that are based on three world regions into one file
CombinedPowerData = pd.concat ([RawPowerDataAsia, RawPowerDataNAmerica, RawPowerDataOther])

# Delete some data from Platts that are not required for the electricity outlook study
newdata = CombinedPowerData.drop(['UNIT','PLANT'],axis=1)






# using melt to make a tidy set with multiple measured variables - see Table 12 in Tidy Data paper
TidySteel = pd.melt(RawSteelData, id_vars=['Economy'], var_name='Year')
TidySteel.rename(columns={'value':'SteelProduction'}, inplace=True)

# write to csv
TidySteel.to_csv(r'data\modified\TidySteel.csv', index=False)