#key value pair
#dictionary
#object
#hash map
#overlap with set
#{key:value,key:value}


person={'name':'kalapakhi','address':'kaliapur','job':'bekar','age':23}
print(person)
print(person['job'])
print(person.keys())

person['language']="python"#new value add

print(person)

person['name']="Alu" #modify name
print(person)

#special dictionary loop

for key,value in person.items():
    print(key,value)


