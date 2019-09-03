"""Sort a dictionary according to values"""

dictionary = {"key1":8,"key2":4,"key3":2,"key4":1,"key5":6,"key6":0}
dict2=sorted(dictionary.items(), key=lambda item : item[1])
print(dict2)