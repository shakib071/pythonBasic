#string er moto data store kore
# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.
# Python has a built-in package called json, which can be used to work with JSON data.


import json

#If you have a JSON string, you can parse it by using the json.loads() method
#The result will be a Python dictionary.

#some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'#full dictionary na kintu

y=json.loads(x)

# the result is a Python dictionary:
print(y['age'])
print(y['name'])



#If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y=json.dumps(x)

# the result is a JSON string
print(y)


# You can convert Python objects of the following types, into JSON strings:

# dict
# list
# tuple
# string
# int
# float
# True
# False
# None


print(json.dumps({"name": "John", "age": 30})) #object print korbe
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


# When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

# Python -->	JSON
# dict  -->	Object
# list  -->	Array
# tuple  --> Array
# str -->	String
# int	Number
# float	Number
# True	true
# False	false
# None	null

#notion ay acea



#The json.dumps() method has parameters to make it easier to read the result

#The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.
# The json.dumps() method has parameters to make it easier to read the result:

#bujhi nai
#Use the indent parameter to define the numbers of indents

json.dumps(x, indent=4)

print(json.dumps(x, indent=4))

# Use the separators parameter to change the default separator

json.dumps(x, indent=4, separators=(". ", " = "))

print(json.dumps(x, indent=4, separators=(". ", " = ")))

json.dumps(x, indent=4, separators=("# ", " = "))

print(json.dumps(x, indent=4, separators=(". ", " = ")))

# Use the sort_keys parameter to specify if the result should be sorted or not:
json.dumps(x, indent=4, sort_keys=True)
print(json.dumps(x, indent=4, sort_keys=True)) # sort kore value debe
print(json.dumps(x, indent=4, sort_keys=True)) # sort kore value debe
