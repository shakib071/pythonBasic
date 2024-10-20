class Phone:
    manufactured='China'

    # def __init__(self):#constractor
    #     pass
    #init tai constractor
    def __init__(self,owner,brand,price):#constractor
        self.owner=owner
        self.brand=brand
        self.price=price

my_phone=Phone('kala Chan','Oppo',9999) #constractor  a 3 ta perameter acea tai 3 ta value dile hbe
print(my_phone.brand,my_phone.owner,my_phone.manufactured,my_phone.price)

        