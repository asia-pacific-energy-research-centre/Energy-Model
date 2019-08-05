# MakeTidy.py
# Take Power subsector production data from the 7th and reshape in Tidy format
# https://stackoverflow.com/questions/45066873/pandas-melt-with-multiple-value-vars

# import math and data table functions
import numpy as np
import pandas as pd

#Select power data from Platts database by choosing 16 out of 45 columns
RawPowerDataAsia = pd.read_csv(r'Platts\data\MI_WorldElectricPowerPlants_Asia_March2019_v1.csv', usecols=['MW', 'STATUS', 'YEAR', 'UTYPE', 'FUEL', 'ALTFUEL', 'BOILTYPE', 'TURBTYPE', 'GENTYPE', 'STYPE', 'PARTCTL', 'SO2CTL', 'NOXCTL', 'RETIRE', 'COUNTRY', 'ELECTYPE'])
RawPowerDataNAmerica = pd.read_csv(r'Platts\data\MI_WorldElectricPowerPlants_NorthAmerica_March2019_v1.csv', usecols=['MW', 'STATUS', 'YEAR', 'UTYPE', 'FUEL', 'ALTFUEL', 'BOILTYPE', 'TURBTYPE', 'GENTYPE', 'STYPE', 'PARTCTL', 'SO2CTL', 'NOXCTL', 'RETIRE', 'COUNTRY', 'ELECTYPE'])
RawPowerDataOther = pd.read_csv(r'Platts\data\MI_WorldElectricPowerPlants_Other_March2019_v1.csv', usecols=['MW', 'STATUS', 'YEAR', 'UTYPE', 'FUEL', 'ALTFUEL', 'BOILTYPE', 'TURBTYPE', 'GENTYPE', 'STYPE', 'PARTCTL', 'SO2CTL', 'NOXCTL', 'RETIRE', 'COUNTRY', 'ELECTYPE'])

# Merge all three Platts database that are based on three world regions into one file
CombinedPowerData = pd.concat([RawPowerDataAsia, RawPowerDataNAmerica, RawPowerDataOther])

# Select only APEC economies except for Hong Kong which may be included in the CHINA data
CombinedPowerData = CombinedPowerData.loc[CombinedPowerData['COUNTRY'].isin(['AUSTRALIA', 'BRUNEI', 'CHINA', 'INDONESIA', 'JAPAN', 'PAPUA NEW GUINEA', 'SINGAPORE', 'THAILAND', 'TAIWAN', 'VIETNAM', 'CANADA', 'PHILIPPINES', 'USA', 'RUSSIA', 'NEW ZEALAND', 'CHILE', 'PERU','MALAYSIA','SOUTH KOREA','MEXICO'])]

#Rows to be deleted if MW value equal to 0 or does not exist
CombinedPowerData = CombinedPowerData[pd.notnull(CombinedPowerData['MW'])]

# write APEC Platts data to csv file
CombinedPowerData.to_csv(r'Platts\data\APECPlatts.csv', index=False)