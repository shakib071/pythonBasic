txt = f"The price is 49 dollars"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)


price = 59
txt = f"The price is {price:.2f} dollars"
# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:

print(txt)


#You can perform if...else statements inside the placeholders

price = 434

txt=f"It is very {'Expensive' if price>50 else 'Cheap'}"
print(txt)


#Use the string method upper()to convert a value into upper case letters

fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)

def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)


price = 59000
txt = f"The price is {price:,} dollars"
print(txt)


#Add a placeholder where you want to display the price
#eta ager pyto a use hoto


# price=54
# txt="The price is {} dollers"
# price(txt.format(price))




