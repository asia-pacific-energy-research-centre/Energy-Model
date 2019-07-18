# Energy-Model

## IMPORTANT
***Remember to create your own branch before you start making edits!!!***

When you are ready to share your changes, _push_ your branch then make _Pull Request_.

## Contents
This repository contains the data and code to run the [APERC](https://aperc.ieej.or.jp/) Energy Model.

Folders are structured by type of analysis:
1. Macro
2. EGEDA
3. Demand

There is a shared data folder for putting final datasets that all models can use. Think of it as the "integration" folder from the 7th. 

#### Shared Data
The following data series are stored here for use in the other models:
- GDP (historical and projected)
- Population
- Other?

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