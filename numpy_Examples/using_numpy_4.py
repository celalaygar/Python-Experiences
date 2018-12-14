import numpy as np

array = np.array([1,2,3,4,5,26,55,22,11,33,25,71,24])
print(array[0])         # 1
print(array[0:3])       # [1 2 3]
print(array[2:7])       # [ 3  4  5 26 55]

reverse_array=array[::-1]
print(reverse_array)    # [24 71 25 33 11 22 55 26  5  4  3  2  1]

print("2 dimension array ------------------------------------")
array=np.array([[1,2,3,4,5],[6,7,8,9,0]])
print(array[1,2])       # 8
print(array[:,2])       # [3 8]
print(array[:,4])       # [5 0]
print(array[1,:])       # [6 7 8 9 0]
print(array[1,2:4])     # [8 9]
print(array[:,-1])      # [5 0]
print(array[-1,:])      # [6 7 8 9 0]
print(array[0,:])       # [1 2 3 4 5]

reverse_array=array[::-1]
print(reverse_array)








