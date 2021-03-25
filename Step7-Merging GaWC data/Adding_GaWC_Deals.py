import pandas as pd 
import numpy as np 


gc_d = pd.read_excel("GaWC Alpha Global Cities.xlsx",sheet_name="Intersection",header=None)

gc_d.columns = gc_d.iloc[1]
gc_d = gc_d[2:]


deals = pd.read_excel("Final_Deals_2020.xlsx")
deals.shape

# Check for City names different in GC and deals


list( set(gc_d['City']) - set(deals['icity']) )
list( set(gc_d['Country']) - set(deals['icoun']) )


list( set(gc_d['City']) - set(deals['tcity']) )
list( set(gc_d['Country']) - set(deals['tcoun']) )


# Country like Russia,UAE and U.S is not matching
# Deals have United Arab Emirates
# United States of America
# Russian Federation
deals[deals['icoun'].str.contains("United",na=False)]['icoun']

# Manually change the country names to match with Deals

gc_d['Country'].mask(gc_d['Country'] == 'Russia', 'Russian Federation', inplace=True)
gc_d['Country'].mask(gc_d['Country'] == 'UAE', 'United Arab Emirates', inplace=True)
gc_d['Country'].mask(gc_d['Country'] == 'U.S.', 'United States of America', inplace=True)

list( set(gc_d['City']) - set(deals['icity']) )
list( set(gc_d['Country']) - set(deals['icoun']) )

list( set(gc_d['City']) - set(deals['tcity']) )
list( set(gc_d['Country']) - set(deals['tcoun']) )


# Rule to create new columns
"""
Deals	
i_GaWC_int	From Intersection sheet. 1-when investor city categorized as alpha +, alpha or alpha -; 0 - otherwise
i_GaWC_int_fine	From Intersection sheet. 1-when investor city categorized as alpha ++, 2 - when investor city categorized as alpha+, 3-when investor city categorized as alpha, 4-when investor city categorized as alpha-, 0- otherwise
t_GaWC_int	From Intersection sheet. 1-when target city categorized as alpha +, alpha or alpha -; 0 - otherwise
t_GaWC_int_fine	From Intersection sheet. 1-when target city categorized as alpha ++, 2 - when target city categorized as alpha+, 3-when target city categorized as alpha,4- when target city categorized as alpha-, 0- otherwise

"""

# For Investor Country 
gc_d["i_GaWC_int"] = np.where(gc_d.Category.isin(['Alpha++','Alpha+','Alpha','Alpha-']),1,0)
conditions = [
    (gc_d['Category'] =='Alpha++'),
    (gc_d['Category'] =='Alpha+'),
    (gc_d['Category'] =='Alpha'),(gc_d['Category'] =='Alpha-'),
    ((gc_d['Category']!='Alpha++') & (gc_d['Category']!='Alpha+')&(gc_d['Category']!='Alpha')&(gc_d['Category']!='Alpha-'))
    ]
values=[1,2,3,4,0]
gc_d["i_GaWC_int_fine"] = np.select(conditions, values)


# Merge in deals based on Investor City and Country
gc_d_s = gc_d[['City','Country','i_GaWC_int','i_GaWC_int_fine']]
gc_d_s.columns = ['icity_new','icoun','i_GaWC_int','i_GaWC_int_fine']

imerge = pd.merge(deals, gc_d_s,how="left" ,on=["icity_new","icoun"]) 
list(imerge)

# merge for target country
gc_d_s.columns = ['tcity_new','tcoun','t_GaWC_int','t_GaWC_int_fine']
tmerge = pd.merge(imerge, gc_d_s,how="left" ,on=["tcity_new","tcoun"]) 

# For the Union Data

gc_u = pd.read_excel("GaWC Alpha Global Cities.xlsx",sheet_name="Union",header=None)
gc_u.columns = gc_u.iloc[1]
gc_u = gc_u[2:]

list( set(gc_u['City']) - set(tmerge['icity']) )
list( set(gc_u['Country']) - set(tmerge['icoun']) )


list( set(gc_u['City']) - set(tmerge['tcity']) )
list( set(gc_u['Country']) - set(tmerge['tcoun']) )

# ['Russia', 'UAE', 'Korea', 'U.S.'] are different

tmerge[tmerge['icoun'].str.contains("Korea",na=False)]['icoun']

# Manually change the country names to match with Deals

gc_u['Country'].mask(gc_u['Country'] == 'Russia', 'Russian Federation', inplace=True)
gc_u['Country'].mask(gc_u['Country'] == 'UAE', 'United Arab Emirates', inplace=True)
gc_u['Country'].mask(gc_u['Country'] == 'U.S.', 'United States of America', inplace=True)
gc_u['Country'].mask(gc_u['Country'] == 'Korea', 'Republic of Korea', inplace=True)


list( set(gc_u['City']) - set(tmerge['icity']) )
list( set(gc_u['Country']) - set(tmerge['icoun']) )

# Rules for creating new variables
"""
i_GaWC_un	From Union sheet. 1-when investor city categorized as alpha +, alpha or alpha -; 0 - otherwise
i_GaWC_un_fine	From Union sheet. 1-when investor city categorized as alpha ++, 2 - when investor city categorized as alpha+, 3-when investor city categorized as alpha, 4-when investor city categorized as alpha-, 0- otherwise
t_GaWC_un	From Union sheet. 1-when target city categorized as alpha +, alpha or alpha -; 0 - otherwise
t_GaWC_un_fine	From Union sheet. 1-when target city categorized as alpha ++, 2 - when target city categorized as alpha+, 3-when target city categorized as alpha,4- when target city categorized as alpha-, 0- otherwise
"""
gc_u["i_GaWC_un"] = np.where(gc_u.Category.isin(['Alpha++','Alpha+','Alpha','Alpha-']),1,0)
conditions = [
    (gc_u['Category'] =='Alpha++'),
    (gc_u['Category'] =='Alpha+'),
    (gc_u['Category'] =='Alpha'),(gc_u['Category'] =='Alpha-'),
    ((gc_u['Category']!='Alpha++') & (gc_u['Category']!='Alpha+')&(gc_u['Category']!='Alpha')&(gc_u['Category']!='Alpha-'))
    ]
values=[1,2,3,4,0]
gc_u["i_GaWC_un_fine"] = np.select(conditions, values)

# Merge Union in deals based on Investor City and Country
gc_u_s = gc_u[['City','Country','i_GaWC_un','i_GaWC_un_fine']]
gc_u_s.columns = ['icity_new','icoun','i_GaWC_un','i_GaWC_un_fine']

iu_merge = pd.merge(tmerge, gc_u_s,how="left" ,on=["icity_new","icoun"]) 

# target country
gc_u_s.columns = ['tcity_new','tcoun','t_GaWC_un','t_GaWC_un_fine']
tu_merge = pd.merge(iu_merge, gc_u_s,how="left" ,on=["tcity_new","tcoun"]) 

tu_merge.to_csv("Final_Deals_2020_gaWC.csv")
tu_merge.to_excel("Final_Deals_2020_gaWC.xlsx")