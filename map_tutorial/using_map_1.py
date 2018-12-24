# using map and list
def double(x):
    return x*2

maap=map(double,[1,2,3])

liste=list(maap)
print(liste)            # [2, 4, 6]

#---------------------------------------------------------------------
# using map, list and set
def calculateSquare(n):
  return n*n

numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)        # {16, 1, 4, 9}

#---------------------------------------------------------------------
numbers = ( 2, 3, 4, 5, 6)
result = map(calculateSquare, numbers)

# converting map object to list
liste=list(result)
print(liste)           # [4, 9, 16, 25, 36]