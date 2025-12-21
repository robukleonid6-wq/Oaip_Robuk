class bank_account:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"пополнено: {amount}. баланс: {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("недостаточно средств!")
        else:
            self.balance -= amount
            print(f"снято: {amount}. баланс: {self.balance}")
    
    def get_balance(self):
        return self.balance

account = bank_account("магомед", 100)
account.deposit(50)
account.deposit(50)
account.withdraw(200)
account.withdraw(30)
print("итоговый баланс:", account.get_balance())