# what is all method -------------------------------------------------------------------
def all_1(liste):
    for i in liste:
        if not i:
            return False
    return True

liste = [True,False,True,False,True]
print(all_1(liste))               # False
liste = [True,True,True]
print(all_1(liste))               # True
liste = [False,False,False]
print(all_1(liste))               # False

liste = [1,21,32,4,55]
print(all_1(liste))               # True
liste = [1,21,32,4,55,0]
print(all_1(liste))               # False

#using all -------------------------------------------------------------------
liste = [True,False,True,False,True]
print(all(liste))               # False,

liste = [1,2,3,4,5]
print(all(liste))               # True


print("--------------------------------")
# what is any method -------------------------------------------------------------------
def any_1(liste):
    for i in liste:
        if i:
            return True
    return False


liste = [True,False,True,False,True]
print(any_1(liste))               # True,

liste = [0,0,0,0,0,0,0] # Bütün değerler False , 0 = False
print(any_1(liste))               # False,

# using any method ------------------------------------------------------------------------
liste = [True,False,True,False,True]
print(any(liste))                 # True

liste = [0,0,0,0,0,0,0]
print(any(liste))                 # False