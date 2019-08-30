# MakeTidy.py
# take raw population and GDP from the 7th and reshape as Tidy
# save Tidy data in results folder

# import numpy for math and pandas for tables
import numpy as numpy
import pandas as pd
import os
import datetime as dt

print("\nScript started. -- Current date/time:", dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# create directories for modified and results data
paths = {'path1':'data\modified','path2':'data\modified','path3':'data\processed', 'path4':'results'}
for key, value in paths.items(): 
        try:
            os.makedirs(value)
        except OSError:
            print ("Directory %s exists." % value)
        else:
            print ("Successfully created the directory %s " % value)

# import from Excel
print('\nImporting population and GDP data from the 7th Edition...')
rawPop7th = pd.read_excel(r'data\raw\Macro\Population_7th_2019_07_02 - raw.xlsx')
rawGDP7th = pd.read_excel(r'data\raw\Macro\GDP_7th_2019_07_02 - raw.xlsx')

# define list of years
year_list = list(range(1990,2051,1))

Pop7th = rawPop7th.set_index('Economy').stack().reset_index(name='Population')
Pop7th.rename(columns={'level_1':'Year'}, inplace=True)

GDP7th = rawGDP7th.set_index('Economy').stack().reset_index(name='GDP')
GDP7th.rename(columns={'level_1':'Year'}, inplace=True)

# use melt to collapse the year columns in to a new column and rename columns
print('\nBegin cleaning...')
#Pop7th = pd.melt(rawPop7th, id_vars='Economy', value_vars=year_list)
#Pop7th.rename(columns={'variable':'Year','value':'Population'}, inplace=True)

#GDP7th = pd.melt(rawGDP7th, id_vars='Economy', value_vars=year_list)
#GDP7th.rename(columns={'variable':'Year','value':'GDP'}, inplace=True)

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
Pop7thHistorical.to_csv(r'data\processed\Pop7thHistorical.csv', index=False)
Pop7thFuture.to_csv(r'data\processed\Pop7thFuture.csv', index=False)
GDP7thHistorical.to_csv(r'data\processed\GDP7thHistorical.csv', index=False)
GDP7thFuture.to_csv(r'data\processed\GDP7thFuture.csv', index=False)

# Finished
print("\nFINISHED. -- Current date/time:", dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print('\nCleaned data saved in the folder %s' %paths['path3'])