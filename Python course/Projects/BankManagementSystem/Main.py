from Bank import Bank
from BaseClass import Base
from User import User
from Admin import Admin

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

    choic=int(input("Enter Your choice : "))

    if choic == 1:
        UserFunc()

    elif choic == 2:
        AdminFunc()
    
    elif choic == 3:
        print("Exit")
        break

    else:
        print("invalid Choice")

