from Bank import Bank

from BaseClass import Base


class Admin(Base):
    
    def __init__(self, name, email, address,bank) -> None:#bank er object
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
    
    

