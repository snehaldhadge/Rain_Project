import pandas as pd 
import numpy as numpy
import random 
from itertools import chain

def rename_icon_columns_wbd(df):
 df.rename(columns={'Country Code':'WBD_councode'
,'GDP_Growth':'WBD_GDPg'
,'GDPperCapitaPPP':'WBD_GDPpc'
,'Exports_As_GDP':'WBD_eGDP'
,'FDI':'WBD_FDI'
,'ServicesValueAddedAsGDP':'WBD_SVAasGDP'
,'RuralPopulationAsTPopulation':'WBD_RPasTP'
,'GenderParityIndex':'WBD_GPI'
,'CO2EmissionsPerCapita':'WBD_co2pc'
,'Population Growth':'WBD_pg'
,'RenewableEnergyConsuption':'WBD_REC'
,'UnemploymentRate':'WBD_UR'
,'Expenditures on Education':'WBD_EonE'
,'TertiarySchoolEnrollmentAsPerce':'WBD_TSE %'
,'WomenLaborForceParticipation':'WBD_WLFP'
,'OreAndMetalsExports':'WBD_OME'
,'EnergyIMports':'WBD_energyI'
,'MarketCapitalizationAsGDP':'WBD_MCasGDP'
,'PublichHealthExpenditures':'WBD_PHE'
,'AgingPopulation':'WBD_AP'
,'MobilePhonesDiffusion':'WBD_MPD'
,'InternetServersperMillion':'WBD_ISpermil'
,'Air_transport_registered_carri':'WBD_ATR'
,'PortContainerTraffic':'WBD_PCT'
,'GINI':'WBD_GINI'
,'DisclosureIndex':'WBD_discloserI'
,'BanksAsSourceofCredit':'WBD_bankasSOC'
,'HighTechExports':'WBD_HTE'
,'InternationalTourismExpenditure':'WBD_ITE'
,'InternationalTourismReceipts':'WBD_ITR'
,'LeadTimeToExport':'WBD_leadtimeE'
,'MerchandiseTrade':'WBD_MT'
,'StrengthofLegalRights':'WBD_strengthLR'
,'NumberOfSTartupProcedures':'WBD_startup_procedures'
,'IntentionalHomicides':'WBD_IH'
,'NewBusinessFormation':'WBD_NBF'
,'ResearchAndDevelopemntSpending':'WBD_RandDspending'
,'PatentApplicationResidents':'WBD_patentapps'
,'TrademarkAppsResdients':'WBD_TMapps'
,'ResearchersinR_D':'WBD_researchersRD'
,'FuelExport':'WBD_FE'
,'Year_WBD':'WBD_year'
},inplace=True)
 df.columns
 return df



def rename_tcon_columns_wbd(df):
  df.rename(columns={'Country Code':'WBD_councode_t'
,'GDP_Growth':'WBD_GDPg_t'
,'GDPperCapitaPPP':'WBD_GDPpc_t'
,'Exports_As_GDP':'WBD_eGDP_t'
,'FDI':'WBD_FDI_t'
,'ServicesValueAddedAsGDP':'WBD_SVAasGDP_t'
,'RuralPopulationAsTPopulation':'WBD_RPasTP_t'
,'GenderParityIndex':'WBD_GPI_t'
,'CO2EmissionsPerCapita':'WBD_co2pc_t'
,'Population Growth':'WBD_pg_t'
,'RenewableEnergyConsuption':'WBD_REC_t'
,'UnemploymentRate':'WBD_UR_t'
,'Expenditures on Education':'WBD_EonE_t'
,'TertiarySchoolEnrollmentAsPerce':'WBD_TSE %_t'
,'WomenLaborForceParticipation':'WBD_WLFP_t'
,'OreAndMetalsExports':'WBD_OME_t'
,'EnergyIMports':'WBD_energyI_t'
,'MarketCapitalizationAsGDP':'WBD_MCasGDP_t'
,'PublichHealthExpenditures':'WBD_PHE_t'
,'AgingPopulation':'WBD_AP_t'
,'MobilePhonesDiffusion':'WBD_MPD_t'
,'InternetServersperMillion':'WBD_ISpermil_t'
,'Air_transport_registerecarri':'WBD_ATR_t'
,'PortContainerTraffic':'WBD_PCT_t'
,'GINI':'WBD_GINI_t'
,'DisclosureIndex':'WBD_discloserI_t'
,'BanksAsSourceofCredit':'WBD_bankasSOC_t'
,'HighTechExports':'WBD_HTE_t'
,'InternationalTourismExpenditure':'WBD_ITE_t'
,'InternationalTourismReceipts':'WBD_ITR_t'
,'LeadTimeToExport':'WBD_leadtimeE_t'
,'MerchandiseTrade':'WBD_MT_t'
,'StrengthofLegalRights':'WBD_strengthLR_t'
,'NumberOfSTartupProcedures':'WBD_startup_procedures_t'
,'IntentionalHomicides':'WBD_IH_t'
,'NewBusinessFormation':'WBD_NBF_t'
,'ResearchAndDevelopemntSpending':'WBD_RandDspending_t'
,'PatentApplicationResidents':'WBD_patentapps_t'
,'TrademarkAppsResdients':'WBD_TMapps_t'
,'ResearchersinR_D':'WBD_researchersRD_t'
,'FuelExport':'WBD_FE_t'
,'Year_WBD':'WBD_year_t'
},inplace=True)
 
  return df

def rename_tcon_columns_wgi(df):
    df = df.rename(columns={'WGI_CC':'WGI_CC_t',
                       'WGI_GE':'WGI_GE_t',
                       'WGI_RL':'WGI_RL_t',
                       'WGI_RQ':'WGI_RQ_t',
                       'WGI_VA':'WGI_VA_t',
                       'WGI_pstabilityNV':'WGI_pstabilityNV_t'})
    return df

def get_year_data(bmi_data,year):
    cols = [c for c in bmi_data.columns if c.startswith(year) or c.startswith('Unnamed')]
    new_df =  bmi_data[cols]
    new_df.columns= ['Country','both_sexes','male','female']
    new_df['adate_year'] = year
    return new_df[2:]

def replace_company_columns(year):
    col1 = [
'BvD ID number',
'Operating revenue (Turnover)\nm USD 2015' ,
'P/L before tax\nm USD 2015' ,
'Working capital\nm USD 2015' ,
'Cash & cash equivalent\nm USD 2015' ,
'Total Liabilities and Equity\nm USD 2015' ,
'Short Term Debt, Net\nm USD 2015' ,
'Long Term Debt, Net\nm USD 2015' ,
'Number of employees\n2015' ,
'Export revenue\nm USD 2015' ,
'Costs of employees\nm USD 2015' ,
'Research & Development expenses\nm USD 2015' ,
'Cash flow\nm USD 2015' ,
'EBITDA\nm USD 2015' ,
'Profit margin (%)\n2015' ,
'Export revenue / Operating revenue (%)\n2015' ,
'R&D expenses / Operating revenue (%)\n2015', 
'Current ratio\n2015' ,
'Liquidity ratio\n2015' ,
'Profit per employee (th) (th)\nth USD 2015' ,
'Operating revenue per employee (th) (th)\nth USD 2015' ,
'Costs of employees / Operating revenue (%)\n2015' ,
'Market price - year end\nUSD 2015' ,
'Market price - high\nUSD 2015' ,
'Market price - low\nUSD 2015' ,
'Market capitalisation (m)\nm USD 2015' ,
'Cash flow per share\nUSD 2015' ,
'Capital expenditure per share\nUSD 2015' ,
'Earnings per share\nUSD 2015' ,
'Operating revenue (Turnover) per share\nUSD 2015' ,
'Operating profit per share\nUSD 2015' ,
'Dividends per share\nUSD 2015' ,
'Book Value per share\nUSD 2015' ,
'Tangible Book Value per share\nUSD 2015' ,
'Long Term Liabilities per share\nUSD 2015' ,
'Working Capital per share\nUSD 2015' ,
 ]
    return [sub.replace('2015',str(year)) for sub in col1]


# Cross check the entire Deals File to make sure data is correct

deals_data = pd.read_excel('Final_Deals_2020.xlsx')
deals_data.shape



# Reading the old errorneous file to make sure the row and column counts are same
deals_old = pd.read_excel("Final DEALS 2020_old.xlsx")
deals_old.shape

# There is a row mismatch and column mismatch due to years chosen from 2014-2019
# Cross check for rows count for years from 2014-2019
deals_o_filtered = deals_old[(deals_old.adateyear.isin([2014,2015,2016,2017,2018,2019])) | (deals_old.adate.isnull() & deals_old.rdate.isnull() & deals_old.laststatusdate.notnull())]
deals_o_filtered.shape

if deals_o_filtered.shape[0] == deals_data.shape[0] :
    print(" The Row count matches")

final_cols=[]

# First cross check the WBD data
# picking few WBD columns and cross checking the data

Wbd_cols = deals_data.filter(regex=r'^WBD', axis=1).columns
wbd_tcols = deals_data.filter(regex=r'^WBD.*_t$', axis=1).columns
wbd_icols = set(Wbd_cols) - set(wbd_tcols)
#list( set(gc_data['GlobalCity']) - set(deals_data['tcity']) )
wgi_cols = deals_data.filter(regex=r'^WGI', axis=1).columns
wgi_tcols = deals_data.filter(regex=r'^WGI.*_t$', axis=1).columns
wgi_icols = set(wgi_cols) - set(wgi_tcols)

ipri_cols = deals_data.filter(regex=r'^ipri', axis=1).columns
ipri_tcols = deals_data.filter(regex=r'^ipri.*_t$', axis=1).columns
ipri_icols = set(ipri_cols) - set(ipri_tcols)
bmi_cols = deals_data.filter(regex=r'^bmi', axis=1).columns
bmi_tcols = deals_data.filter(regex=r'^bmi.*_t$', axis=1).columns
bmi_icols = set(bmi_cols) - set(bmi_tcols)
gc_cols = deals_data.filter(regex=r'^GC', axis=1).columns
gc_icols = deals_data.filter(regex=r'^GC.*_i$', axis=1).columns
gc_tcols = set(gc_cols) - set(gc_icols)
company_cols = ['oper_turnover','PL_beforetax','wcapital','cash',
'TLE','ST_debt','LT_debt','empl','EXP','cost_empl','RD','cashflow','EBITDA',
'profit_margin','ER_OR','RD_OR','current_ratio','iliquidity_ratio','profit_empl','OR_empl',
'cost_empl_OR','MP_current','MP_high','MP_low','mcapital','CF_share',
'expen_share','EPS','OperPS','OPPS','DPS','BVPS','TBVPS','LTLPS','WCPS']
gaWC_cols = ['i_GaWC_int','i_GaWC_int_fine','t_GaWC_int','t_GaWC_int_fine','i_GaWC_un','i_GaWC_un_fine','t_GaWC_un','t_GaWC_un_fine']

rest_cols = deals_data.filter(['icoun','adateyear','tcoun','iBVDid','icity','tcity'], axis=1).columns
rest_cols


final_cols = list(chain(Wbd_cols, wgi_cols, ipri_cols,bmi_cols,gc_cols,company_cols,gaWC_cols,rest_cols))

wbd = pd.ExcelFile("World Bank Variables Year wise sheet.xlsx")

wgi = pd.ExcelFile("WGI_yearwise.xlsx")

ipri = pd.read_excel("International Property Rights Index.xlsx")
ipri_col =  [col for col in ipri if col.startswith('Score')]
ipri_selected = ipri[ipri_col]
ipri_selected = ipri_selected.rename(columns = lambda x: x.split(' ')[1])
ipri_selected['Countries'] = ipri['Countries']

gc_data = pd.read_excel("Global (World) Cities List - Beaverstock et al.xlsx")

city_dict ={'AbuDhabi':'Abu Dhabi',
'Bogotá':'Bogota',
'CapeTown':'Cape Town',
'Düsseldorf':'Dusseldorf',
'HoChiMinhCity':'Ho Chi Minh City',
'HongKong':'Hong Kong',
'KansasCity':'Kansas City',
'KualaLumpur':'Kuala Lumpur',
'LosAngeles':'Los Angeles',
'MexicoCity':'Mexico City',
'NewDelhi':'New Delhi',
'NewYork':'New York',
'RiodeJaneiro':'Rio De Janeiro',
'SanFrancisco':'San Francisco',
'SãoPaulo':'Sao Paulo',
'St.Petersburg':'St Petersburg',
'TelAviv':'Tel Aviv',
'Zürich':'Zurich',
'BuenosAires':'Buenos Aires',
'TheHague':'The Hague',
'Brasília':'Brasilia',
}

for c in city_dict.items():
    indexes = gc_data.loc[gc_data.GlobalCity == c[0]].index
    gc_data.at[indexes,'GlobalCity'] =c[1]

gc_data.GlobalCity = gc_data.GlobalCity.astype(str)


bmi_data = pd.read_csv("BMI_data.csv")
bmi_data.loc[bmi_data['Unnamed: 0'] == 'Viet Nam','Unnamed: 0'] = 'Vietnam'
bmi_data.loc[bmi_data['Unnamed: 0'] == 'Venezuela (Bolivarian Republic of)','Unnamed: 0'] = 'Venezuela'
bmi_data.loc[bmi_data['Unnamed: 0'] == 'United Kingdom of Great Britain and Northern Ireland','Unnamed: 0'] = 'United Kingdom'
bmi_data.loc[bmi_data['Unnamed: 0'] == 'Myanmar','Unnamed: 0'] = 'Myanmar/Burma'
bmi_data.loc[bmi_data['Unnamed: 0'] == "Lao People's Democratic Republic",'Unnamed: 0'] = "Lao People'S Democratic Republic"
bmi_data.loc[bmi_data['Unnamed: 0'] == 'Iran (Islamic Republic of)','Unnamed: 0'] = 'Islamic Republic of Iran'
bmi_data.loc[bmi_data['Unnamed: 0'] == 'Democratic Republic of the Congo','Unnamed: 0'] = 'Democratic Republic of Congo'
bmi_data.loc[bmi_data['Unnamed: 0'] == "C�te d'Ivoire",'Unnamed: 0'] = "Côte D'Ivoire"
bmi_data.loc[bmi_data['Unnamed: 0'] == 'Czechia','Unnamed: 0'] = 'Czech Republic'
bmi_data.loc[bmi_data['Unnamed: 0'] == 'Bolivia (Plurinational State of)','Unnamed: 0'] = 'Bolivia'

years = ['2014','2015','2016']
df = []

for yr in years:
    df.append(get_year_data(bmi_data,yr))

bmi_df = pd.concat(df)

# Get GaWC file
gc_wc_I = pd.read_excel("GaWC Alpha Global Cities.xlsx",sheet_name="Intersection",header=None)
gc_wc_U = pd.read_excel("GaWC Alpha Global Cities.xlsx",sheet_name="Union",header=None)
gc_wc_I.columns = gc_wc_I.iloc[1]
gc_wc_I = gc_wc_I[2:]
gc_wc_U.columns = gc_wc_U.iloc[1]
gc_wc_U = gc_wc_U[2:]

gc_wc_I['Country'].mask(gc_wc_I['Country'] == 'Russia', 'Russian Federation', inplace=True)
gc_wc_I['Country'].mask(gc_wc_I['Country'] == 'UAE', 'United Arab Emirates', inplace=True)
gc_wc_I['Country'].mask(gc_wc_I['Country'] == 'U.S.', 'United States of America', inplace=True)

gc_wc_U['Country'].mask(gc_wc_U['Country'] == 'Russia', 'Russian Federation', inplace=True)
gc_wc_U['Country'].mask(gc_wc_U['Country'] == 'UAE', 'United Arab Emirates', inplace=True)
gc_wc_U['Country'].mask(gc_wc_U['Country'] == 'U.S.', 'United States of America', inplace=True)
gc_wc_U['Country'].mask(gc_wc_U['Country'] == 'Korea', 'Republic of Korea', inplace=True)

# deals_data['icity'] = deals_data['icity'].str.lower()
# deals_data['icity']= deals_data['icity'].str.title() 
# deals_data['tcity'] = deals_data['tcity'].str.lower()
# deals_data['tcity']= deals_data['tcity'].str.title() 

# Choose randon rows to cross check the data
for i in range(30):
    random_rows = random.randint(1,55746)
    data_df_l = deals_data.loc[random_rows,final_cols]
    data_df = data_df_l.to_frame()
    data_df = data_df.T
    data_df = data_df.reset_index(drop=True)
    wbd_year = wbd.parse(data_df.iloc[0]['adateyear'].astype(int).astype(str))
    data_df = data_df.apply(pd.to_numeric, errors='ignore', axis=1)
    # Check for icountry data
    wbd_idata = wbd_year[data_df.iloc[0]['icoun'] == wbd_year['Country Name']]
    wbd_tdata = wbd_year[data_df.iloc[0]['tcoun'] == wbd_year['Country Name']]
    wbd_idata = wbd_idata.reset_index(drop=True)

    wbd_tdata = wbd_tdata.reset_index(drop=True)

    wbd_idata_m = rename_icon_columns_wbd(wbd_idata)
    wbd_tdata_m = rename_tcon_columns_wbd(wbd_tdata)


    data_df.loc[:, data_df.dtypes == object] = data_df.loc[:,data_df.dtypes == object].fillna('')
    data_df.loc[:, data_df.dtypes != object] = data_df.loc[:,data_df.dtypes != object].fillna(0).astype(float).round(4)
    wbd_idata_m.loc[:, wbd_idata_m.dtypes == object] = wbd_idata_m.loc[:,wbd_idata_m.dtypes == object].fillna('')
    wbd_idata_m.loc[:, wbd_idata_m.dtypes != object] = wbd_idata_m.loc[:,wbd_idata_m.dtypes != object].fillna(0).astype(float).round(4)

    # if ((round(wbd_idata_m[wbd_icols],4), round(data_df[wbd_icols],4), check_index_type=False)):
    if (wbd_idata_m[wbd_icols].equals(data_df[wbd_icols])):
        print("Row: "+ str(random_rows) +" matches for WBD icoun")
    else:
        print("Rows do not match for WBD  please check for icoun row:" +str(random_rows))
        print(data_df[wbd_icols])
        print(wbd_idata_m[wbd_icols])
    
    wbd_tdata_m.loc[:, wbd_tdata_m.dtypes == object] = wbd_tdata_m.loc[:,wbd_tdata_m.dtypes == object].fillna('')
    wbd_tdata_m.loc[:, wbd_tdata_m.dtypes != object] = wbd_tdata_m.loc[:,wbd_tdata_m.dtypes != object].fillna(0).astype(float).round(4)

    if (wbd_tdata_m[wbd_tcols].equals(data_df[wbd_tcols])):
        print("Row: "+ str(random_rows) +" matches for WBD tcoun")
    else:
        print("Rows do not match for WBD  please check for tcoun row:" +str(random_rows))
        print(data_df[wbd_tcols])
        print(wbd_tdata_m[wbd_tcols])

    # Check for WGI

    wgi_year = wgi.parse(data_df.iloc[0]['adateyear'].astype(int).astype(str))

    # Check for icountry data
    wgi_idata = wgi_year[data_df.iloc[0]['icoun'] == wgi_year['Countr']]
    wgi_tdata = wgi_year[data_df.iloc[0]['tcoun'] == wgi_year['Countr']]
    wgi_idata = wgi_idata.reset_index(drop=True)

    wgi_tdata = wgi_tdata.reset_index(drop=True)



    wgi_tdata_m = rename_tcon_columns_wgi(wgi_tdata)
    wgi_idata.loc[:, wgi_idata.dtypes == object] = wgi_idata.loc[:,wgi_idata.dtypes == object].fillna('')
    wgi_idata.loc[:, wgi_idata.dtypes != object] = wgi_idata.loc[:,wgi_idata.dtypes != object].fillna(0).astype(float).round(4)

    wgi_tdata_m.loc[:, wgi_tdata_m.dtypes == object] = wgi_tdata_m.loc[:,wgi_tdata_m.dtypes == object].fillna('')
    wgi_tdata_m.loc[:, wgi_tdata_m.dtypes != object] = wgi_tdata_m.loc[:,wgi_tdata_m.dtypes != object].fillna(0).astype(float).round(4)


    comparison_array = wgi_idata[wgi_icols].values == data_df[wgi_icols].values

    if False in comparison_array:
        print("Rows do not match for WGI icoun please check "+ str(random_rows))
        print(data_df[wgi_icols].values)
        print(wgi_idata[wgi_icols].values)
    else:
        print("Row: "+ str(random_rows) +" matches for WGI icoun")
    
    comparison_array_1 = wgi_tdata_m[wgi_tcols].values == data_df[wgi_tcols].values

    if False in comparison_array_1:
        print("Rows do not match for WGI tcoun please check "+ str(random_rows))
        print(data_df[wgi_tcols].values)
        print(wgi_tdata_m[wgi_tcols].values)
    else:
        print("Row: "+ str(random_rows) +" matches for WGI tcoun")


    # Check for IPRI
  
    yr = str(data_df.iloc[0]['adateyear'].astype(int))
    ipri_s = ipri_selected[['Countries',yr]]
    ipri_s = ipri_s.rename(columns={yr:'ipri'})
   
    ipri_idata = ipri_s[ipri_s['Countries'] == data_df.iloc[0]['icoun']]
    ipri_tdata = ipri_s[ipri_s['Countries'] == data_df.iloc[0]['tcoun']]
    
    if(ipri_idata.empty == False):
        if(ipri_idata.iloc[0]['ipri'] == int(data_df.iloc[0]['ipri'])):
            print("IPRI data matches for icoun row:" + str(random_rows))
        else:
            print("Please check the IPRI mismatches for icoun row: "+ str(random_rows))
            print(data_df.iloc[0]['ipri'])
            print(ipri_idata)

    else:
        print("ICountry:"+str(data_df.iloc[0]['icoun'])+" does not exist in IPRI so values will be null")
        print(data_df.iloc[0]['ipri'])
        
    
    if(ipri_tdata.empty == False):
        if ( ipri_tdata.iloc[0]['ipri'] == int(data_df.iloc[0]['ipri_t'])):
            print("IPRI data matches for tcoun and row: " + str(random_rows))
        else:
            print("Please check the IPRI mismatches for tcoun for row: "+ str(random_rows))
            print(data_df.iloc[0]['ipri_t'])
            print(ipri_tdata)
    else:
        print("Target Country:"+str(data_df.iloc[0]['tcoun'])+" does not exist in IPRI so values will be null")
        print(data_df.iloc[0]['ipri_t'])
    
    
    gc_idata = gc_data[(gc_data['Country'] == data_df.iloc[0]['icoun']) & (gc_data['GlobalCity'] == data_df.iloc[0]['icity'])]
    gc_tdata = gc_data[(gc_data['Country'] == data_df.iloc[0]['tcoun']) & (gc_data['GlobalCity'] == data_df.iloc[0]['tcity'])]


# Checking for the GC data
    if(gc_idata.empty == False):
        if ( gc_idata.iloc[0]['GC1'] == data_df.iloc[0]['GC1_i']) & ( gc_idata.iloc[0]['GC2'] == data_df.iloc[0]['GC2_i']) :
          print("GC idata matches at row:"+ str(random_rows))
        else:
          print("Please check the GC mismatches at row:" + str(random_rows))
    else:
        print("This City "+str(data_df.iloc[0]['icity']) +"has no entry in GC so should be Nan (displayed as 0) ")
    
    if(gc_tdata.empty == False):
        if(gc_tdata.iloc[0]['GC1'] == data_df.iloc[0]['GC1']) & ( gc_tdata.iloc[0]['GC2'] == data_df.iloc[0]['GC2']):
            print("GC idata matches at row:"+ str(random_rows))
        else:
            print("Please check the GC mismatches at row:" + str(random_rows))
    else:
        print("This Target City "+str(data_df.iloc[0]['tcity']) +" has no entry in GC so should be Nan (displayed as 0)")

# Checking BMI data
    bmi_idata = bmi_df[(bmi_df['Country'] == data_df.iloc[0]['icoun']) & (bmi_df['adate_year'] == yr) ]
    bmi_tdata = bmi_df[(bmi_df['Country'] == data_df.iloc[0]['tcoun']) &  (bmi_df['adate_year'] == yr)]
    if(bmi_idata.empty == False):
        if((bmi_idata.iloc[0]['both_sexes'] == data_df.iloc[0]['bmi_both_sexes']) &
         (bmi_idata.iloc[0]['male'] == data_df.iloc[0]['bmi_male']) &
         (bmi_idata.iloc[0]['female'] == data_df.iloc[0]['bmi_female'])):
            print("bmi data matches for iCountry for row:"+str(random_rows))
        else:
            
            print("Please check the bmi mismatches for iCountry at row: "+ str(random_rows))
            print(data_df.iloc[0][bmi_cols])
            print(bmi_idata)

    else:
        print("adateyear does not have bmi data so values should be Nan for icountry" )
        print(data_df.iloc[0][bmi_cols])
    
    if(bmi_tdata.empty == False):
        if((bmi_tdata.iloc[0]['both_sexes'] == data_df.iloc[0]['bmi_both_sexes_t']) &
         (bmi_tdata.iloc[0]['male'] == data_df.iloc[0]['bmi_male_t']) &
         (bmi_tdata.iloc[0]['female'] == data_df.iloc[0]['bmi_female_t'])):
            print("bmi data matches for tCountry for row:"+str(random_rows))
        else:
            
            print("Please check the bmi mismatches for tCountry at row: "+ str(random_rows))
            print(bmi_tdata)
    else:
        print("adateyear does not have bmi data so values should be Nan for tcountry")
        print(data_df[bmi_cols] )
    


# Cross check company data
    file_name = "Companies_Deals_"+ str(data_df.iloc[0]['adateyear'].astype(int)-1)+".xlsx"
    print(file_name)
    print(data_df.iloc[0]['adateyear'])
    data = pd.read_excel(file_name)
    data_cols = replace_company_columns(data_df.iloc[0]['adateyear'].astype(int)-1)
    selected_data = data[data_cols]
    col2 = [
'iBVDid',
'oper_turnover',
'PL_beforetax',
'wcapital',
'cash',
'TLE',
'ST_debt',
'LT_debt',
'empl',
'EXP',
'cost_empl',
'RD',
'cashflow',
'EBITDA',
'profit_margin',
'ER_OR',
'RD_OR',
'current_ratio',
'iliquidity_ratio',
'profit_empl',
'OR_empl',
'cost_empl_OR',
'MP_current',
'MP_high',
'MP_low',
'mcapital',
'CF_share',
'expen_share',
'EPS',
'OperPS',
'OPPS',
'DPS',
'BVPS',
'TBVPS',
'LTLPS',
'WCPS'
]
    selected_data.columns = col2
    
    comp_data = selected_data[selected_data['iBVDid'] == data_df.iloc[0]['iBVDid']][company_cols]
    print(data_df.iloc[0]['iBVDid']) 
    comp_data = comp_data.reset_index(drop=True)
    comp_data.loc[:, comp_data.dtypes == object] = comp_data.loc[:,comp_data.dtypes == object].fillna('')
    comp_data.loc[:, comp_data.dtypes != object] = comp_data.loc[:,comp_data.dtypes != object].fillna(0).astype(float).round(4)
    
    
    if(comp_data.empty == False):
       if(comp_data[company_cols].equals(data_df[company_cols])):
         print("Companies data match for row :"+str(random_rows))
       else:
        print("Companies data do not match for row :"+str(random_rows))
        print(data_df.iloc[0][company_cols])
        print(data_df.iloc[0]['iBVDid'])
        print(comp_data)
    else:
        print("No company data is present")


    gc_wc_I_id = gc_wc_I[(gc_wc_I['Country'] == data_df.iloc[0]['icoun']) & (gc_wc_I['City'] == data_df.iloc[0]['icity'])]
    gc_wc_I_td = gc_wc_I[(gc_wc_I['Country'] == data_df.iloc[0]['tcoun']) & (gc_wc_I['City'] == data_df.iloc[0]['tcity'])]
    
    if(gc_wc_I_id.empty==False):
        if ( gc_wc_I_id.iloc[0]['GaWC_int'] == data_df.iloc[0]['i_GaWC_int']) & ( gc_wc_I_id.iloc[0]['GaWC_int_fine'] == data_df.iloc[0]['i_GaWC_int_fine']) :
          print("GaWC investor country matches at row:"+ str(random_rows))
        else:
          print("Please check the GaWC investor countrymismatches at row:" + str(random_rows))
    else:
        print("This City "+str(data_df.iloc[0]['icity']) +"has no entry in GaWC so should be Nan (displayed as 0) ")
        print(gc_wc_I_id)
    
    if(gc_wc_I_td.empty == False):
        if(gc_wc_I_td.iloc[0]['GaWC_int'] == data_df.iloc[0]['t_GaWC_int']) & ( gc_wc_I_td.iloc[0]['GaWC_int_fine'] == data_df.iloc[0]['t_GaWC_int_fine']):
            print("GaWC target country matches at row:"+ str(random_rows))
        else:
            print("Please check the GaWC target country mismatches at row:" + str(random_rows))
    else:
        print("This Target City "+str(data_df.iloc[0]['tcity']) +" has no entry in GaWC so should be Nan (displayed as 0)")
        print(gc_wc_I_td)
    gc_wc_U_id = gc_wc_U[(gc_wc_U['Country'] == data_df.iloc[0]['icoun']) & (gc_wc_U['City'] == data_df.iloc[0]['icity'])]
    gc_wc_U_td = gc_wc_U[(gc_wc_U['Country'] == data_df.iloc[0]['tcoun']) & (gc_wc_U['City'] == data_df.iloc[0]['tcity'])]
    
    if(gc_wc_U_id.empty==False):
        if ( gc_wc_U_id.iloc[0]['GaWC_un'] == data_df.iloc[0]['i_GaWC_un']) & ( gc_wc_U_id.iloc[0]['GaWC_un_fine'] == data_df.iloc[0]['i_GaWC_un_fine']) :
          print("GaWC Union investor country matches at row:"+ str(random_rows))
        else:
          print("Please check the GaWC Union investor country mismatches at row:" + str(random_rows))
    else:
        print("This City "+str(data_df.iloc[0]['icity']) +"has no entry in GaWC Union so should be Nan (displayed as 0) ")
        print(gc_wc_U_id)
    if(gc_wc_U_td.empty == False):
        if(gc_wc_U_td.iloc[0]['GaWC_un'] == data_df.iloc[0]['t_GaWC_un']) & ( gc_wc_U_td.iloc[0]['GaWC_un_fine'] == data_df.iloc[0]['t_GaWC_un_fine']):
            print("GaWC Union target country matches at row:"+ str(random_rows))
        else:
            print("Please check the GaWC Union target country mismatches at row:" + str(random_rows))
    else:
        print("This Target City "+str(data_df.iloc[0]['tcity']) +" has no entry in GaWC Union so should be Nan (displayed as 0)")
        print(gc_wc_U_td)