# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b


a=33
b=200

if b>a:
    print("Yes")
elif a>b:
    print("No")
else:
    print("Dont know")



# Short Hand If

if a<b : print("a is greater than  b")
print("A") if a > b else print("B")
# This technique is known as Ternary Operators, or Conditional Expressions.



a = 330
b = 330
print("A") if a>b else print("=") if a==b else print("B")
#if a>b print A
# else (if a==b print "=" else print "B")



# The and keyword is a logical operator, and is used to combine conditional statements

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")


# The not keyword is a logical operator, and is used to reverse the result of the conditional statemen
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")


#Nested

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")



# if statements cannot be empty, but if you for some reason have an
#  if statement with no content, put in the pass statement to avoid getting an error

a = 33
b = 200

if b>a:
   pass











