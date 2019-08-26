# EGEDA

## Contents
This folder contains EGEDA data and code to transform it to a form suitable for analysis.

### code folder
The code runs in the following order:
1. CleanEGEDAdata.py

#### 1.CleanEGEDAdata.py
Reshape EGEDA data in Tidy format by:
- removing unnecessary columns
- melting to Tidy Data
- renaming economy abbreviations
- replace 'x' and 'X' with NaN
- fixed typos in Item Codes

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

#### EGEDA fuels with APERC codes dictionary explnation
Format: EGEDA fuel name [APERC fuel code] definition

1 Coal [Coal] Solid fossil fuel consisting of carbonised vegetal matter.
    1.1 Hard coal [CoalH] Hard coal.
        1.1.1 Coking coal [CoalHC] A bituminous coal that can be used in the production of a coke capable of supporting a flast furnace charge.
        1.1.2 Other bituminous coal [CoalHB] A medium-rank hard coal with either a gross calorific value (moist, ash-free basis) not less than 24 MJ/kg and with a Vitrinite mean random reflectance less than 2%, or a gross calorific value (mois, ash-free basis) less than 24 MJ/kg provided that the Vitrinite mean random reflectance is equal to or greater than 0.6%.
        1.1.3 Sub-bituminous [CoalHS] A brown coal with a gross calorific value (moist, ash-free basis) equal to or greater than 20 MJ/kg, but less than 24 MJ/kg.
    1.2 Anthracite [CoalA] A high-rank, hard coal with a gross calorific value (moist, ash-free basis) greater than or equal to 24 MJ/kg and a Vitrinite mean random reflectance greater than or equal to 2.0%.
    1.3 Lignite [CoalL] A brown coal with a gross calorific value (moist, ash-free basis) less than 20 MJ/kg.
    1.4 Peat [CoalO] A solid formed from the partial decomposition of dead vegetation under conditions of high humidity and limited air access (initial stage of coalification). It is available in two forms for use as a fuel, sod peat and milled peat.

2 Coal products [CoalP] Coal products
    2.1 Coke oven coke [CoalPC] "Coke comprises coke oven coke and gas coke:
    Coke oven coke: the solid product obtained from carbonisation of coking coal at high temperature. Coke oven coke is low in moisture, and volatile matter and has the mechanical strength to support a blast furnace charge. It is used mainly in the iron and steel industry acting as heat source and chemical agent.
    Gas coke: a by-product from the carbonisation of bituminous coal for the manufacture of “gas works gas”. Gas coke is used mainly for heating purposes."
    2.2 Coke oven gas [CoalPO] A gas produced from coke ovens during the manufacture of coke oven coke.
    2.3 Blast furnace gas [CoalPF] The by-product gas of blast furnace operation consisting mainly of nitrogen, carbon dioxide and carbon monoxide. The gas is recovered as it leaves the furnace. Its calorific value arises mainly from the carbon monoxide produced by the partial combustion of coke and other carbon bearing products in the blast furnace. It is used to heat blast air and as a fuel in the iron and steel industry. It may also be used by other nearby industrial plants. Note that where carbonised biomass (e.g, charcoal or animal meal) is used in blast furnaces, part of the carbon supply may be considered renewable.
    2.4 Oxygen steel furnace gas [CoalPS] The by-product gas of the production of steel in a basic oxygen furnace. The gas is recovered as it leaves the furnace.
    2.5 Patent fuel [CoalPP] A composition fuel made by moulding hard coal fines into briquette shapes with the addition of a binding agent.
    2.6 Coal tar [CoalPT] The liquid by-product of the carbonisation of coal in coke ovens.
    2.7 BKB/PB [CoalPB] "BKB (Braunkohlenbriketts) is a composition fuel made of brown coal produced by briquetting under high pressure with or without the addition of a binding agent. PB (Peat briquettes) is a fuel comprising of small blocks of dried, highly compressed peat made without a binding agent."

3 Crude oil & NGL [Oil] Crude oil & NGL
    3.1 Crude oil [OilC] A mineral oil of fossil origin extracted by conventional means from underground reservoirs, and comprises liquid or near-liquid hydrocarbons and associated impurities such as sulphur and metals.It exists in the liquid phase under normal surface temperature and pressure, and usually flows to the surface under the pressure of the reservoir. This is termed “conventional” extraction. Crude oil includes condensate from condensate fields, and “field” or “lease” condensate extracted with the crude oil.
    3.2 Natural gas liquids [OilN] Mixture of ethane, propane, butane (normal and iso), (iso) pentane and a few higher alkanes collectively referred to as pentanes plus. NGL are produced in association with oil or natural gas. They are removed in field facilities or gas separation plants before sale of the gas. All of the components of NGL except ethane are either liquid at the surface or are liquefied for disposal.
    3.3 Refinery feedstocks [OilOR] Oils or gases from crude oil refining or the processing of hydrocarbons in the petrochemical industry which are destined for further processing in the refinery excluding blending. Typical feedstocks include naphthas, middle distillates, pyrolysis gasoline and heavy oils from vacuum distillation and petrochemical plants.
    3.4 Additives / oxygenates [OilOA] "Compounds added to or blended with oil products to modify their properties (octane, cetane, cold properties, etc.) Examples of these products are:
        (a) oxygenates such as alcohols (methanol, ethanol) and ethers such as methyl tertiary butyl ether (MTBE), ethyl tertiary butyl ether (ETBE), tertiary amyl methyl ether (TAME);
        (b) esters such as (e.g., rapeseed or dimethylester, etc.) and
        (c) chemical compounds such as tetramethyllead (TML), tetraethyllead (TEL) and detergents. Some additives and oxygenates may be derived from biomass while others may be of hydrocarbon origin."
    3.5 Other hydrocarbons [OilOO] "These are non-conventional oil and hydrogen. Non-conventional oils refer to oils obtained by non-conventional production techniques, that is oils which are extracted from reservoirs containing extra heavy oils or oil sands which need heating or treatment (e.g., emulsification) in situ before they can be brought to the surface for refining/processing. They also include oils extracted from oil sands, extra heavy oils, coal and oil shale which are at, or can be brought to the surface without treatment and require processing after mining (ex situ processing). Non-conventional oils may also be produced from natural gas. Hydrogen, although not a hydrocarbon, is included unless it is a component of another gas."

4 Petroleum products [PetP]
    4.1 Gasoline [PetPx] REDUNDANT Complex mixtures of volatile hydrocarbons distilling between approximately 25ºC and 220ºC and consisting of compounds in the C4 to C12 range.
        4.1.1 Motor gasoline [PetPG] Motor gasoline is a mixture of some aromatics (for example, benzene and toluene) and aliphatic hydrocarbons in the C5 to C12 range. The distillations range is 25ºC to 220ºC. Motor gasoline may also contain biogasoline products.
        4.1.2 Aviation gasoline [PetPJG] Aviation gasoline is gasoline prepared especially for aviation piston engines with additives which assure performance under flight conditions. Aviation gasolines are predominantly alkylates (obtained by combining C4 and C5 isoparaffins with C3, C4 and C5 olefins) with the possible addition of more aromatic components including toluene. The distillation range is 25ºC to 170ºC. 
    4.2 Naphtha [PetPN] Refers to light or medium oils distilling between 30ºC and 210ºC which do not meet the specification for motor gasoline. The main uses for naphthas are as feedstock for high octane gasolines and the manufacture of olefins in the petrochemical industry.
    4.3 Jet fuel [PetPJ]
        4.3.1 Gasoline type jet fuel [PetPJO] This includes all light hydrocarbon oils for use in aviation turbine power units, distilling between 100ºC and 250ºC. They are obtained by blending kerosene and gasoline or naphtha in such a way that the aromatic content does not exceed 25% in volume and the vapor pressure is between 13.7kilopascal (kPa) and 20.6 kPa.
        4.3.2 Kerosene type jet fuel [PetPJK] This is a blend of kerosene suited to flight conditions with particular specifications, such as freezing point. The specifications are set down by a small number of national standards committees, most notably, ASTM (US), MOD (UK), GOST (Russia).
    4.4 Kerosene [PetPK] "Comprise kerosene-type jet fuel and other kerosene. This is a mixture of hydrocarbons in the range C9 to C16 distilling over the temperature interval 145ºC to 300ºC, but not usually above 250ºC, and with a flash point above 38ºC.  Other kerosene: kerosene used for heating, cooking, lighting, solvents and internal combustion engines. Other names of this product are burning oil, vaporising oil, power kerosene and illuminating oil."
    4.5 Gas/Diesel oil [PetPD] Distillate fuel oil: middle distillates, predominantly of carbon number range C11 to C25 and with a distillation range of 160ºC to 420°C. This product comprises road diesel and heating or other gas oil.
    4.6 Fuel oil [PetPF] This comprises residual fuel oil and heavy fuel oil which is usually a blended product based on the residues from various refinery, distillation and cracking processes. Residual fuel oils A-5 have a distillation range of 350ºC to 650ºC and a kinematic viscosity in the range 6 to 55 centistokes (cSt) at 100ºC. Their flash point is always above 60ºC and their specific gravity is above 0.95.
    4.7 LPG [PetPL] Refers to liquefied propane (C3H8) and butane (C4H10) or mixtures of both. Commercial grades are usually mixtures of the gases with small amounts of propylene, butylene, isobutene and isobutylene stored under pressure in containers.
    4.8 Refinery gas (not liquefied) [PetPR] A mixture of non-condensable gases mainly consisting of hydrogen, methane, ethane and olefins obtained during distillation of crude oil or treatment of oil products (e.g., cracking) in refineries or from nearby petrochemical plants. It is used mainly as a fuel within the refinery.
    4.9 Ethane [PetPE] A naturally gaseous straight-chain hydrocarbon (C2H6). Ethane is obtained at gas separation plants or from the refining of crude oil. It is a valuable feedstock for petrochemical manufacture.
    4.10 Other petroleum products [PetPO]
        4.10.1 White spirit SBP [PetPOW] "White spirit and special boiling point industrial spirits (SBP) are refined distillate intermediates with a distillation in the naphtha/kerosene range. They are mainly used for non-fuel purposes and sub-divided as:
            (a) white spirit - an industrial spirit with a flash point above 30ºC and a distillation range of 135ºC to 200ºC; and
            (b) industrial spirit (SBP) – light oils distilling between 30ºC and 200ºC."
        4.10.2 Lubricants [PetPOL] Oils, produced from crude oil, for which the principal use is to reduce friction between sliding surfaces and during metal cutting operations.
        4.10.3 Bitumen [PetPOB] A solid, semi-solid or viscous hydrocarbon with a colloidal structure, being brown to black in color. It is obtained as a residue in the distillation of crude oil and by vacuum distillation of oil residues from atmospheric distillation. It should not be confused with the nonconventional primary extra heavy oils which may also be referred to as bitumen.
        4.10.4 Paraffin waxes [PetPOP] Residues extracted when dewaxing lubricant oils. The waxes have a crystalline structure which varies in fineness according to the grade, and are colourless, odourless and translucent, with a melting point above 45ºC.
        4.10.5 Petroleum coke [PetPOC] A black solid obtained mainly by cracking and carbonising heavy hydrocarbon oils, tars and pitches. It consists mainly of carbon (90 to 95 per cent) and has a low ash content. The two most important categories are "green coke" and "calcined coke". Green coke (raw coke) is the primary solid carbonisation product from high boiling hydrocarbon fractions obtained at temperatures below 630ºC. It contains 4-15 per cent by weight of matter that can be released as volatiles during subsequent heat treatment at temperatures up to approximately 1330ºC. Calcined coke is a petroleum coke or coal-derived pitch coke obtained by heat treatment of green coke to about 1330ºC. It will normally have a hydrogen content of less than 0.1 per cent by weight.
        4.10.6 Other products [PetPOO] Other products include products (including partly refined products) from the refining of crude oil and feedstocks which are not specified above.

5 Gas [Gas]
    5.1 Natural gas [GasN] "A mixture of gaseous hydrocarbons, primarily methane, but generally also including ethane, propane and higher hydrocarbons in much smaller amounts and some noncombustible gases such as nitrogen and carbon dioxide.
        Associated gas: gas produced in association with crude oil.
        Non-associated gas: gas originating from fields producing hydrocarbons only in gaseous form.
        Colliery gas: gas recovered from coal mines.
        Shale gas: natural gas produced from hydrocarbon rich shale formation. Shale gas is typically a dry gas primarily composed of methane (90% or more methane), but some formations do produce wet gas.
        Coal seam gas: Coal seam gas (also known as coal bed methane) is a form of natural gas extracted from coal seams."
    5.2 LNG [GasL] Liquid natural gas is produced by liquefaction of natural gas, liquefied by reducing its temperature in order to simplify storage and transportation when production sites are remote from centres of consumption and pipeline transportation is not economically practicable.
    5.3 Gas works gas [GasW] "This group includes gases obtained from the carbonisation or gasification of carbonaceous material of fossil or biomass origins in gas works. The gases comprise:
        (a) gases obtained from carbonisation or gasification of coals, cokes, biomass or waste; and
        (b) substitute natural gas (a methane-rich gas) made from synthesis gas."

6 Hydro [RenH] Electricity produced from devices driven by fresh, flowing or falling water.
??? 6.1 Hydro Conventional [RenHC]
??? 6.2 Hydro Pumped Storage [RenHP]

7 Nuclear [Nuc] Electricity and heat generation from nuclear plants.
    7.1 Nuclear fuel [Nuke]

8 Geothermal, solar, etc. [RenNRE]
    8.1 Geothermal power [RenGE] Electricity and heat generation produced from geothermal plants.
    8.2 Other power [RenOO]
        8.2.1 Photovoltaic [RenSE] Electricity from solar photovoltaics refers to electricity produced by the direct conversion of solar radiation through photovoltaic processes in semiconductor devices (solar cells), including concentrating photovoltaic systems.
        8.2.2 Tide, wave, ocean [RenO] Electricity generation produced from tide / wave / ocean.
        8.2.3 Wind [RenW] Electricity produced from devices driven by wind.
        8.2.4 Solar other [RenSO] e.g. Concentrated Solar power
    8.3 Geothermal heat [RenGH] Electricity and heat generation produced from geothermal plants.
    8.4 Solar heat [RenSH] Heat from concentrating solar thermal refers to high temperature heat produced from solar radiation captured by concentrating solar thermal systems. The high temperature heat can be transformed to generate electricity, drive chemical reactions, or be used directly in industrial processes. Heat from non-concentrating solar thermal refers to low temperature heat produced from solar radiation captured by non-concentrating solar thermal systems.

9 Others
    9.1 Fuel wood & Woodwaste [RenBSF] "Fuelwood (in log, brushwood, pellet or chip form) obtained from natural or managed forests or isolated trees. Also included are wood residues used as fuel and in which the original composition of wood is retained. Charcoal and black liquor are excluded. Woodwaste is yard trash and types of waste typically generated by sawmills, plywood mills, and woodyards associated with the lumber and paper industry, such as wood residue, cutoffs, wood chips, sawdust, wood shavings, bark, wood refuse, wood-fired boiler ash, and plywood or other bonded materials that contain only phenolic-based glues or other glues that are approved specifically by the administrative authority."
    9.2 Bagasse [RenBSB] The fuel obtained from the fibre which remains after juice extraction in sugar cane processing.
    9.3 Charcoal [RenBSC] The solid residue from the carbonisation of wood or other vegetal matter through slow pyrolysis.
    9.4 Other biomass [RenBSO] All other solid biomass products not specifically mentioned above. This includes agricultural wastes such as straw, rice husks, nut shells, poultry litter, crushed grape dregs, palm oil bunches, etc. The quantity of fuel used should be reported on a net calorific value basis.
    9.5 Biogas [RenBG] "Gases arising from the anaerobic fermentation of biomass and the gasification of solid biomass (including biomass in wastes):
        Landfill gas: biogas from the anaerobic fermentation of organic matter in landfills.
        Sewage sludge gas: biogas from the anaerobic fermentation of waste matter in sewage plants.
        Other biogas: other biogases from anaerobic fermentation not elsewhere specified."
    9.6 Industrial waste [OthI] Non-renewable waste which is combusted with heat recovery in plants other than those used for the incineration of municipal waste.
    9.7 Municipal solid waste [RenMSW] REDUNDANT
        9.7.1 Municipal solid waste (renewable) [RenBSW] Municipal solid waste (renewables): household waste and waste from companies and public services that resembles household waste and which is collected at installations specifically designed for the disposal of mixed wastes with recovery of combustible liquids, gases or heat.
        9.7.2 Municipal solid waste (non-renewable) [OthM]
    9.8 Liquid biofuels [RenBL] "Fuels derived directly or indirectly from biomass:
        Biogasoline: refers to liquid fuels derived from biomass and used in spark- ignition internal combustion engines. Biogasoline may be blended with petroleum gasoline or used directly in engines. The blending may take place in refineries or at or near the point of sale.
        Biodiesel: liquid biofuels derived from biomass and used in diesel engines. Biodiesels may be blended with petroleum diesel or used directly in diesel engines.
        Bio-jet kerosene: liquid biofuels derived from biomass and blended with or replacing jet kerosene. 
        Bioethanol: ethanol produced from biomass and/or biodegradable fraction of waste;
        Biomethanol: methanol produced from biomass and/or the biodegradable fraction of waste;
        Biodimethylether: a diesel quality fuel produced from biomass and/or the biodegradable fraction of waste;
        Bio-oil: a pyrolysis oil fuel produced from biomass"
        9.8.1 Biogasoline [RenBLE] Ethanol produced from biomass and/or biodegradable fraction of waste.
        9.8.2 Biodiesel [RenBLD] Liquid biofuels derived from biomass and used in diesel engines. Biodiesels may be blended with petroleum diesel or used directly in diesel engines.
        9.8.3 Bio jet kerosene [RenBLJ] 
        9.8.4 Other liquid biofuels [RenBLO]
    9.9 Other sources [OthO]

10 Electricity [Elec]

11 Heat [Heat] 
    11.1 Heating [HeatF] non-EGEDA
    11.2 Cooling [HeatC] non-EGEDA

xx Hydrogen [H2] non-EGEDA
    xx.1 Hydrogen fuel [H2F] non-EGEDA

12 Total [Tot]

13 Total renewables [TotRen]