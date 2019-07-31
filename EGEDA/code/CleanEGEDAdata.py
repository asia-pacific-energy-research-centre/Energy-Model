# CleanEGEDAdata.py

# Take EGEDA 2016 data and reshape in Tidy format and clean
# https://stackoverflow.com/questions/45066873/pandas-melt-with-multiple-value-vars

# raw data file = APEC21_22Jul2019B_raw.xlsx
# manual adjustments made to the raw data file before the following code:
# - renamed 'MYS' to 'MAS'
# - removed column labels for columns A,B,C,D
# - removed summary rows at bottom of each sheet
# - removed miscellaneous calculations in row AP

#### Begin data manipulation ####

# import math and data table functions
import numpy as np
import pandas as pd
import os

# automatically create directories for modified and results data
# these are not tracked in GitHub (see .gitignore)
paths = {'path1':'EGEDA/data/results'}
for key, value in paths.items(): 
        try:
            os.makedirs(value)
        except OSError:
            print ("%s already exists. It's OK" % value)
        else:
            print ("Successfully created %s " % value)

# read all sheets from EGEDA spreadsheet to Pandas dictionary.
# `sheet_name = none` means the output will be a dictionary that contains a key for each economy, 
# and the value is a dataframe with the table data.
RawEGEDA = pd.read_excel(r'EGEDA\data\modified\APEC21_22Jul2019B_ready.xlsx', sheet_name=None)

# define year range
years = list(range(1980,2016,1))

# create empty list to store each dataframe
df_list =[]
for sheet, dataframe in RawEGEDA.items():
        # rename blank columns
        RawEGEDA[sheet].rename(columns={'Unnamed: 0':'Product Number','Unnamed: 1':'Item Number', 'Unnamed: 2':'Product Code','Unnamed: 3':'Item Code'}, inplace=True)
        
        # Make Item Code Columns
        df_name = (RawEGEDA[sheet].drop(['Product Number', 'Item Number'], axis=1).set_index(['Product Code', 'Item Code'])
                  .rename_axis(['Year'], axis=1)
                  .stack().unstack('Item Code')
                  .reset_index())
 
        # create column with economy name
        df_name['Economy'] = sheet

        df_list.append(df_name)

# combine individual economy dataframes to one dataframe
dfResults = pd.concat(df_list, sort=True).reset_index(drop=True)

# replace x and X placeholders with NaNs
dfResults = dfResults.replace('x', np.NaN)
dfResults = dfResults.replace('X', np.NaN)

# Make a list of Item Codes
# note that 15.1.2 has whitespace after the text
dfResults = dfResults[['Economy', 
    'Year', 'Product Code', 
    '01. Indigenous Production', 
    '02. Imports', 
    '03. Exports', 
    '04. International Marine Bunkers', 
    '05. Intarnational Aviation Bunkers',
    '06. Stock Changes', 
    '07. Total Primary Energy Supply', 
    '08. Transfers', 
    '09. Total Transformation Sector', 
    '09.01 Main Activity Producer', 
    '09.02 Autoproducers', 
    '09.03 Gas Processing', 
    '09.04 Refineries', 
    '09.05Coal Transformation', 
    '09.06 Petrochemical Industry', 
    '09.07 Biofuel Processing', 
    '09.08 Charcoal Processing', 
    '09.09 Non-specified Transformation', 
    '10. Loss & Own Use', 
    '11. Discrepancy', 
    'Total Final Consumption', 
    '12. Total Final Energy Consumptions', 
    '13. Industry Sector', 
    '14. Transport Sector', 
    '14.01 Domestic Air Transport', 
    '14.02 Road', 
    '14.03 Rail', 
    '14.04 Inland Waterways', 
    '14.05 Pipeline Transport', 
    '14.06 Non-specified Transport', 
    '15. Other Sector', 
    '15.1 Residential & Commercial', 
    '15.1.1 Commerce and Public Services', 
    '15.1.2 Residential ', 
    '15.2 Agriculture', 
    '15.3 Fishing', 
    '15.4 Non-specified Others', 
    '16. of which Non-Energy Use', 
    '16.1 Transformation Sector', 
    '16.2 Industry Sector', 
    '16.3 Transport Sector', 
    '16.4 Other Sector', 
    '17. Electricity Output in GWh', 
    '18. Heat Output in TJ']]

# fix typos
typos = {'05. Intarnational Aviation Bunkers':'05. International Aviation Bunkers',
    '15.1.2 Residential ':'15.1.2 Residential'}
dfResults.rename(typos, axis='columns',inplace=True)

# replace economies using APEC abbreviations
EconomyNames = {
        'AUS':'AUS',
        'BRN':'BD',
        'CAN':'CDA',
        'CHL':'CHL',
        'CHN':'PRC',
        'HKG':'HKC',
        'IDN':'INA',
        'JPN':'JPN',
        'KOR':'KOR',
        'MAS':'MAS',
        'MEX':'MEX',
        'NZL':'NZ',
        'PNG':'PNG',
        'PER':'PE',
        'PHL':'RP',
        'RUS':'RUS',
        'SGP':'SIN',
        'CT':'CT',
        'THA':'THA',
        'USA':'USA',
        'VNM':'VN'}

# code to replace economy abbreviations
# --code here--

# create dictionary of Product Code and APERC code
APERCcodes = {
        '02. Coal Products':'CoalP',
        '03. Crude Oil & NGL':'OilP'
        # and so on...
        }

#dfResults.replace(APERCcodes, inplace=True)

# write to csv
dfResults.to_csv(r'EGEDA\data\results\TidyEGEDA.csv', index=False)

print('\n----FINISHED----')


