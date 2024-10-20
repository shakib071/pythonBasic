class Shop:
    shopping_Mall='Jamuna'

    def __init__(self,buyer):
        self.buyer=buyer
        self.cart=[] #cart is a insatance attributes


    def add_to_cart(self,item):
        self.cart.append(item)


mehzabeen=Shop('meh')
mehzabeen.add_to_cart('Alu')
mehzabeen.add_to_cart('Potol')
print(mehzabeen.cart)

nisho=Shop("nish")

nisho.add_to_cart("Cap")
nisho.add_to_cart("Bador")
print(nisho.cart)
