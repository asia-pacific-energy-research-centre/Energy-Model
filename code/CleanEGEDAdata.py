# CleanEGEDAdata.py

# Take EGEDA 2016 data and reshape in Tidy format and clean
# https://stackoverflow.com/questions/45066873/pandas-melt-with-multiple-value-vars

# raw data file = APEC21_22Jul2019B_raw.xlsx
# manual adjustments made to the raw data file before the following code:
# - renamed 'MYS' to 'MAS'
# - removed column labels for columns A,B,C,D
# - removed summary rows at bottom of each sheet
# - removed miscellaneous calculations in row AP
# file used by the code is APEC21_22Jul2019B_ready.xlsx

#### Begin data manipulation ####

# import math and data table functions
import numpy as np
import pandas as pd
import os
import datetime as dt

print("Script started. -- Current date/time:", dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# create directories for modified and results data
paths = {'path1':'data\modified','path2':'data\modified','path3':'data\processed', 'path4':'results'}
for key, value in paths.items(): 
        try:
            os.makedirs(value)
        except OSError:
            print ("Directory %s exists." % value)
        else:
            print ("Successfully created the directory %s " % value)

# read all sheets from EGEDA spreadsheet to Pandas dictionary.
# units are in ktoe
# `sheet_name = none` means the output will be a dictionary that contains a key for each economy, 
# and the value is a dataframe with the table data.
print('\nImporting the raw EGEDA data...')
RawEGEDA = pd.read_excel(r'data\raw\APEC21_22Jul2019B_ready.xlsx', sheet_name=None, na_values=['x', 'X', ''])
print('...Imported raw EGEDA data!')
print('\nBegin cleaning...')

# define year range
years = list(range(1980,2016,1))

# create empty list to store each dataframe
df_list =[]
for sheet, dataframe in RawEGEDA.items():
        # rename blank columns
        RawEGEDA[sheet].rename(columns={'Unnamed: 0':'Product Number','Unnamed: 1':'Item Number', 'Unnamed: 2':'Product Code','Unnamed: 3':'Item Code'}, inplace=True)
        
        # Make Item Code Columns
        df_name = (RawEGEDA[sheet].drop(['Product Number', 'Item Number'], axis=1).set_index(['Product Code', 'Item Code'])
              .div(1000)
              .rename_axis(['Year'], axis=1)
              .stack().unstack('Item Code')
              .reset_index())
 
        # create column with economy name
        df_name['Economy'] = sheet

        df_list.append(df_name)

# combine individual economy dataframes to one dataframe
dfResults = pd.concat(df_list, sort=True).reset_index(drop=True)

# Reorder the columns to bring Economy, Year, and Product Code to the beginning
# note that there are typos
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
         '09.05Coal Transformation':'09.05 Coal Transformation',
         '15.1.2 Residential ':'15.1.2 Residential'}
dfResults.rename(typos, axis='columns',inplace=True)

# replace economies using APEC approved abbreviations
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
        'TWN':'CT',
        'THA':'THA',
        'USA':'USA',
        'VNM':'VN'}

# code to replace economy abbreviations
dfResults.replace(EconomyNames, inplace=True)

# create dictionary of EGEDA Product Codes and APERC Fuel code
Fuelcodes = {
        '01. Coal':'Coal',
        '02. Coal Products':'CoalP',
        '03. Crude Oil & NGL':'Oil',
        '04. Petroleum Products':'PetP',
        '04.01 Motor Gasoline   ':'PetPG',   
        '04.02 Naphtha':'PetPN',
        '04.03 Jet Fuel':'PetPJ',
        '04.04 Kerosene':'PetPK',
        '04.05 Gas/Diesel Oil ':'PetPD',
        '04.06 Fuel Oil':'PetPF',
        '04.07 LPG':'PetPL',
        '04.08 Refinery Gas':'PetPR',
        '04.09 Ethane':'PetPE',
        '04.10 Other Petroleum Products':'PetPO',
        '05. Gas':'Gas',
        '06. Hydro':'RenH',
        '07. Nuclear':'Nuc',        
        '08. Geothermal, Solar etc.':'RenNRE',
        '09. Others':'Oth',
        '10. Electricity':'Elec',
        '11. Heat':'Heat',
        '12. Total':'Tot',
        '13. Total Renewables':'TotRen'       
        }

# create dictionary of NEW Product Codes and APERC code
# to replace the above codes in late 2019 from new EGEDA release
FuelcodesNEW = {
        '1. Coal':'Coal',
        '1.1 Hard coal':'CoalH',
        '1.1.1 Coking coal':'CoalHC',   
        '1.1.2 Other bituminous coal':'CoalHB',
        '1.1.3 Sub-bituminous coal':'CoalHS',
        '1.2 Anthracite':'CoalA',
        '1.3 Lignite':'CoalL',
        '1.4 Peat':'CoalO',
        '2. Coal products':'CoalP',
        '2.1 Coke oven coke':'CoalPC',
        '2.2 Coke oven gas':'CoalPO',
        '2.3 Blast furnace gas':'CoalPF',
        '2.4 Oxygen steel furnace gas':'CoalPS',
        '2.5 Patent fuel':'CoalPP',
        '2.6 Coal tar':'CoalPT',
        '2.7 BKB/PB':'CoalPB',
        '3. Crude oil & NGL':'Oil',
        '3.1 Crude oil':'OilC',
        '3.2 Natural gas liquids':'OilN',
        '3.3 Refinery feedstocks':'OilOR',
        '3.4 Additives/  oxygenates':'OilOA',
        '3.5 Other hydrocarbons':'OilOO',
        '4. Petroleum Products':'PetP',
# [REDUNDANT] PetPGx
        '4.1 Gasoline':'PetPGx',
        '4.1.1 Motor gasoline':'PetPG',
        '4.1.2 Aviation gasoline':'PetPJG',
        '4.2 Naphtha':'PetPN',        
        '4.3 Jet Fuel':'PetPJ',        
        '4.3.1 Gasoline type jet fuel':'PetPJO',
        '4.3.2 Kerosene type jet fuel':'PetPJK',
        '4.4 Kerosene':'PetPK',
        '4.5 Gas/Diesel Oil':'PetPD',
        '4.6 Fuel Oil':'PetPF',
        '4.7 LPG':'PetPL',        
        '4.8 Refinery gas (not liquefied)':'PetPR',        
        '4.9 Ethane':'PetPE',        
        '4.10 Other Petroleum Products':'PetPO',
        '4.10.1 White spirit SBP':'PetPOW',
        '4.10.2 Lubricants':'PetPOL',
        '4.10.3 Bitumen':'PetPOB',
        '4.10.4 Paraffin  waxes':'PetPOP',
        '4.10.5 Petroleum coke':'PetPOC',
        '4.10.6 Other products':'PetPOO',
        '5. Gas':'Gas',        
        '5.1 Natural gas':'GasN',
        '5.2 LNG':'GasL',
        '5.3 Gas works gas':'GasO',
        '6 Hydro':'RenH',        
        '7 Nuclear':'Nuc',        
# [REDUNDANT] RenNRE
        '8 Geothermal, solar etc.':'RenNRE',        
        '8.1 Geothermal power':'RenGE',
# [REDUNDANT] RenOO
        '8.2 Other power':'RenOO',
        '8.2.1 Photovoltaic':'RenSE',
        '8.2.2 Tide, wave, ocean':'RenO',
        '8.2.3 Wind':'RenW',
        '8.2.4 Solar thermal':'RenSO',
        '8.3 Geothermal heat':'RenGH',
        '8.4 Solar heat':'RenSH',
        '9 Others':'Oth',
        '9.1 Fuelwood & woodwaste':'RenBSF',
        '9.2 Bagasse':'RenBSB',
        '9.3 Charcoal':'RenBSC',
        '9.4 Other biomass':'RenBSO',
        '9.5 Biogas':'RenBG',
        '9.6 Industrial waste':'OthI',
# [REDUNDANT] RenMSW
        '9.7 Municipal solid waste':'RenMSW',
        '9.7.1 Municipal solid waste (renewable)':'RenBSW',
        '9.7.2 Municipal solid waste (non-renewable)':'OthM',
        '9.8 Liquid biofuels':'RenBL',
        '9.8.1 Biogasoline':'RenBLE',
        '9.8.2 Biodiesel':'RenBLD',
        '9.8.3 Bio jet kerosene':'RenBLJ',
        '9.8.4 Other liquid biofuels':'RenBLO',
        '9.9 Other sources':'OthO',        
        '10. Electricity':'Elec',
        '11. Heat':'Heat',
        '12. Total':'Tot',
        '13. Total Renewables':'TotRen'       
        }

# code to replace fuel abbreviations
dfResults.replace(Fuelcodes, inplace=True)
#dfResults.replace(FUELcodesNEW, inplace=True)

dfResults.rename(columns={'Product Code':'Fuel Code'}, inplace=True)

# code to replace 'odd' Coal numbers in Brunei
dfResults.loc[(dfResults['Economy']=='BD') & (dfResults['Year'] < 1990) & (dfResults['Fuel Code']=='Coal'),'18. Heat Output in TJ']=0

# convert units from ktoe to Mtoe


## [GROUP] RenGE + RenGH = RenG 'Geothermal energy'
## [GROUP] RenSE + RenSH + RenSO = RenS 'Solar energy'
## [GROUP] RenBSF + RenBSB + RenBSC + RenBSO + RenBSW = RenBS 'Bioenergy Solid'
## [GROUP] RenBS + RenBL + RenBG = RenB 'Bioenergy'

# write to csv
dfResults.to_csv(r'data\processed\TidyEGEDA.csv', index=False)
print("\nFINISHED. -- Current date/time:", dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print('\nCleaned data saved in the folder %s' %paths['path3'])