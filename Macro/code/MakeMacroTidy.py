# MakeTidy.py
# take raw population and GDP from the 7th and reshape as Tidy
# save Tidy data in results folder

# import numpy for math and pandas for tables
import numpy as numpy
import pandas as pd
import os

# create directories for modified and results data
paths = {'path1':'Macro/data/modified','path2':'Macro/data/results'}
for key, value in paths.items(): 
        try:
            os.makedirs(value)
        except OSError:
            print ("%s already exists. It's OK." % value)
        else:
            print ("Successfully created the directory %s " % value)

# import from Excel
rawPop7th = pd.read_excel(r'Macro\data\raw\Population_7th_2019_07_02 - raw.xlsx')
rawGDP7th = pd.read_excel(r'Macro\data\raw\GDP_7th_2019_07_02 - raw.xlsx')

# define list of years
year_list = list(range(1990,2051,1))

# use melt to collapse the year columns in to a new column and rename columns
Pop7th = pd.melt(rawPop7th, id_vars='Economy', value_vars=year_list)
Pop7th.rename(columns={'variable':'Year','value':'Population'}, inplace=True)

GDP7th = pd.melt(rawGDP7th, id_vars='Economy', value_vars=year_list)
GDP7th.rename(columns={'variable':'Year','value':'GDP'}, inplace=True)

# replace economies using APEC approved abbreviations
EconomyNames = {
    '01_AUS':'AUS',
    '02_BD':'BD',
    '03_CDA':'CDA',
    '04_CHL':'CHL',
    '05_PRC':'PRC',
    '06_HKC':'HKC',
    '07_INA':'INA',
    '08_JPN':'JPN',
    '09_ROK':'KOR',
    '10_MAS':'MAS',
    '11_MEX':'MEX',
    '12_NZ':'NZ',
    '13_PNG':'PNG',
    '14_PE':'PE',
    '15_RP':'RP',
    '16_RUS':'RUS',
    '17_SIN':'SIN',
    '18_CT':'CT',
    '19_THA':'THA',
    '20_USA':'USA',
    '21_VN':'VN'}

GDP7th.replace(EconomyNames, inplace=True)
Pop7th.replace(EconomyNames, inplace=True)

# remove World Economy data
Pop7th.dropna(inplace=True)
GDP7th.dropna(inplace=True)

GDP7th.drop(GDP7th[GDP7th['Economy']=='27_WOR'].index, inplace=True)
Pop7th.drop(Pop7th[Pop7th['Economy']=='27_WOR'].index, inplace=True)


# separate historical and future
# store all values up up to, and including, 2016 in one dataframe
GDP7thHistorical = GDP7th[GDP7th.Year <= 2016].reset_index(drop=True)
GDP7thFuture = GDP7th[GDP7th.Year > 2016].reset_index(drop=True)
Pop7thHistorical = Pop7th[Pop7th.Year <= 2016].reset_index(drop=True)
Pop7thFuture = Pop7th[Pop7th.Year > 2016].reset_index(drop=True)

# write all dataframes to csv
Pop7thHistorical.to_csv(r'Macro\data\results\Pop7thHistorical.csv', index=False)
Pop7thFuture.to_csv(r'Macro\data\results\Pop7thFuture.csv', index=False)
GDP7thHistorical.to_csv(r'Macro\data\results\GDP7thHistorical.csv', index=False)
GDP7thFuture.to_csv(r'Macro\data\results\GDP7thFuture.csv', index=False)