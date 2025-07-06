class BankAccount:
    def __init__(self , balance) :
        self ._balance = balance
    @property
    def balance(self):
        return self._balance
    
    @balance.setter 
    def balance(self, amount):
        if amount <0 :
            raise ValueError("Balance can not be negative.")
        self._balance = amount
        
        
acc=BankAccount(1000)
print(acc.balance)
acc.balance=200
print(acc.balance)
    