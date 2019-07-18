# MakeTidy.py
# take raw population and GDP from the 7th and reshape as Tidy
# save Tidy data in results folder

# import numpy for math and pandas for tables
import numpy as numpy
import pandas as pd

# import from Excel
rawPop7th = pd.read_excel(r'data\raw\Population_7th_2019_07_02 - raw.xlsx')
rawGDP7th = pd.read_excel(r'data\raw\GDP_7th_2019_07_02 - raw.xlsx')

# define list of years
year_list = list(range(1990,2050,1))

# use melt to collapse the year columns in to a new column and rename columns
Pop7th = pd.melt(rawPop7th, id_vars='Economy', value_vars=year_list)
Pop7th.rename(columns={'variable':'Year','value':'Population'}, inplace=True)

GDP7th = pd.melt(rawGDP7th, id_vars='Economy', value_vars=year_list)
GDP7th.rename(columns={'variable':'Year','value':'Population'}, inplace=True)

# write to csv
Pop7th.to_csv(r'data\results\Pop7th.csv', index=False)
GDP7th.to_csv(r'data\results\GDP7th.csv', index=False)