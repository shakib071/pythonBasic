# result=56/0

# #divission by zero error
# #porer line gula execute korbe na


# print("hello")

try:
    result=45/0
except:
    #error khaile jabe
    print('Error happend')
finally:#exceptional na dileoo hoy
    #eita shob somoyi debe
    print('finally')
print('done')

try:
    result=45/5
except:
    print('Error happend')
finally:#exceptional na dileoo hoy
    #eita shob somoyi debe
    print('finally')
print('done')