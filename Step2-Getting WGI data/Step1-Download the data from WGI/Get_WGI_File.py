import sys
import requests
import pandas as pd
from openpyxl.workbook import Workbook
import xlsxwriter
import os

writer = pd.ExcelWriter('WGIDataset_Latest.xlsx', engine='xlsxwriter')
def get_DataFrame(f_name,sname):

    # excel_df = pd.read_excel(f_name,
    #                              sheet_name=sname,
    #                              header=[0,1],
    #                              index_col= [0] ,
    #                              skiprows=13
    #                              )
    excel_df = pd.read_excel(f_name,
                             sheet_name=sname,
                             header=[0, 1],
                             skiprows=13
                             )
    # excel_df = excel_df.drop(['index'],axis=1)
    
    # skip rows 2:14 as we need data from year 2000 onwards
    df = excel_df.drop(excel_df.iloc[:, 2:14], axis=1)

    df.T.reset_index().T.to_excel(writer, sheet_name=sname, index=None)



def main():

    # Downloads the excel from following link and saves it as WGIDataset_Latest.xlsx
    url = 'https://info.worldbank.org/governance/wgi/Home/downLoadFile?fileName=wgidataset.xlsx'
    f_name = 'WGIDataset_Website.xls'
    r = requests.get(url, allow_redirects=True)
    open(f_name, 'wb').write(r.content)
    # The file contain following Indicators as individual sheets
    get_DataFrame(f_name,sname="VoiceandAccountability")
    get_DataFrame(f_name, sname="Political StabilityNoViolence")
    get_DataFrame(f_name, sname="GovernmentEffectiveness")
    get_DataFrame(f_name, sname="RegulatoryQuality")
    get_DataFrame(f_name, sname="RuleofLaw")
    get_DataFrame(f_name, sname="ControlofCorruption")
    writer.save()
    os.remove(f_name)




if __name__ == "__main__":
    sys.exit(main())