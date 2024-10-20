
#in python function is first class object

def double_decker():
    print('starting the double decker')

    def inner_func():
        print("inside func")
        return 5
    
    return inner_func

# print(double_decker())
# print(double_decker()()) #innter func k call korbe

def do_something(work):
    print('work started')
    # print(work)
    work()
    print('work ended')

# do_something(2)
# do_something('gshdghs')

def coding():
    print("coding")

# do_something(coding)

def sleeping():
    print("sleeping and dreaming")

do_something(sleeping)
