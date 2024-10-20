class Shop:
    cart=[] #cart is a class attribute
    #class er sob constractor ektai cart use korbe

    def __init__(self,buyer):
        self.buyer=buyer

    def add_to_cart(self,item):
        self.cart.append(item)

mehzbeen=Shop('mehzabeen')
mehzbeen.add_to_cart('shoes')
mehzbeen.add_to_cart('phone')

print(mehzbeen.cart)

#kintu notun karo add korle cart a agerjoner taooo add hbe 
#eita ekta problem
#etar solution korci
#instance attributes


