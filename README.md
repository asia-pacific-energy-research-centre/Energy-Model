# Energy-Model

## IMPORTANT
***Remember to create your own branch before you start making edits!!!***

How to use and make edits:
1. In GitHub Desktop, create a new branch - *do not make changes to 'development'!*
2. Open the Energy-Model folder in your text editor.
3. When you are ready to share your changes, _push_ your branch then make a _Pull Request_.
4. Someone will review your changes.
5. If there are no issues, the changes will be merged.

## Folder contents
Folders are structured by type of analysis:
1. Macro
2. EGEDA
3. Demand

#### 1. Macro
This model supplies the GDP projections.

#### 2. EGEDA
Historical data are sourced from [EGEDA](https://www.egeda.ewg.apec.org/). This folder contains scripts for mapping and aggregating the raw EGEDA data to the naming convention used by the models.

#### 3. Demand
End-use service demands are estimated for the following demand sectors:
- Buildings
- Industry
- Transport

#### Optimization
OSeMOSYS will be added...

## Requirements
Scripts for data cleaning and manipulation are written in Python. The optimization (linear programs) are written in GAMS.