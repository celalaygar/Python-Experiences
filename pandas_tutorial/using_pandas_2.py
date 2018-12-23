import pandas as pd




dictionary = {"NAME":["ali","cengiz","kavlak","veli","kenan silah","hilal mert","ayse katı","evren cemre", "gül ela"],
                "AGE":[15,16,17,33,45,66,23,35,11],
                "SALARY": [100,150,240,350,110,220,133,231,143]}

dataFrame1 = pd.DataFrame(dictionary)


print("Get Coloumn********************************************************")
print(dataFrame1.columns)           # get all column's name
print(dataFrame1.keys())            # get all column's name
print("Get specific data********************************************************")
print(dataFrame1.get("NAME"))       # get all  names
print(dataFrame1.get("AGE"))        # get all  ages
print(dataFrame1.get("SALARY"))     # get all  salary
print("*get info *******************************************************")
print(dataFrame1.info())


print("get column data type ********************************************************")

print(dataFrame1.dtypes)

print(dataFrame1.describe())                # numeric feature = columns (age,maas)
print(dataFrame1.count())                   # get all column's count
