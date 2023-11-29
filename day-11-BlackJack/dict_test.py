# Dict
dict1 = {
    "a": 1,
    "b": 2
}
dict2 = dict1

dict1["b"] = 3
print("Equal sign")
print(dict1)
print(dict2)

dict2 = dict1.copy()
dict1["b"] = 2
print("Without Equal sign")
print(dict1)
print(dict2)

# List
dict1 = [1, 2, 3, 4, 5]
dict2 = dict1

dict1[-1] = 3
print("Equal sign")
print(dict1)
print(dict2)

dict2 = dict1.copy()
dict1[-1] = 5
print("Without Equal sign")
print(dict1)
print(dict2)
