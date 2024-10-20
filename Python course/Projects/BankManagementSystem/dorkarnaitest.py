from abc import ABC
import random
class Base(ABC):

    def __init__(self,name,email,address) -> None:
        self.name=name
        self.email=email
        self.address=address
        

class Bank:
    def __init__(self) -> None:
        self.user_history=[]
        self.loan_status=True




class Admin(Base):
    
    def __init__(self, name, email, address,bank) -> None: #bank er obj
        self.bank=bank
        super().__init__(name, email, address)
        
    
    def create_account(self,user_obj):
        self.bank.user_history.append(user_obj)
        print("Account Created")

    def delete_account(self,account_num):
        
        for account in self.bank.user_history:
            if account.account_num==account_num:
                self.bank.user_history.remove(account)
                print("Account Deleted Successfully")
                return
        print("Account Not found")
    

    def view_accounts(self):
        print("Name\tAccount Number")
        for account in self.bank.user_history:
            print(f'{account.name}\t{account.account_num}')

    def total_bank_balance(self):
        sum=0
        for account in self.bank.user_history:
            sum+=account.balance
        
        print(f'Total Bank Balance is: {sum}')
    


    def total_loan(self):
        sum=0
        for account in self.bank.user_history:
            sum+=account.loan_amount
        
        print(f'Total loan amount is: {sum}')


    def turn_on_loan_status(self):
        self.bank.loan_status=True
        print("Loan Stutus has been turned on")

    def turn_off_loan_status(self):
        self.bank.loan_status=False
        print("Loan status has been turn off")
    
    


class User(Base):
    def __init__(self, name, email, address,accout_type,bank) -> None:#Saving or Current#bank er obj
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

        for account in self.bank.user_history:
            if account.account_num==reiceiver_acc:
                account.account_num-=amount
                for account1 in self.bank.user_history:
                    if account1.account_num==reiceiver_acc:
                        account1.account_num+=amount
                        return
        print("Account is Invalid")
                    


        

bank1=Bank()

def UserFunc():

    name=input("Enter Your Name: ")
    email=input("Enter Your email : ")
    address=input("Enter Your Address: ")
    account_type=input("Enter Your account type (Savings or Current) : ")
    customer=User(name,email,address,account_type,bank1)
    
    while True:
        print("Welcome")
        print("1: Create Account")
        print("2: Deposit")
        print("3: Withdraw")
        print("4: Check Balance")
        print("5: View Transaction History")
        print("6: Take_loan")
        print("7:transfer money")
        print("8: Exit")


        choice=int(input("Enter your Choice : "))

        if choice == 1:
            customer.create_account(customer)

        elif choice == 2:
            amount=int(input("Enter The Amount: "))
            customer.deposite(amount)

        elif choice == 3:
            amount1=int(input("Enter The Amount: "))
            customer.withdraw(amount1)
        
        elif choice == 4:
            customer.check_balance()

        elif choice == 5:
            customer.view_transaction_history()

        elif choice == 6:
            amount2=int(input("Enter loan amount: "))
            customer.take_loan(amount2)

        elif choice == 7:
            receiver_acc=int(input("Enter receiver account number: "))
            amountt=int(input("Enter transfer amount: "))
            customer.tranfer_money(receiver_acc,amountt)
        
        elif choice == 8:
            print("Exiting")
            break

        else:
            print("Invalid Choice")




def AdminFunc():

    name=input("Enter Your Name: ")
    email=input("Enter Your email : ")
    address=input("Enter Your Address: ")
    admin=Admin(name,email,address,bank1)

    while True:
        print("Welcome Admin")
        print("1: Create Account")
        print("2: delete Account")
        print("3: View Accounts")
        print("4: View Total Bank Amount")
        print("5: View Total Loan Amount")
        print("6: Turn on Loan Status")
        print("7: Turn off Loan Status")
        print("8: Exit")

        choice=int(input("Enter your Choice: "))

        if choice == 1:
            name1=input("Enter user name: ")
            email1=input("Enter user email: ")
            address1=input("Enter user address")
            account_type1=input("Enter user account type (Saving or Current): ")
            user1=User(name1,email1,address1,account_type1,bank1)
            admin.create_account(user1)
        elif choice == 2:
            acc_num=int(input("Enter account Number: "))
            admin.delete_account(acc_num)

        elif choice == 3:
            admin.view_accounts()
        
        elif choice == 4:
            admin.total_bank_balance()

        elif choice == 5:
            admin.total_loan()

        elif choice == 6:
            admin.turn_on_loan_status()

        elif choice == 7:
            admin.turn_off_loan_status()

        elif choice == 8:
            print("Exiting")
            break

        else:
            print("Invalid Choice")


while True:
    print("Welcome")
    print("1: Customer")
    print("2: Admin")
    print("3: Exit")

    choice=int(input("Enter Your choice : "))

    if choice == 1:
        UserFunc()

    elif choice == 2:
        AdminFunc()
    
    elif choice == 3:
        print("Exit")
        break

    else:
        print("invalid Choice")

