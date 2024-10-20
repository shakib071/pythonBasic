thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

for i in range(len(thislist)):
  print(thislist[i])


i=0
while i<len(thislist):
  print(thislist[i])
  i+=1


#A short hand for loop that will print all items in a list

[print(x) for x in thislist] #important (New)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist=[]

for x in fruits:
    if "a" in x: #jodi list item er moddhe  a thake tahole append korbe
        newlist.append(x)
    
print(newlist)

newlist1=[x for x in fruits if "a" in x] #short form of above loop
print(newlist1)

#newlist = [expression for item in iterable if condition == True]
