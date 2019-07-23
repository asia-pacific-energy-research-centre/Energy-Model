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
year_list = list(range(1990,2051,1))

# use melt to collapse the year columns in to a new column and rename columns
Pop7th = pd.melt(rawPop7th, id_vars='Economy', value_vars=year_list)
Pop7th.rename(columns={'variable':'Year','value':'Population'}, inplace=True)

GDP7th = pd.melt(rawGDP7th, id_vars='Economy', value_vars=year_list)
GDP7th.rename(columns={'variable':'Year','value':'GDP'}, inplace=True)

# remove World Economy data

Pop7th.dropna(inplace=True)
GDP7th.dropna(inplace=True)

# separate historical and future
# store all values up up to, and including, 2016 in one dataframe
GDP7thHistorical = GDP7th[GDP7th.Year <= 2016].reset_index(drop=True)
GDP7thFuture = GDP7th[GDP7th.Year > 2016].reset_index(drop=True)
Pop7thHistorical = Pop7th[Pop7th.Year <= 2016].reset_index(drop=True)
Pop7thFuture = Pop7th[Pop7th.Year > 2016].reset_index(drop=True)

# write all dataframes to csv
Pop7thHistorical.to_csv(r'data\results\Pop7thHistorical.csv', index=False)
Pop7thFuture.to_csv(r'data\results\Pop7thFuture.csv', index=False)
GDP7thHistorical.to_csv(r'data\results\GDP7thHistorical.csv', index=False)
GDP7thFuture.to_csv(r'data\results\GDP7thFuture.csv', index=False)