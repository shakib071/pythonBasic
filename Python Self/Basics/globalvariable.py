x="Awesome" #Global Variable

def myfunc():
    x="Fantastic" #Local Variable
    print("Python is " +x)

myfunc()

print("Python is "+x)


def myfunc():
    global xx #declares global variable inside a function
    xx=  "Fantastic"

myfunc()

print("Python is ",xx)

