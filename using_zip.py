liste1 = [1,2,3,4,5]
liste2 = [6,7,8,9,10,11]

sonuç = list()
i = 0
while (i < len(liste1) and i < len(liste2)):
    sonuç.append((liste1[i], liste2[i]))

    i += 1
print(sonuç)            # [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]


#using zip
zip1=zip(liste1,liste2)
liste=list(zip1)
print(liste)            # [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]


liste1 = [1,2,3,4]
liste2 = [5,6,7,8]
liste3 = ["Spring","Hibernate","Java","Javascript","Python"]

liste=list(zip(liste1,liste2,liste3))
print(liste)            # [(1, 5, 'Spring'), (2, 6, 'Hibernate'), (3, 7, 'Java'), (4, 8, 'Javascript')]


# Sözlükleri zipleyelim.
sözlük1 = {"Pc":11,"Tv":22,"Radio":33}
sözlük2 = {"Ali":0,"Veli":1,"Niyazi":2}

liste=list(zip(sözlük1,sözlük2)) # Anahtarlar eşleşti.
print(liste)            # [('Pc', 'Ali'), ('Tv', 'Veli'), ('Radio', 'Niyazi')]

liste=list(zip(sözlük1.values(),sözlük2.values())) # Değerler eşleşti
print(liste)            # [(11, 0), (22, 1), (33, 2)]
