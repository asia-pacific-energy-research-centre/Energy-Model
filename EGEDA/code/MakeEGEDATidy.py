# MakeTidy.py
# Take EGEDA 2016 data and reshape in Tidy format
# https://stackoverflow.com/questions/45066873/pandas-melt-with-multiple-value-vars

# import math and data table functions
import numpy as np
import pandas as pd

# read in EGEDA file in to a dictionary. All sheets are read in.
# note Canada is missing years 1980-2003. Filled in manually to 0.
RawEGEDA = pd.read_excel(r'data\raw\EGEDA_2019.06_AK.xlsx', sheet_name=None)

# define year range
years = list(range(1970,2016,1))

# rename economies
economy_names = {'APEC21':'APEC','AUS':'01_AUS',
                 'BRN':'02_BD','CAN':'03_CDA','CHL':'04_CHL',
                 'CHN':'05_PRC','HKG':'06_HKC',
                 'IDN':'07_INA','JPN':'08_JPN',
                 'KOR':'09_KOR','MAS':'10_MAS',
                 'MEX':'11_MEX','NZL':'12_NZ',
                 'PNG':'13_PNG','PER':'14_PE',
                 'PHL':'15_RP','RUS':'16_RUS',
                 'SGP':'17_SIN','CT':'18_CT',
                 'THA':'19_THA','USA':'20_USA','VNM':'21_VN'}

#RawEGEDA.rename(columns=economy_names, inplace=True)

df_list =[]
for sheet, dataframe in RawEGEDA.items():
        RawEGEDA[sheet].rename(columns={'Unnamed: 2':'Product Code', 'Unnamed: 3':'Item Code'}, inplace=True)
        # using melt to make a tidy set with multiple measured variables - see Table 12 in Tidy Data paper
        df_name = pd.melt(RawEGEDA[sheet],id_vars=['Product No.','item No.','Product Code','Item Code'],value_vars=years)
        df_name.rename(columns={'variable':'Year','value':'Energy'}, inplace=True)
        df_name['Economy'] = sheet
        df_list.append(df_name)
        #df_name.to_csv(r'data\modified\%s.csv' %sheet, index=False)
        print('I am on economy %s' %sheet)
dfResults = pd.concat(df_list).reset_index(drop=True)
#dfResults.replace(economy_names, inplace=True)

dfResults[dfResults['Economy'] == 'THA']
# write to csv
dfResults.to_csv(r'data\modified\TidyEGEDA.csv', index=False)