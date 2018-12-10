import numpy as np

a=np.array([1,2,3,4])
b=np.array([2,3,4,5])

print(a+b)      #[3 5 7 9]
print(a-b)      #[-1 -1 -1 -1]
print(a*2)      #[2 4 6 8]
print(a**2)     #[ 1  4  9 16]
print(a*b)      #[ 2  6 12 20]

print("transpose example -------------------------------")
c=np.array([[1,2,3],[4,5,6]])
d=np.array([[2,3,4],[5,6,7]])
print("before --------")
print(d)
print("after --------")
d=d.transpose()
print(d)
print("matris c*d -----------------------")
print(c.dot(d))

print("numpy extra example -------------------")
print(a.sum())                      # 1+7+3+4+13+5=33
print(a.max())                      # 13
print(a.min())                      # 1
print(np.exp(a))
print(np.random.random((3,3)))      # get number data between 0 and 1

print("numpy extra math example")
a=np.array([1,4,9,16])
print(a+a)                          # [ 2  8 18 32]
print(np.add(a,a))                  # [ 2  8 18 32]
print(np.sqrt(a))                   # [1. 2. 3. 4.]
print(np.square(a))                 # [  1  16  81 256]

a=np.array([[1,2,3,4,5,6],[1,7,3,4,13,5]])
print(a.sum())              # 54
print(a.sum(axis=0))        # [ 2  9  6  8 18 11]   get summation on coloum
print(a.sum(axis=1))        # [21 33]               get summation on row