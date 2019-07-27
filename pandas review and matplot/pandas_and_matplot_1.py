import pandas as pd

df = pd.read_csv("iris.csv")

# which columns has this csv file
print(df.columns)           #output : Index(['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species'], dtype='object')


# show columns details

print(df.Id)
#print(df.SepalLengthCm)
#print(df.SepalWidthCm)
#print(df.PetalLengthCm)
#print(df.PetalWidthCm)
#print(df.Species)


print(df.Species.unique())   #output : ['Iris-setosa' 'Iris-versicolor' 'Iris-virginica']
print(df.info())

# show count mean std min max values for current columns
print(df.describe())


# show count mean std min max values for current columns
setosa = df[df.Species == "Iris-setosa"]
# show Iris-setosa of Species column
print(setosa)

# show count mean std min max values for Iris-setosa of Species column
print(setosa.describe())






