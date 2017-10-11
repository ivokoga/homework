
# coding: utf-8

import pandas as pd
import csv
from sets import Set

# slcsp =pd.read_csv("slcsp.csv")
#
# zips =pd.read_csv("zips.csv")
#
# plans=pd.read_csv("plans.csv")
# plans = plans.loc[plans['metal_level'] == 'Silver']

#create one single table
# slcsp_zips = pd.merge(slcsp, zips, left_on ='zipcode', right_on='zipcode')
# slcsp_zips.info()


# for each zipcode in zips file search for the rate_areas in zips.csv
# with open('zips.csv') as zips_csv:
#     zips_reader = csv.DictReader(zips_csv)
#     for zip_row in zips_reader:
#         print(zip_row['zipcode'])

conjunto = Set()
#open file second low cost silver plan
with open('slcsp.csv') as slcsp_csv:
    slcsp_reader = csv.DictReader(slcsp_csv)
    for slcsp_row in slcsp_reader:
        print(slcsp_row['zipcode'])
        conjunto.add(slcsp_row['zipcode'])

print(len(conjunto))