import pandas as pd




dictionary = {"NAME":["ali","cengiz","kavlak","veli","kenan silah","hilal mert","ayse katı","evren cemre", "gül ela"],
                "AGE":[15,16,17,33,45,66,23,35,11],
                "SALARY": [100,150,240,350,110,220,133,231,143]}

dataFrame1 = pd.DataFrame(dictionary)
print("get all data-------------------------------------------------------------")
print(dataFrame1)
print("get first 5 data-------------------------------------------------------------")
head = dataFrame1.head()            #get first 5 data
print(head)
print("get first 3 data-------------------------------------------------------------")
head = dataFrame1.head(3)            #get first 3 data
print(head)
print("get last 5 data-------------------------------------------------------------")
tail = dataFrame1.tail()            #get last 5 data
print(tail)
print("get last 3 data-------------------------------------------------------------")
tail = dataFrame1.tail(3)            #get last 3 data
print(tail)
