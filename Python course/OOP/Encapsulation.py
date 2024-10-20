#Encapsulation -->hide details
#access Modifier -->public,protected & private

class Bank:
    def __init__(self,holder_name,initial_deposit) -> None:
        self.holder_name=holder_name #public attribute
        # self.balance=initial_deposit
        self._branch='banani' #its not private its protected it can be access from outside  its do not mean nothing

        #below private attribute
        self.__balance=initial_deposit #bahir theke access kora jabe na
         
    def  deposit(self,amount):
        self.__balance+=amount

    def get_balance(self):
        return self.__balance 
    
    def withdraw(self,amount):
        if amount <self.__balance :
            self.__balance=self.__balance-amount
            return amount
        else:
            return f'Taka nai'
    


rafsun=Bank('Choooto bro',10000)

print(rafsun.holder_name)
# print(rafsun.balance)
# print(rafsun.__balance)#not accessable
rafsun.deposit(10000)
print(rafsun.get_balance())
rafsun.holder_name='Boro vai'
print(rafsun.holder_name)
print(dir(rafsun))
print(rafsun._Bank__balance)# dir theke paici ager line a 



      