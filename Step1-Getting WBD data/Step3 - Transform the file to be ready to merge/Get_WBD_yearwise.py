import sys
import requests
import pandas as pd
from openpyxl.workbook import Workbook
import xlsxwriter
import os
from Change_Country_Name import Change_Country_Names

# This creates the year wise WBD File.
# It needs the current World Bank Variables Year wise sheet.xlsx
# It renames it to World Bank Variables Year wise sheet_old.xlsx
# The Country Names need changes so Country names is copied from old file
# Headings are copied from old file
# New header Year_WBD is added
def main():
    writer = pd.ExcelWriter('WorldBank_yearwise.xlsx', engine='xlsxwriter')
    fname = "./WorldBank Combined Data LATEST.xlsx"
    orig_file = "./World Bank Variables Year wise sheet.xlsx"
    orig_df = pd.read_excel(orig_file,sheet_name=None)
    os.rename(orig_file,'./World Bank Variables Year wise sheet_old.xlsx')
    sname = list(orig_df.keys())[0]
    col_names = orig_df[sname].columns
    single_df = pd.read_excel(fname,sheet_name=None)
    yr_col = single_df['GDP Growth'].columns[2:]
    new_df= pd.DataFrame()

    new_country = single_df['GDP Growth']['Country Name']
    old_country = orig_df[sname]['Country Name'][:len(new_country)]
    print(old_country)
    # Some countries need to be modified. This code will name it as it is required in our project
    country_diff = [(i, new_country[i], old_country[i]) for i in range(len(new_country)) if
               new_country[i] != old_country[i]]
    print(country_diff)
    for year in yr_col:
        new_df = single_df['GDP Growth'].filter(['Country Name', 'Country Code'], axis=1)
        new_df['Country Name'] = Change_Country_Names(new_df['Country Name'])
        # new_df = orig_df[sname].filter(['Country Name', 'Country Code'], axis=1)[:len(single_df['GDP Growth'])]
        for key in single_df.keys():
            k = key.replace(" ","_")
            k = k.replace(',','')
            new_df[k] = single_df[key][year]

        new_df['Year_WBD'] = year

        if(len(new_df.columns) == len(col_names)):
            print("Columns Differ")
            changes = [(i, new_df.columns[i], col_names[i]) for i in range(len(new_df.columns)) if new_df.columns[i] != col_names[i]]
            print(changes)

        new_df.to_excel(writer, sheet_name=year, index=None)
    writer.save()
    os.rename('WorldBank_yearwise.xlsx','World Bank Variables Year wise sheet.xlsx')

if __name__ == "__main__":
    sys.exit(main())