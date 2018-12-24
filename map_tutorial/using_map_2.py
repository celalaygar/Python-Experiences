# using map list and lambda
liste=list(map(lambda x: x**2,[1,2,3,4,5]))

print(liste)            # [1, 4, 9, 16, 25]

#---------------------------------------------------------------------
liste1=[1,2,3]
liste2=[4,5,6]
liste3=[5,6,7,8,9]

liste=list(map(lambda x,y:x*y,liste1,liste2))
print(liste)            # [4, 10, 18]

liste=list(map(lambda x,y,z:x*y*z,liste1,liste2,liste3))
print(liste)            # [20, 60, 126]