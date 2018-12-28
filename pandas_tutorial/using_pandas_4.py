import pandas as pd


dictionary = {"NAME":["ali","cengiz","kavlak","veli","kenan silah","hilal mert","ayse katı","evren cemre", "gül ela"],
                "AGE":[75,16,17,33,45,66,23,35,11],
                "SALARY": [100,110,133,143,150,220,231,240,350]}

dataFrame1 = pd.DataFrame(dictionary)

# filter example - 1    ----------------------------------------------------------------------------
filtre1 = dataFrame1.SALARY > 200               # get all data about salary>200
filtrelenmis_data = dataFrame1[filtre1]
print(filtrelenmis_data)

# filter example - 2    ----------------------------------------------------------------------------
filtre2 = dataFrame1.AGE <20
filtrelenmis_data=dataFrame1[filtre1 & filtre2] # get all data about salary>200 and age<20
print(filtrelenmis_data)

# filter example - 3    ----------------------------------------------------------------------------
print(dataFrame1[dataFrame1.AGE > 60])          # get all data about age>60


