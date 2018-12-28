import pandas as pd
import numpy as np

dictionary = {"NAME":["ali","cengiz","kavlak","veli","kenan silah","hilal mert","ayse katı","evren cemre", "gül ela"],
                "AGE":[75,16,17,33,45,66,23,35,11],
                "SALARY": [100,110,133,143,150,220,231,240,350]}

dataFrame1 = pd.DataFrame(dictionary)

avarage_salary = dataFrame1.SALARY.mean()
print(avarage_salary)                    # 186.33333333333334

# how to control which salary is high  or low from avarage_salary
dataFrame1["salary_rate"] = ["low" if avarage_salary > each else "high" for each in dataFrame1.SALARY]
print(dataFrame1["salary_rate"] )


# how to control which salary is high  or low from salary = 250
dataFrame1["salary_rate"] = ["low" if 250> each else "high" for each in dataFrame1.SALARY]
print(dataFrame1.salary_rate )


# how to control which age is younger  or older than age = 20
dataFrame1["age_rate"] = ["younger" if 20> each else "older" for each in dataFrame1.AGE]
print(dataFrame1.age_rate )