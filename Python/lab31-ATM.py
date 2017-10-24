"""
This program emulates an ATM program
original version by Kyle Douglas
"""

# creates a class called ATMAccount
class ATMAccount:
# defines the class
    def __init__(self, bal, interest):
        self.bal = bal
        self.interest = interest

# checks the balance
    def check_bal(self):
        return self.bal
# makes a deposit
    def deposit(self, amount):
        self.bal += amount
# checks the withdrawal amount
    def check_withdrawal(self, amount):
        if self.bal < amount:
            return False
        else:
            return True
# executes the withdrawal
    def withdrawal(self, amount):
        self.bal -= amount


# calculates the interest on the account
    def calc_interest(self):
        interest = 0.01
        return self.bal * interest






# defines and prints the above class
account = ATMAccount(100.0, 0.01)
print(account.check_bal())
amount = float(input('How much would you like to withdrawal?: '))
account.withdrawal(amount)
amount = float(input('how much would you like to deposit?: '))
account.deposit(amount)
print(account.check_bal())
print(account.calc_interest())