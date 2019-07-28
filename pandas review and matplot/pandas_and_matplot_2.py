import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("iris.csv")

df1 = df.drop(["Id"],axis=1)

df1.plot()
plt.show()

# show specific  values of setosa of Species 
setosa = df[df.Species == "Iris-setosa"]
# show specific  values of Iris-versicolor of Species 
versicolor = df[df.Species == "Iris-versicolor"]
# show specific  values of Iris-virginica of Species 
virginica = df[df.Species == "Iris-virginica"]

plt.plot(setosa.Id,setosa.PetalLengthCm,color="yellow",label= "setosa")
plt.plot(versicolor.Id,versicolor.PetalLengthCm,color="green",label= "versicolor")
plt.plot(virginica.Id,virginica.PetalLengthCm,color="blue",label= "virginica")
# show label on the graphic
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.legend()
plt.show()


df1.plot(grid=True,alpha= 0.9)
plt.show()

