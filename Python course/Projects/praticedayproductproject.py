
class Product:
    def __init__(self,id,name,price) -> None:
        self.id=id
        self.name=name
        self.price=price


class Shop:

    def __init__(self) -> None:
        self.products=[]

    def add_product(self,product):
        if isinstance(product,Product):
            self.products.append(product)
        
        else:
            print("F U")
    
    def buy_product(self,product_name):

        for product in self.products:
            if product.name==product_name:
                print("GOT IT")
                return
        print("Sorry product is unavaiabail")
    

        
p1=Product(10,"Laptop",1000)
p2=Product(11,"Alu",2000)
shop=Shop()
shop.add_product(p1)
shop.add_product(p2)

for product in shop.products:
    print(product.id ," ",product.name," ",product.price)
