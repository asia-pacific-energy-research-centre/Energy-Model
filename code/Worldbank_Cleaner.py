# Worldbank_Cleaner.py

# Import tools
import pandas as pd
import re
import numpy as np
import os
import datetime as dt

print("Script started. -- Current date/time:", dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

desired_width=320

# create results directory
path = "results"
try:
    os.mkdir(path)
except OSError:
    print(' ')
else:
    print ("Successfully created the directory %s " % path)

# set file path names
input_file_name = 'data/WB_DATA_raw.csv'
output_file_name = 'results/WB_data_tidy.csv'

pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',10)

# Add Data
wb_data = pd.read_csv(input_file_name)

# clean up the column names and make a list of all years in the series
wb_columns = (list(wb_data.columns))
wb_columns_clean = []
wb_columns_years = []
for coloumn in wb_columns:
    column_clean = re.sub(r"\[.*\]", "", coloumn).strip()
    wb_columns_clean.append(column_clean)
    for num in coloumn:
        if num.isdigit() and column_clean not in wb_columns_years:
            wb_columns_years.append(column_clean)

# replace columns names with cleaned up names
wb_data = wb_data.set_axis(wb_columns_clean, axis=1, inplace=False)

# list all unique series in the data set
unique_series_names = wb_data["Series Name"].unique()
unique_series_names = unique_series_names[~pd.isnull(unique_series_names)]
unique_series_names_list = unique_series_names.tolist()
columns_add = ['Year','Country Code','Country Name']
for string in columns_add:
    unique_series_names_list.insert(0,string)

#print(unique_series_names_list)

# make years a single a single column
wb_melt_years = pd.melt(wb_data, id_vars =['Country Name','Country Code','Series Name'], value_vars=wb_columns_years,
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

print("Results are saved. -- Current date/time:", dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))