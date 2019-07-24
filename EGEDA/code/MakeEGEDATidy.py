# MakeTidy.py
# Take EGEDA 2016 data and reshape in Tidy format
# https://stackoverflow.com/questions/45066873/pandas-melt-with-multiple-value-vars

# raw data file = APEC21_22Jul2019B_raw.xlsx
# manual adjustments made to the raw data file before the following code:
# - renamed 'MYS' to 'MAS'
# - removed column labels for columns A,B,C,D
# - removed summary rows at bottom of each sheet
# - removed miscellaneous calculations in row AP

# to use file, open code editor to the EGEDA folder (so file paths will be correct)

#### Begin data manipulation ####

# import math and data table functions
import numpy as np
import pandas as pd

# read all sheets from EGEDA spreadsheet to Pandas dictionary
# Pandas dictionary contains a key for each economy, and the value is a dataframe with the table data
RawEGEDA = pd.read_excel(r'data\modified\APEC21_22Jul2019B_ready.xlsx', sheet_name=None)

# define year range
years = list(range(1980,2016,1))

# create empty list to store each dataframe
df_list =[]
for sheet, dataframe in RawEGEDA.items():
        # rename blank columns
        RawEGEDA[sheet].rename(columns={'Unnamed: 0':'Product Number','Unnamed: 1':'Item Number', 'Unnamed: 2':'Product Code','Unnamed: 3':'Item Code'}, inplace=True)
        
        # Make Item Code Columns
        df_name = (RawEGEDA[sheet].set_index(['Product Number','Item Number', 'Product Code', 'Item Code'])
                  .rename_axis(['Year'], axis=1)
                  .stack().unstack('Item Code')
                  .reset_index())
 
        # create column with economy name
        df_name['Economy'] = sheet

        df_list.append(df_name)

# combine individual economy dataframes to one dataframe
dfResults = pd.concat(df_list).reset_index(drop=True)

# remove x and X placeholders with NaNs
# code..
# code..

# replace economy names
# rename economies
economy_names = {'AUS':'01_AUS','BRN':'02_BD','CAN':'03_CDA','CHL':'04_CHL','CHN':'05_PRC',
        'HKG':'06_HKC','IDN':'07_INA','JPN':'08_JPN','KOR':'09_KOR','MAS':'10_MAS', 'MEX':'11_MEX',
        'NZL':'12_NZ','PNG':'13_PNG','PER':'14_PE','PHL':'15_RP','RUS':'16_RUS','SGP':'17_SIN',
        'CT':'18_CT','THA':'19_THA','USA':'20_USA','VNM':'21_VN'}
# code to replace..

# add column to store APERC codes
dfResults['APERC'] = np.NaN

# create dictionary of Product Code and APERC code
#APERC_codes = {
#        '02. Coal Products':'CoalP',
#        '03. Crude Oil & NGL':'OilP'
#        }

#dfResults.replace(APERC_codes, inplace=True)

# write to csv
dfResults.to_csv(r'data\modified\TidyEGEDA.csv', index=False)


