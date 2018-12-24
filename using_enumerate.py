liste = ["Java", "C#", "C", "Dijango","Spring"]

sonuç = list()
i = 0
for a in liste:
    sonuç.append((i, a))
    i += 1
print(sonuç)        #[(0, 'Java'), (1, 'C#'), (2, 'C'), (3, 'Dijango'), (4, 'Spring')]

result=list(enumerate(liste))
print(result)       # [(0, 'Java'), (1, 'C#'), (2, 'C'), (3, 'Dijango'), (4, 'Spring')]


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