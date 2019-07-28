import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("iris.csv")

df1 = df.drop(["Id"],axis=1)

# scatter plot example

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

# %% histogram

plt.scatter(setosa.PetalLengthCm,setosa.PetalWidthCm,color="red",label="setosa")
plt.scatter(versicolor.PetalLengthCm,versicolor.PetalWidthCm,color="green",label="versicolor")
plt.scatter(virginica.PetalLengthCm,virginica.PetalWidthCm,color="blue",label="virginica")
plt.legend()
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.title("scatter plot")
plt.show()

# show amount of PetalLengthCm of setosa on histogram
plt.hist(setosa.PetalLengthCm,bins= 20)
plt.xlabel("PetalLengthCm values")
plt.ylabel("frekans")
plt.title("hist")
plt.show()

# %% bar plot

import numpy as np

x = np.array([1,2,3,4,5,6,7])

y = x*2+5

plt.bar(x,y)
plt.title("bar plot for x and y")
plt.xlabel("x")
plt.ylabel("y")
plt.show()


x = np.array([1,2,3,4,5,6,7])
a = ["turkey","usa","arabia","bulgaria","vietnam","denmark","sirbia"]
y = x*2+5

plt.bar(a,y)
plt.title("bar plot")
plt.xlabel("x")
plt.ylabel("y")
plt.show()















