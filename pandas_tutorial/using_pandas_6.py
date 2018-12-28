import pandas as pd
import numpy as np

dictionary = {"NAME":["ali","cengiz","kavlak","veli","kenan silah","hilal mert","ayse katı","evren cemre", "gül ela"],
                "AGE":[75,16,17,33,45,66,23,35,11],
                "SALARY": [100,110,133,143,150,220,231,240,350]}

dataFrame1 = pd.DataFrame(dictionary)
print(dataFrame1.columns)               #Index(['NAME', 'AGE', 'SALARY'], dtype='object
print(len(dataFrame1.NAME[2]))          # 6
print(len(dataFrame1.NAME[7]))          # 11
print(len(dataFrame1.NAME[5]))          # 10
print(len(dataFrame1.columns))          # 3
print(len(dataFrame1.SALARY))           # 9

data1 = dataFrame1.head()
data2 = dataFrame1.tail()
print(data1)                            # get first 5 index row data
print(data2)                            # get last 5 index row data

salary = dataFrame1.SALARY
age = dataFrame1.AGE
print(salary)                           # get all salary
print(age)                              # get all age


dataFrame1["result"] = [ each*2 for each in dataFrame1.AGE]
print(dataFrame1.result)                # get all age as 2 x age


def multiply(age):
    return age * 3

dataFrame1["multiply"] = dataFrame1.SALARY.apply(multiply)
print(dataFrame1.multiply)                # get all age as 3 x SALARY


result=dataFrame1.columns = [ each.lower() for each in dataFrame1.columns]
print(result)                           # ['name', 'age', 'salary']