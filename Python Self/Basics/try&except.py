# # The try block lets you test a block of code for errors.
# # The except block lets you handle the error.
# # The else block lets you execute code when there is no error.
# # The finally block lets you execute code, regardless of the result of the try- and except blocks.

# try:
#     print(x) #x ke define kori nai tai exception a jabe
# except:
#     print("An exception occured")

# #You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:

# try:
#     print(x)
# except NameError:#name er error x undefine
#     print("Variable x is not define") 
# except:
#     print("something else went wrong")


# #You can use the else keyword to define a block of code to be executed if no errors were raised

# try:
#     print("hello")
# except:
#     print("Something else went wrong")
# else:
#     print("Nothing went wrong")

# # The finally block, if specified, will be executed regardless if the try block raises an error or not

# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#     print("jhdfghjdfs") #error dik ar na dik eta kaj korbei

# #This can be useful to close objects and clean up resources:

# try:
#   f = open("demofile.txt")
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")




#Raise an exception

x=-1

if x<0:
    raise Exception("Sorry, no numbers below zero")

#Raise a TypeError if x is not an integer
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")


