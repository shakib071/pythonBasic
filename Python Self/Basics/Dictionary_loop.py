
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#You can loop through a dictionary by using a for loop.

#Print all key names in the dictionary, one by one:

for x in thisdict:
    print(x) #only prints keys not value

#Print all values in the dictionary, one by one:

for x in thisdict:
  print(thisdict[x])

#You can also use the values() method to return values of a dictionary:

for x in thisdict.values():
  print(x)

# You can use the keys() method to return the keys of a dictionary:

for x in thisdict.keys():
  print(x)

#Loop through both keys and values, by using the items() method:

for x,y in thisdict.items():
   print(x,y)
