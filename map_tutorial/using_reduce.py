from functools import reduce

# usiing reduce
red=reduce(lambda x,y : x + y , [12,18,20,10])
print(red)          # 60
red=reduce(lambda x,y : x + y , [1,2,3,4])
print(red)          # 10
red=reduce(lambda x,y : x * y , [1,2,3,4,5])
print(red)          # 120
red=reduce(lambda x,y : x * y , [3,4,5,10])
print(red)          # 600

max=max([1,2,3,4,5,6])
print(max)          # 6

# reduce ile max fonksiyonu
def maksimum(x,y):
    if (x > y):
        return x
    else:
        return y

red=reduce(maksimum, [-2,1,100,35,32])
print(red)          # 100