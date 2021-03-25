# %%
import pandas as pd 
import numpy as np 

projects_data = pd.read_excel("Final_Projects_2020_gaWC.xlsx",na_values='')
projects_data.shape

# %%
projects_data['LT_debt']
# %%
# Remove n.a. from columns
for c in projects_data.columns:
    projects_data[c].loc[(projects_data[c] =='n.a.')] = np.nan

# there is x variable in cdh
projects_data['cdh'].loc[(projects_data['cdh'] =='x')] = np.nan

# %%
# Remove [] from bmi data
# first get all bmi columns
bmi_cols = projects_data.filter(regex=r'^bmi', axis=1).columns
for c in bmi_cols:
    projects_data[c] = projects_data[c].loc[projects_data[c].notna()].apply(lambda x: x.split(' ')[0])
    
# %%
gc_cols = projects_data.filter(regex=r'^GC', axis=1).columns
# %%
for c in gc_cols:
    projects_data[c].loc[(projects_data[c].isna())] = 0

gawc_cols = projects_data.filter(regex=r'GaWC', axis=1).columns
for c in gawc_cols:
    projects_data[c].loc[(projects_data[c].isna())] = 0
projects_data.to_excel("Final_projects_2020_corrected.xlsx")
# %%
