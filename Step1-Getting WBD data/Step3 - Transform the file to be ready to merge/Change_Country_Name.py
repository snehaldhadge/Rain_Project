import pandas as pd
import numpy as np

def Change_Country_Names(c_name):
    cname_tobe_changed = { 'Bahamas, The':'Bahamas',
                           "Cote d'Ivoire":"Côte d'Ivoire",
                           "Congo, Dem. Rep.":'Democratic Republic of the Congo',
                           'Congo, Rep.':'Congo',
                           'Cabo Verde':'Cape Verde',
                           'Curacao':'Curaçao',
                           'Egypt, Arab Rep.':'Egypt',
                           'Micronesia, Fed. Sts.':'Federated States of Micronesia',
                           'Gambia, The':'Gambia',
                           'Guinea-Bissau':'Guinea Bissau',
                           'Hong Kong SAR, China':'Hong Kong',
                           'Iran, Islamic Rep.':'Islamic Republic of Iran',
                           'St. Kitts and Nevis':'Saint Kitts and Nevis',
                           'Korea, Rep.':'Republic of Korea',
                           'Lao PDR':"Lao People's Democratic Republic",
                           'St. Lucia':'Saint Lucia',
                           'Macao SAR, China':'Macao',
                           'Moldova':'Republic of Moldova',
                           'North Macedonia':'Macedonia (FYROM)',
                           'Myanmar':'Myanmar/Burma',
                           'Korea, Dem. People’s Rep.':"Democratic People's Republic of Korea",
                           'Sao Tome and Principe':'São Tome and Principe',
                           'Tanzania':'United Republic of Tanzania',
                           'United States':'United States of America',
                           'St. Vincent and the Grenadines':'Saint Vincent and the Grenadines',
                           'British Virgin Islands':'Virgin Islands (British)',
                           'Yemen, Rep.':'Yemen'
                           }
    for i in range(len(c_name)):
        if (c_name[i] in cname_tobe_changed):
            c_name[i]=cname_tobe_changed[c_name[i]]

    return c_name


