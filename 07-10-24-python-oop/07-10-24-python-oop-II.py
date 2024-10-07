class BankAccount:
    def __init__(self,account_number,account_holder,balance) :
        self.account_number = account_number
        self._account_holder = account_holder
        self.__balance = balance
        
    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self._account_holder}")
        print(f"Balance: {self.__balance}")
        
    def _update_account_holder(self, new_name):
        self._account_holder = new_name
        print("Account holder's name updated.")
        
    def __update_balance(self,amount):
        if amount < 0 and abs(amount) > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance += amount
            print("Balance updated.")
            
    def withdraw(self, amount):
        self.__update_balance(-amount)
        
    def deposit(self,amount):
        self.__update_balance(amount)
        
account = BankAccount('123654','Bob',10000)
print(account.account_number)
print(account._account_holder)
account.display_account_info()
account.deposit(2000)
account.withdraw(3000)
account.display_account_info()