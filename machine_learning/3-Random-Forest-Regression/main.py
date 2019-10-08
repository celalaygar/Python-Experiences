# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 14:44:19 2019

@author: aygar
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# C:\\Users\\aygar\\PycharmProjects\\Deneme\\Ai_experiency\\machine_learning\\3-Random-Forest-Regression\\
df = pd.read_csv("random-forest-regression-dataset.csv",sep = ";",header = None)

x = df.iloc[:,0].values.reshape(-1,1)   # tüm satırları al ve sadece 1. kolonu al
y = df.iloc[:,1].values.reshape(-1,1)   # tüm satırları al ve sadece 2. kolonu al


from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(n_estimators = 100, random_state = 42)

rf.fit(x,y)


x_ = np.arange(min(x),max(x),0.01).reshape(-1,1)
y_head = rf.predict(x_)
print("ok")

# visualize
plt.scatter(x,y,color="red")
plt.plot(x_,y_head,color="green")
plt.xlabel("tribun level")
plt.ylabel("ucret")
plt.show()
