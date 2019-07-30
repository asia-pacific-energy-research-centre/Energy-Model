# MakeTidy.py
# Take Steel subsector consumption data from the 7th and reshape in Tidy format
# https://stackoverflow.com/questions/45066873/pandas-melt-with-multiple-value-vars

# import math and data table functions
import numpy as np
import pandas as pd

RawSteelData = pd.read_csv(r'Demand Models\Industry\data\raw\IS_consumption7th.csv')
RawSteelData.head()

# using melt to make a tidy set with multiple measured variables - see Table 12 in Tidy Data paper
TidySteel = pd.melt(RawSteelData, id_vars=['Economy'], var_name='Year')
TidySteel.rename(columns={'value':'SteelConsumption'}, inplace=True)

# write to csv
TidySteel.to_csv(r'Demand Models\Industry\data\modified\TidySteel.csv', index=False)