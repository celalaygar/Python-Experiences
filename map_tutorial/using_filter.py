filt=filter(lambda x : x % 2 == 0, [1,2,3,4,5,6,7,8,9,10])
# Çift olan sayılar
liste=list(filt)
print(liste)            # [2, 4, 6, 8, 10]


def asal_mi(x):
    i = 2
    if (x == 1):
        return False # Asal değil
    elif(x == 2):
        return True # Asal sayı
    else:
        while((x/2)>=i):
            if (x % i == 0):
                return False # Asal Değil
            i += 1
    return True

print(asal_mi(15))          # False
print(asal_mi(22))          # False
print(asal_mi(23))          # True

filt=filter(asal_mi,range(1,15))
liste=list(filt)            # 1 den 15' e kadar olan asal sayılar.
print(liste)                # [2, 3, 5, 7, 11, 13]

filt=filter(asal_mi,range(15,25))
liste=list(filt)            # 15 den 25' e kadar olan asal sayılar.
print(liste)                # [17, 19, 23]

filt=filter(asal_mi,range(25,50))
liste=list(filt)            # 25 den 50' e kadar olan asal sayılar.
print(liste)                # [29, 31, 37, 41, 43, 47]

