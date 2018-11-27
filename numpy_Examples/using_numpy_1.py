import numpy as np

a = np.arange(18).reshape(3, 6)

print (a)
print ("shape       : ",a.shape)
print ("ndim        : ",a.ndim)
print ("dtype.name  : ",a.dtype.name)
print ("itemsize    : ",a.itemsize)
print ("size        : ",a.size)
print ("type        : ",type(a))


b = np.array([6, 7, 8, 9, 10])
print (b)
print ("type        : ",type(b))