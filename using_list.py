
liste=[1,2,3,4,5,6]
liste2=["ali","veli"]
value=liste2[1]

print(type(liste))                  # <class 'list'>
print(type(liste2))                 # <class 'list'>
print(type(value))                  # <class 'str'>

liste3=[12,2,31,4,11,61,2,4,11,11,22,13,1]
print("liste3 : ",liste3)           # liste3 :  [12, 2, 31, 4, 11, 61, 2, 4, 11, 11, 22, 13, 1]

liste3.append(7)
print("liste3 : ",liste3)           # liste3 :  [12, 2, 31, 4, 11, 61, 2, 4, 11, 11, 22, 13, 1, 7]

liste3.remove(2)
print("liste3 : ",liste3)           # liste3 remove :  [12, 31, 4, 11, 61, 2, 4, 11, 11, 22, 13, 1, 7]

liste3.reverse()
print("liste3 : ",liste3)           # liste3 reverse :  [7, 1, 13, 22, 11, 11, 4, 2, 61, 11, 4, 31, 12]

liste3.sort()
print("liste3 : ",liste3)           # liste3 sort :  [1, 2, 4, 4, 7, 11, 11, 11, 12, 13, 22, 31, 61]

print("liste3 : ",liste3.count(4))  # liste3 count :  2




