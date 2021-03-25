import sys
import requests
import pandas as pd
from openpyxl.workbook import Workbook
import xlsxwriter
import os
from Change_Country_Name import Change_Country_Names
# This reads the WGIDataset_latest and the WGI_yearwise from Google Drive
# The Column names need to follow what is in the old file

def main():
    writer = pd.ExcelWriter('WGI_yearwise_new.xlsx', engine='xlsxwriter')
    fname = "./WGIDataset_Latest.xlsx"
    orig_file = "./WGI_yearwise.xlsx"
    # Reading the old yearwise file
    orig_df = pd.read_excel(orig_file,sheet_name=None,header=[0,1])
    os.rename(orig_file,'./WGI_yearwise_old.xlsx')

    # setting column names from the old yearwise file

    sname = list(orig_df.keys())[0]
    # col_names = orig_df[sname].columns.levels[0]

    # Create dictionary with sheet name to convert into column name
    new_col_n = {'VoiceandAccountability':'WGI_VA',
                 'Political StabilityNoViolence':'WGI_pstabilityNV',
                 'GovernmentEffectiveness':'WGI_GE',
                 'RegulatoryQuality':'WGI_RQ',
                 'RuleofLaw':'WGI_RL',
                 'ControlofCorruption':'WGI_CC'}

    yr_df = pd.DataFrame()
    single_df = pd.read_excel(fname,sheet_name=None,header=[1,2],index_col=[0,1])

    # get all the sheet names
    f_sheet = list(single_df.keys())[0]

    # Get year after columns country name and country code onwards
    yr_col = list(single_df[f_sheet].columns.levels[0])[2:]
    # The file is multiindexed so converting into normal dataframe
    for key in single_df.keys():
        idx = pd.IndexSlice
        new_df = single_df[key].loc[:, idx[:, 'Estimate']]
        new_df = new_df.droplevel(1, axis=1)
        new_df.reset_index(inplace=True)
        new_df.rename(columns={'level_0': 'Country Name'}, inplace=True)
        new_df.rename(columns={'level_1': 'Country Code'}, inplace=True)
        single_df[key] = new_df

    # Convert into yearwise sheet
    for year in yr_col:
     yr_df['Countr'] = single_df[f_sheet]['Country Name']
     yr_df['Countr'] = Change_Country_Names(yr_df['Countr'])
     for key in single_df.keys():
        yr_df[new_col_n[key]] = single_df[key][year]
     yr_df.to_excel(writer, sheet_name=str(year), index=None)

    writer.save()
    os.rename('WGI_yearwise_new.xlsx','WGI_yearwise.xlsx')

if __name__ == "__main__":
    sys.exit(main())