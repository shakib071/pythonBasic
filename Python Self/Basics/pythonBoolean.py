print(5>3)
print(bool("Hello")) #true
print(bool(23))

#Any list, tuple, set, and dictionary are True, except empty ones.
# Almost any value is evaluated to True if it has some sort of content.

# Any string is True, except empty strings.

# Any number is True, except 0.
# In fact, there are not many values that evaluate to False, except empty values,
# such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.

class myclass():
    def __len__(self):
        return 0
myobj=myclass()
print(bool(myobj))

#One more value, or object in this case, evaluates to False,
# and that is if you have an object that is made from a class with a __len__ function that returns 0 or False

# Check if an object is an integer or not

x = 200
print(isinstance(x, int)) # is it instance or checks is x a instance of int type

