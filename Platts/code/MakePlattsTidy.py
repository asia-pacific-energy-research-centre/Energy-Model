# MakeTidy.py
# Take Power subsector production data from the 7th and reshape in Tidy format
# https://stackoverflow.com/questions/45066873/pandas-melt-with-multiple-value-vars

# import math and data table functions
import numpy as np
import pandas as pd
import os
import datetime as dt

print("Script started. -- Current date/time:", dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# create directories for modified and results data
paths = {'path1':'Platts/data/modified','path2':'Platts/data/results'}
for key, value in paths.items(): 
        try:
            os.makedirs(value)
        except OSError:
            print ("Creation of the directory %s failed" % key)
        else:
            print ("Successfully created the directory %s " % key)

## David notes:
# - When reading CSV, use option to start at Row x, and specify header row
# - create a list for the columns you want to keep, then pass that list to the read_csv function so you don't
#   have to type the same thing in the next two read_csv calls

#Select power data from Platts database by choosing 16 out of 45 columns
RawPowerDataAsia = pd.read_csv(r'Platts\data\raw\MI_WorldElectricPowerPlants_Asia_March2019_v1.csv', usecols=['MW', 'STATUS', 'YEAR', 'UTYPE', 'FUEL', 'ALTFUEL', 'BOILTYPE', 'TURBTYPE', 'GENTYPE', 'STYPE', 'PARTCTL', 'SO2CTL', 'NOXCTL', 'RETIRE', 'COUNTRY', 'ELECTYPE'])
RawPowerDataNAmerica = pd.read_csv(r'Platts\data\raw\MI_WorldElectricPowerPlants_NorthAmerica_March2019_v1.csv', usecols=['MW', 'STATUS', 'YEAR', 'UTYPE', 'FUEL', 'ALTFUEL', 'BOILTYPE', 'TURBTYPE', 'GENTYPE', 'STYPE', 'PARTCTL', 'SO2CTL', 'NOXCTL', 'RETIRE', 'COUNTRY', 'ELECTYPE'])
RawPowerDataOther = pd.read_csv(r'Platts\data\raw\MI_WorldElectricPowerPlants_Other_March2019_v1.csv', usecols=['MW', 'STATUS', 'YEAR', 'UTYPE', 'FUEL', 'ALTFUEL', 'BOILTYPE', 'TURBTYPE', 'GENTYPE', 'STYPE', 'PARTCTL', 'SO2CTL', 'NOXCTL', 'RETIRE', 'COUNTRY', 'ELECTYPE'])

# Merge all three Platts database that are based on three world regions into one file
CombinedPowerData = pd.concat([RawPowerDataAsia, RawPowerDataNAmerica, RawPowerDataOther])

# Select only APEC economies except for Hong Kong which may be included in the CHINA data
CombinedPowerData = CombinedPowerData.loc[CombinedPowerData['COUNTRY'].isin(['AUSTRALIA', 'BRUNEI', 'CHINA', 'INDONESIA', 'JAPAN', 'PAPUA NEW GUINEA', 'SINGAPORE', 'THAILAND', 'TAIWAN', 'VIETNAM', 'CANADA', 'PHILIPPINES', 'USA', 'RUSSIA', 'NEW ZEALAND', 'CHILE', 'PERU','MALAYSIA','SOUTH KOREA','MEXICO'])]

## David notes:
# I didn't run this part yet, but let's be careful about dropping missing data just yet
# let's discuss further

#Rows to be deleted if MW value equal to 0 or does not exist
CombinedPowerData = CombinedPowerData[pd.notnull(CombinedPowerData['MW'])]

# write APEC Platts data to csv file
CombinedPowerData.to_csv(r'Platts\data\APECPlatts.csv', index=False)


# end of script
print("\nFINISHED. -- Current date/time:", dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))