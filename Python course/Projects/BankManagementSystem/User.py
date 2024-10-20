
from BaseClass import Base
import random
from Bank import Bank

class User(Base):
    def __init__(self, name, email, address,accout_type,bank) -> None:#Saving or Current
        self.account_type=accout_type
        
        self.balance=0
        
        # self.account_num=self.generate_account()
        self.account_num=random.randint(1,1000000)
        self.transaction_history=[] #transaction history
        self.loan_history=[]
        self.loan_amount=0
        self.bank=bank
        super().__init__(name, email, address)
        
    
    def create_account(self,obj): #user object
        self.bank.user_history.append(obj)
        print("Account Created")

    # def generate_account(self):
    #     temp=random.randint(1,1000000000)

    #     for account in self.bank.user_history:
    #          if account.account_num == temp:
    #              self.generate_account()
        
    #     return temp
    
    
    

    def deposite(self,amount):
        self.balance+=amount
        print(f'Your deposit amount {amount} is added to Your Account \n Your new balance is {self.balance}')
        self.transaction_history.append(f'Deposited {amount}')

    def withdraw(self,amount):
        if self.balance < amount:
            print("Withdraw Amount Exceeded")

        else:
            self.balance-=amount
            print(f'Your Withdraw of amount : {amount} is successful \n your new balance is {self.balance} ')
            self.transaction_history.append(f'Withdrew {amount} ')
        

    def check_balance(self):
        print(f'Your account balance is: {self.balance}')
    

    def view_transaction_history(self):
        for transeaction in self.transaction_history:
            print(transeaction)
    
    def can_take_loan(self):

        if len(self.loan_history) < 2 and self.bank.loan_status :
            return True
        else:
            return False

    def  take_loan(self,amount): #loan amount

        if self.can_take_loan():
            self.loan_history.append(f'Loan taken {amount}')
            print("Loan Taken Successfully")
            self.loan_amount+=amount

        else:
            print("You are not eligable for any loans")
        




    def tranfer_money(self,reiceiver_acc,amount): #reciever account ie User object
        if amount>self.balance:
            print("You don't have enough money to send")
            return
        for account in self.bank.user_history:
            if account.account_num==reiceiver_acc:
                account.account_num+=amount
                self.balance-=amount
                self.transaction_history.append(f'Transfer money: {amount} to acc_no {reiceiver_acc}')
                return
        print("Account is Invalid")
                    


        
