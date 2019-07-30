# Worldbank_Cleaner.py

# Import tools
import pandas as pd
import re
import numpy as np
import os
desired_width=320

# create modified data directory
path = "World Bank/modified"
try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)


input_file_name = 'World Bank\data\raw\WB_DATA_raw.csv'
output_file_name = 'World Bank\data\modified\WB_data_tidy.csv'

pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',10)

# Add Data
wb_data = pd.read_csv(input_file_name)

# clean up the column names and make a list of all years in the series
wb_coloumns = (list(wb_data.columns))
wb_coloumns_cleen = []
wb_coloumns_years = []
for coloumn in wb_coloumns:
    coloumn_cleen = re.sub(r"\[.*\]", "", coloumn).strip()
    wb_coloumns_cleen.append(coloumn_cleen)
    for num in coloumn:
        if num.isdigit() and coloumn_cleen not in wb_coloumns_years:
            wb_coloumns_years.append(coloumn_cleen)

# replace columns names with cleaned up names
wb_data = wb_data.set_axis(wb_coloumns_cleen, axis=1, inplace=False)

# list all unique series in the data set
unique_series_names = wb_data["Series Name"].unique()
unique_series_names = unique_series_names[~pd.isnull(unique_series_names)]
unique_series_names_list = unique_series_names.tolist()
columns_add = ['Year','Country Code','Country Name']
for string in columns_add:
    unique_series_names_list.insert(0,string)

#print(unique_series_names_list)

# make years a single a single column
wb_melt_years = pd.melt(wb_data, id_vars =['Country Name','Country Code','Series Name'], value_vars=wb_coloumns_years,
                        var_name='Year')\
    .dropna()

# set index to all collunms exept the "values" and unstack on the "Series Name"
wb_melt_years.set_index(keys=(list(wb_melt_years.columns)[:-1]), inplace = True)
wb_data_tidy = wb_melt_years.unstack("Series Name")
wb_data_tidy.reset_index(inplace= True, col_level=1)
wb = wb_data_tidy.drop([0],axis= 0)
wb.columns = wb.columns.droplevel()

# write tidy data to csv
wb.to_csv(output_file_name)






