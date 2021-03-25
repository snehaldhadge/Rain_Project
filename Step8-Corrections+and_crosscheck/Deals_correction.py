# %%
import pandas as pd 
import numpy as np 

deals_data = pd.read_excel("Final_Deals_2020.xlsx",na_values='')
deals_data.shape

# %%
deals_data['LT_debt']
# %%
# Remove n.a. from columns
for c in deals_data.columns:
    deals_data[c].loc[(deals_data[c] =='n.a.')] = np.nan

# there is x variable in cdh
deals_data['cdh'].loc[(deals_data['cdh'] =='x')] = np.nan

# %%
# Remove [] from bmi data
# first get all bmi columns
bmi_cols = deals_data.filter(regex=r'^bmi', axis=1).columns
for c in bmi_cols:
    deals_data[c] = deals_data[c].loc[deals_data[c].notna()].apply(lambda x: x.split(' ')[0])
    
# %%
gc_cols = deals_data.filter(regex=r'^GC', axis=1).columns
# %%
for c in gc_cols:
    deals_data[c].loc[(deals_data[c].isna())] = 0

deals_data.to_excel("Final_Deals_2020.xlsx")
# %%
