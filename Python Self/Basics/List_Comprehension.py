fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist=[]

for x in fruits:
    if "a" in x: #jodi list item er moddhe  a thake tahole append korbe
        newlist.append(x)
    
print(newlist)

newlist1=[x for x in fruits if "a" in x] #short form of above loop
print(newlist1)

#newlist = [expression for item in iterable if condition == True]



#Set the values in the new list to upper case
newlist = [x.upper() for x in fruits]

#Set all values in the new list to 'hello':

newlist = ['hello' for x in fruits]

#"Return the item if it is not banana, if it is banana return orange".
print(newlist)
newlist = [x if x != "banana" else "orange" for x in fruits] #bujhi nai
print(newlist)




