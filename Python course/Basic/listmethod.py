numbers=[10,20,30]

numbers.append(40)

print(numbers)
numbers.insert(2,100)
print(numbers)
numbers.remove(20)#jodi list nai emon kichu nai ota remove korte chaile error debe

print(numbers)

if 10 in numbers:#check kore remove 
    numbers.remove(10)
print(numbers)

last=numbers.pop()
#last value remove korbe 
#iccha korle last value ta save oo korrte par 

index=numbers.index(100)
#100 kon index acea seta khujbe
#na thale bolbe 100 is not in the list
print(index)

numbers.sort()
print(numbers)




