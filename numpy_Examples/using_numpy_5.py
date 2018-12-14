import numpy as np

array=np.array([[0,1,2],[3,4,5],[6,7,8]])
print(array)
print("1 dimension -----------------------")
array1=array.ravel()
print(array1)
print("3 dimension -----------------------")
array2=array1.reshape(3,3)
print(array2)
print("transpose -----------------------")

array3=array2.T
print(array3)

array4=array.transpose()
print(array4)

print("how to learn dimension of array -----------------------------")
print(array.shape)

print("array resize -----------------------------")
array=np.array([[1,2,3,4],[5,6,7,8]])
array.resize(4,2)
print(array)

print("array reshape -----------------------------")
print(array.reshape(2,4))
print(array)


