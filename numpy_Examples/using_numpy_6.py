import numpy as np

array1=np.array([[-1,-2,-3],[-4,-5,-6],[-7,-8,-9]])
array2=np.array([[1,2,3],[4,5,6],[7,8,9]])

print(array1)
print(array2)

print("vertical merging --------------------------")
array3=np.vstack((array1,array2))
print(array3)


print("horizontal merging --------------------------")
array4=np.hstack((array1,array2))
print(array4)




