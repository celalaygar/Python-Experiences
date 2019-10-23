# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("random-forest-regression-dataset.csv",sep = ";",header = None)
x = df.iloc[:,0].values.reshape(-1,1)
y = df.iloc[:,1].values.reshape(-1,1)
 
from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(n_estimators = 100, random_state = 42)
rf.fit(x,y)
y_head = rf.predict(x)

print(x)                                # x values
from sklearn.metrics import r2_score
print("r_score: ", r2_score(y,y_head))  # r_score:  0.9798724794092587
