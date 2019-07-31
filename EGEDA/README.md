# EGEDA

## Contents
This folder contains EGEDA data and code to transform it to a form suitable for analysis.

### code folder
The code runs in the following order:
1. MakeEGEDATidy.py

#### 1.CleanEGEDAdata.py
Reshape EGEDA data in Tidy format by:
- removing unnecessary columns
- melting to Tidy Data
- renaming economy abbreviations
- replace 'x' and 'X' with NaN

### data folder
Contains raw EGEDA data.

#### 1.raw
*APEC21_22Jul2019B_raw.xlsx* - EGEDA data provided by Edito on July 22, 2019. It contains data up to and including 2016.

#### 2.modified
*APEC21_22Jul2019B_ready.xlsx* - This is a manually modified copy of *APEC21_22Jul2019B_raw.xlsx*. The following adjustments were made:
- renamed 'MYS' to 'MAS'
- removed column labels for columns A,B,C,D
- removed summary rows at bottom of each sheet
- removed miscellaneous calculations in row AP

This file is used by *CleanEGEDAdata.py*

#### 2.results
*TidyEGEDA.csv* - EGEDA data after processing using *CleanEGEDAdata.py*.
