balance=3000
#global

def buy_things(item,price):
    #local scope variable func er moddhe declare hoy
    #ota func er baire acces kora jay na
    #you can access the global variable withiout global keyword
    #but if you want to modify the global variable u have to use global keyword
    global balance
    balance=balance-price
    #global variable func er moddhe change kora jabe na

    print(f'balance after buying {item}',balance)

buy_things("hfj",500)