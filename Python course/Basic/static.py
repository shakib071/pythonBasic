
#class method
#static method
class Shoping:
    cart=[] #statica attribute or class attribute
    origin="china"

    def __init__(self,name,location) -> None:
        self.name=name #instance Attribute
        self.location=location

    def purchase(self,item,price,amount):
        remaining=amount-price
        print(f'buying :{item} for price {price} remaining :{remaining}' )

    @staticmethod
    def multiply(a,b):#self er dorkar nai
        # print(self.name)#use kora jabe na karon self use kori na
        print(a*b)
    

    @classmethod
    def hudai_dekhi(self,item):
        print("hudai ",item)


basundhara=Shoping("basu","alu")
basundhara.purchase('lungi',500,1000)
basundhara.hudai_dekhi('Alu')

# Shoping.purchase(2,3,3) #eta error dey ekhane self soho dite hbe
Shoping.hudai_dekhi('lungi') #classmethod bolar por direct class a use kora jacche
Shoping.multiply(4,6)
Shoping.multiply(6,9)#staic method a self er dorkar nai
basundhara.multiply(6,9)

