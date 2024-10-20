#Change Tuple Values

# Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.
# Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple

x = ("apple", "banana", "cherry")
y=list(x)

y[1]="kiwi"
x=tuple(y)
print(x)

# Add Items

# Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.
# 1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple

#Convert the tuple into a list, add "orange", and convert it back into a tuple

thistuple = ("apple", "banana", "cherry")
y=list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

# Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many),
#  create a new tuple with the item(s), and add it to the existing tuple

thistuple=("apple","banana","cherry")
y=("orangee",)
thistuple+=y
print(thistuple)


#Remove Items

thistuple = ("apple", "banana", "cherry")
y=list(thistuple)
y.remove("apple")
thistuple=tuple(y)
print(thistuple)


# The del keyword can delete the tuple completely:

# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists






