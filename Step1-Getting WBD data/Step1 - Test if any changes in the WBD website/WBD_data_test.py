# This code is to check for discrepancies in all of the World Bank Data Indicators
# the Indicators are mentioned in the World_Bank_data_indicators word document
# Code downloads each of the indicator excel from the website https://data.worldbank.org/indicator
# Compares it with the corresponding Sheet in the Excel "WorldBank Combined Data LATEST"
# Out File is Excel_GDP_growth_diff.xlsx
# This file has each indicator as Sheets and difference in values are represented as
# {our file value} --> {actual website value}
# This file should be run yearly to check if the data is updated in the website and we need
# to sync out excel to new data
# To run this file have this Python file and "WorldBank Combined Data LATEST" in your local

import pandas as pd
import requests
import numpy as np
import os

# Reading the excel file downloaded from website
def get_DataFrame(url,f_name,sname):
    r = requests.get(url, allow_redirects=True)
    open(f_name, 'wb').write(r.content)

    df = pd.read_excel(f_name,
                                  sheet_name="Data",
                                  index_col=None,
                                  skiprows=3
                                 )

    w_df = get_diff(sname,df)
    w_df.to_excel(writer, sheet_name=sname, index=None)

# This function compares the two excel data
# The Excel Excel_WBD_diff will display cells which are different between the two files.
def get_diff(sname,gdp_growth_df):
    wbd_gdp_growth = pd.read_excel(open('WorldBank Combined Data LATEST.xlsx', 'rb'), sheet_name=sname)
    # The website Excel has more columns like data from 1960-1999. Taking only the common  columns
    common_cols = list(set.intersection(set(wbd_gdp_growth), set(gdp_growth_df)))
    c_df = gdp_growth_df[common_cols].sort_index(axis=1).round(1)
    w_df = wbd_gdp_growth[common_cols].sort_index(axis=1).round(1)

    # Check all the columns where values are different
    difference = w_df.reset_index(drop=True).fillna('NULL') == c_df.reset_index(drop=True).fillna('NULL')
    rows, cols = np.where(difference == False)

    # Write into Excel_WBD_diff the difference in values
    # Each difference is represented as {current_value} --> {New value}
    # if the values are same there is no change
    for item in zip(rows, cols):
        w_df.iloc[item[0], item[1]] = '{} --> {}'.format(w_df.iloc[item[0], item[1]], c_df.iloc[item[0], item[1]])

    return w_df

writer = pd.ExcelWriter('/Users/snehalilawe/Desktop/SDSU JOB/RAIN/Excel_GDP_growth_diff.xlsx', engine='xlsxwriter')
# GDP Growth Indicator
# Downloads the excel from worldbank.org and saves it as GDP_Growth_annual_percent.xls
url = 'http://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.KD.ZG?downloadformat=excel'
f_name = 'GDP_Growth_annual_percent.xls'
sname = 'GDP Growth'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

# GrowthPerCapitaPPP(current International $)
url = 'http://api.worldbank.org/v2/en/indicator/NY.GDP.PCAP.PP.CD?downloadformat=excel'
f_name = 'GrowthPerCapita_PPP.xls'
sname = 'GDPperCapitaPPP'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

# Exports of goods and services (% of GDP)
url = 'http://api.worldbank.org/v2/en/indicator/NE.EXP.GNFS.ZS?downloadformat=excel'
f_name = 'Exports_as_%_GDP.xls'
sname = 'Exports As GDP'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

# Foreign Direct Investment(FDI)
#https://data.worldbank.org/indicator/BX.KLT.DINV.CD.WD
url = 'http://api.worldbank.org/v2/en/indicator/BX.KLT.DINV.CD.WD?downloadformat=excel'
f_name = 'FDI_net_inflow.xls'
sname = 'FDI'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

# Services value added as % of GDP
# https://data.worldbank.org/indicator/NV.SRV.TOTL.ZS?view=chart
url = 'http://api.worldbank.org/v2/en/indicator/NV.SRV.TOTL.ZS?downloadformat=excel'
f_name = 'ServicesAddedValue.xls'
sname = 'ServicesValueAddedAsGDP'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

### Agriculture
# Rural Population as % of Total Population
# https://data.worldbank.org/indicator/SP.RUR.TOTL.ZS?view=chart
url = 'http://api.worldbank.org/v2/en/indicator/SP.RUR.TOTL.ZS?downloadformat=excel'
f_name = 'RuralPopulation.xls'
sname = 'RuralPopulationAsTPopulation'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

### Aid Effectiveness
# Gender Parity Index
# https://data.worldbank.org/indicator/SE.ENR.PRSC.FM.ZS?view=chart
url = 'http://api.worldbank.org/v2/en/indicator/SE.ENR.PRSC.FM.ZS?downloadformat=excel'
f_name = 'GenderParityIndex.xls'
sname = 'GenderParityIndex'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

### Climate Change
# CO2 Emissions tons per Capita
# https://data.worldbank.org/indicator/EN.ATM.CO2E.PC?view=chart
url = 'http://api.worldbank.org/v2/en/indicator/EN.ATM.CO2E.PC?downloadformat=excel'
f_name = 'CO2Emissions.xls'
sname = 'CO2EmissionsPerCapita'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

# Population Growth
# https://data.worldbank.org/indicator/SP.POP.GROW?view=chart
url = 'http://api.worldbank.org/v2/en/indicator/SP.POP.GROW?downloadformat=excel'
f_name = 'PopulationGrowth.xls'
sname = 'Population Growth'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

# Renewable Energy Consumption
# https://data.worldbank.org/indicator/EG.FEC.RNEW.ZS?view=chart
url = 'http://api.worldbank.org/v2/en/indicator/EG.FEC.RNEW.ZS?downloadformat=excel'
f_name = 'Renewable_Energy_Consumption.xls'
sname = 'RenewableEnergyConsuption'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

### Education
# Unemployment Rate
#https://data.worldbank.org/indicator/SL.UEM.TOTL.ZS?view=chart
url = 'http://api.worldbank.org/v2/en/indicator/SL.UEM.TOTL.ZS?downloadformat=excel'
f_name = 'Unemp_Rate.xls'
sname = 'UnemploymentRate'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

# Expenditures on Education
# https://data.worldbank.org/indicator/SE.XPD.TOTL.GB.ZS?view=chart
url = 'http://api.worldbank.org/v2/en/indicator/SE.XPD.TOTL.GB.ZS?downloadformat=excel'
f_name = 'Expenditure_on_Edu.xls'
sname = 'Expenditures on Education'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

# Tertiary Enrollment Ratio
# https://data.worldbank.org/indicator/SE.TER.ENRR?view=chart
url = 'http://api.worldbank.org/v2/en/indicator/SE.TER.ENRR?downloadformat=excel'
f_name = 'TertiaryEnrollmentRatio.xls'
sname = 'TertiarySchoolEnrollmentAsPerce'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

# Women Participation in Labor Force as a percentage total labor force
# https://data.worldbank.org/indicator/SL.TLF.TOTL.FE.ZS?view=chart
url = 'http://api.worldbank.org/v2/en/indicator/SL.TLF.TOTL.FE.ZS?downloadformat=excel'
f_name = 'WomenLaborForceParticipation.xls'
sname = 'WomenLaborForceParticipation'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

# Energy & Mining
# Ore and Metal Exports as % of total Exports
# https://data.worldbank.org/indicator/TX.VAL.MMTL.ZS.UN
url = 'http://api.worldbank.org/v2/en/indicator/TX.VAL.MMTL.ZS.UN?downloadformat=excel'
f_name = 'OreAndMetalsExports.xls'
sname = 'OreAndMetalsExports'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

# Fuel Exports as % of total Exports
# https://data.worldbank.org/indicator/TX.VAL.FUEL.ZS.UN?view=chart
url = 'http://api.worldbank.org/v2/en/indicator/TX.VAL.FUEL.ZS.UN?downloadformat=excel'
f_name = 'FuelExports.xls'
sname = 'FuelExport'
get_DataFrame(url,f_name,sname)

# Energy Imports as % of total energy Use
# https://data.worldbank.org/indicator/EG.IMP.CONS.ZS?view=chart
url = 'http://api.worldbank.org/v2/en/indicator/EG.IMP.CONS.ZS?downloadformat=excel'
f_name = 'EnergyIMports.xls'
sname = 'EnergyIMports'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

### 7.	Financial Sector
# Market Capitalization (of Listed Domestic Companies as a % of GDP)
# https://data.worldbank.org/indicator/CM.MKT.LCAP.GD.ZS?view=chart
url = 'http://api.worldbank.org/v2/en/indicator/CM.MKT.LCAP.GD.ZS?downloadformat=excel'
f_name = 'MarketCapitalizationAsGDP.xls'
sname = 'MarketCapitalizationAsGDP'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

### 8.	Health
# Public health Expenditure as % of total Health expenditures (both public and private)
# https://data.worldbank.org/indicator/SH.XPD.CHEX.GD.ZS?view=chart
url = 'http://api.worldbank.org/v2/en/indicator/SH.XPD.CHEX.GD.ZS?downloadformat=excel'
f_name = 'PublichHealthExpenditures.xls'
sname = 'PublichHealthExpenditures'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

# Aging Population (65 and older as % of Total population)
# Population (65 and older as % of Total population)
# https://data.worldbank.org/indicator/SP.POP.65UP.TO.ZS
url = 'http://api.worldbank.org/v2/en/indicator/SP.POP.65UP.TO.ZS?downloadformat=excel'
f_name = 'AgingPopulation.xls'
sname = 'AgingPopulation'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

### Infrastructure
# Mobile Phone Diffusion (subscription per 100 people)
# https://data.worldbank.org/indicator/IT.CEL.SETS.P2?view=chart
url = 'http://api.worldbank.org/v2/en/indicator/IT.CEL.SETS.P2?downloadformat=excel'
f_name = 'MobilePhonesDiffusion.xls'
sname = 'MobilePhonesDiffusion'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

# Secure Internet Servers per Million people
url = 'http://api.worldbank.org/v2/en/indicator/IT.NET.SECR.P6?downloadformat=excel'
f_name = 'InternetServersperMillion.xls'
sname = 'InternetServersperMillion'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

# Air transport, registered carrier departures9
url = 'http://api.worldbank.org/v2/en/indicator/IS.AIR.DPRT?downloadformat=excel'
f_name = 'Air transport, registered carri.xls'
sname = 'Air transport, registered carri'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

# Container port traffic (TEU: 20 foot equivalent units)
url = 'http://api.worldbank.org/v2/en/indicator/IS.SHP.GOOD.TU?downloadformat=excel'
f_name = 'PortContainerTraffic.xls'
sname = 'PortContainerTraffic'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

### Poverty
# GINI
url = 'http://api.worldbank.org/v2/en/indicator/SI.POV.GINI?downloadformat=excel'
f_name = 'GINI.xls'
sname = 'GINI'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

### Private Sector

# Disclosure Index (the higher the more investor protection)
url = 'http://api.worldbank.org/v2/en/indicator/IC.BUS.DISC.XQ?downloadformat=excel'
f_name = 'DisclosureIndex.xls'
sname = 'DisclosureIndex'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

# Banks as source of credit for working capital financie (Firms using banks to finance working capital (% of firms))
url = 'http://api.worldbank.org/v2/en/indicator/IC.FRM.BKWC.ZS?downloadformat=excel'
f_name = 'BanksAsSourceofCredit.xls'
sname = 'BanksAsSourceofCredit'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

# High Tech Exports (% of manufactured exports)
url = 'http://api.worldbank.org/v2/en/indicator/TX.VAL.TECH.MF.ZS?downloadformat=excel'
f_name = 'HighTechExports.xls'
sname = 'HighTechExports'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

# •	International Tourism Expenditures (% of total imports)
url = 'http://api.worldbank.org/v2/en/indicator/ST.INT.XPND.MP.ZS?downloadformat=excel'
f_name = 'InternationalTourismExpenditure.xls'
sname = 'InternationalTourismExpenditure'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

# Intl Tourism Receipts (% of total exports)
url = 'http://api.worldbank.org/v2/en/indicator/ST.INT.RCPT.XP.ZS?downloadformat=excel'
f_name = 'InternationalTourismReceipts.xls'
sname = 'InternationalTourismReceipts'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

# Lead time to export
url = 'http://api.worldbank.org/v2/en/indicator/LP.EXP.DURS.MD?downloadformat=excel'
f_name = 'LeadTimeToExport.xls'
sname = 'LeadTimeToExport'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

# •	Merchandise Trade as % of GDP
url = 'http://api.worldbank.org/v2/en/indicator/TG.VAL.TOTL.GD.ZS?downloadformat=excel'
f_name = 'MerchandiseTrade.xls'
sname = 'MerchandiseTrade'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

# •	Strength of Legal Rights
url = 'http://api.worldbank.org/v2/en/indicator/IC.LGL.CRED.XQ?downloadformat=excel'
f_name = 'StrengthofLegalRights.xls'
sname = 'StrengthofLegalRights'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

# NumberOfSTartupProcedures
url = 'http://api.worldbank.org/v2/en/indicator/IC.REG.PROC?downloadformat=excel'
f_name = 'NumberOfSTartupProcedures.xls'
sname = 'NumberOfSTartupProcedures'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

# •	Tax rate on commercial profits
url = 'http://api.worldbank.org/v2/en/indicator/IC.TAX.TOTL.CP.ZS?downloadformat=excel'
f_name = 'TaxRateCommercialProfit.xls'
sname = 'TaxRateCommercialProfit'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

# IntentionalHomicides
url = 'http://api.worldbank.org/v2/en/indicator/VC.IHR.PSRC.P5?downloadformat=excel'
f_name = 'IntentionalHomicides.xls'
sname = 'IntentionalHomicides'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

# # NewBusinessFormation
url = 'http://api.worldbank.org/v2/en/indicator/IC.BUS.NDNS.ZS?downloadformat=excel'
f_name = 'NewBusinessFormation.xls'
sname = 'NewBusinessFormation'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

# ResearchAndDevelopemntSpending
url = 'http://api.worldbank.org/v2/en/indicator/GB.XPD.RSDV.GD.ZS?downloadformat=excel'
f_name = 'ResearchAndDevelopemntSpending.xls'
sname = 'ResearchAndDevelopemntSpending'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

# PatentApplicationResidents
url = 'http://api.worldbank.org/v2/en/indicator/IP.PAT.RESD?downloadformat=excel'
f_name = 'PatentApplicationResidents.xls'
sname = 'PatentApplicationResidents'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

# TrademarkAppsResdients
url = 'http://api.worldbank.org/v2/en/indicator/IP.TMK.RESD?downloadformat=excel'
f_name = 'TrademarkAppsResdients.xls'
sname = 'TrademarkAppsResdients'
get_DataFrame(url,f_name,sname)
os.remove(f_name)

# ResearchersinR_D
url = 'http://api.worldbank.org/v2/en/indicator/SP.POP.SCIE.RD.P6?downloadformat=excel'
f_name = 'ResearchersinR_D.xls'
sname = 'ResearchersinR_D'
get_DataFrame(url,f_name,sname)
os.remove(f_name)


# Close the Pandas Excel writer and output the Excel file.
writer.save()
#
