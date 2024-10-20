class Phone:
    price=19000
    colour='Blue'
    brand='Samsung'


my_phone=Phone()
print(my_phone)
print(my_phone.brand)
print(my_phone.colour)
print(my_phone.price)

class Person:
  def __init__(self, name, age):#constractor
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


#The string representation of an object WITH the __str__() function:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self): #func inside class called method
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

#You can delete objects by using the del keyword


class Person:
  pass #if we dont need any content
# we cant put empty



