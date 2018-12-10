import numpy as np

a = np.array([1,2,3,4,5,26,55,22,11,33,25,71,
              24,59,7,22,14,12,16,31,33,52,57,61])

print(a.shape)
print("shape : ",a)
print("reshape with b ---------------------------------")
b=a.reshape(2,12)
print(b.shape)
print("shape : ",b)
print("array1 ---------------------------------")
array1=np.array( [
     [1,2,3,4,],
    [52,3,44,22],
    [44,22,1,2],
    [33,21,55,43],
    [22,31,66,53]
])
print("shape : ",array1.shape)
print(array1)
print("zero_array ---------------------------------")
zero_array=np.zeros((2,5))
print("shaep : ",zero_array)
print(zero_array)
zero_array[0,0]=5
zero_array[1,4]=5
print(zero_array)

print("numpy basic increment example --------------------------")
a=np.arange(10,20,1.5)
print(a)
a=np.linspace(10,20,5)
print(a)