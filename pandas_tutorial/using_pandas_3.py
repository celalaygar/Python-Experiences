import pandas as pd


dictionary = {"NAME":["ali","cengiz","kavlak","veli","kenan silah","hilal mert","ayse katı","evren cemre", "gül ela"],
                "AGE":[15,16,17,33,45,66,23,35,11],
                "SALARY": [100,150,240,350,110,220,133,231,143]}

dataFrame1 = pd.DataFrame(dictionary)

print(dataFrame1["AGE"])                 # get all age data
print(dataFrame1.AGE)                    # get all age data
print(dataFrame1.loc[:,"AGE"])           # get all age data
print(dataFrame1.loc[2:5,"AGE"])         # get all age data between index 2 and 5
print(dataFrame1.loc[2:5,"AGE":"SALARY"])         # get all age and salary datas between index 2 and 5

print(dataFrame1.iloc[:,2])              # get all SALARY data



