dic={
    "turkey":90,
    "germany":70,
    "england":83,
    "spaing":16,
    "italy":54
}
print(dic.keys())                           # dict_keys(['turkey', 'germany', 'england', 'spaing', 'italy'])
print(dic.values())                         # dict_values([90, 70, 83, 16, 54])

print("turkey : ",dic.get("turkey"))        # turkey :  90
print("italy : ",dic.get("italy"))          # spaing :  54
dic["italy"]=66
print("italy : ",dic.get("italy"))          # spaing :  66

dic.pop("england")
print(dic.keys())                   # dict_keys(['turkey', 'germany', 'spaing', 'italy'])


# ------------------------------------------------------------------------------

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(dict1.items())                        # dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])

# Double each value in the dictionary
double_dict1 = {k:v*2 for (k,v) in dict1.items()}
print(double_dict1)                         # {'a': 2, 'b': 4, 'c': 6, 'd': 8, 'e': 10}


double_dict1 = {k:v*v for (k,v) in dict1.items()}
print(double_dict1)                         # {'a': 1, 'b': 4, 'c': 9, 'd': 16, 'e': 25}