# Dictionary
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered, changeable and do not allow duplicates.

#Dictionaries are written with curly brackets, and have keys and values

thisdict={
    "brand" : "Ford",
    "model" : "Mustang",
    "year"  : 1999
}

print(thisdict)

# Dictionary items are ordered, changeable, and do not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

#Print the "brand" value of the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#Duplicate values will overwrite existing values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
#value update kora jabe

print(thisdict)

#To determine how many items a dictionary has, use the len() function
print(len(thisdict))


#It is also possible to use the dict() constructor to make a dictionary.

# Using the dict() method to make a dictionary:

thisdict = dict(name="John", age=36 , country="Norway")
print(thisdict)



# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.



