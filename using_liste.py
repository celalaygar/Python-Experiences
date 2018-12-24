
liste=[1,2,3,4,5,6]
liste2=["ali","veli"]
value=liste2[1]

print(type(liste))
print(type(liste2))
print(type(value))

liste3=[12,2,31,4,11,61,2,4,11,11,22,13,1]
print("liste3 : ",liste3)

liste3.append(7)
print("liste3 append : ",liste3)

liste3.remove(2)
print("liste3 remove : ",liste3)

liste3.reverse()
print("liste3 reverse : ",liste3)

liste3.sort()
print("liste3 sort : ",liste3)

print("liste3 count : ",liste3.count(4))

liste1= ["a", "b", "c", "d", "e", "f", "g"]
liste2=list()
liste3=list()
for index, eleman in enumerate(liste1):
    if (index % 2 == 1):
        liste2.insert(index,eleman)
    else:
        liste3.insert(index,eleman)

print(liste2)       # ['b', 'd', 'f']
print(liste3)       # ['a', 'c', 'e', 'g']

