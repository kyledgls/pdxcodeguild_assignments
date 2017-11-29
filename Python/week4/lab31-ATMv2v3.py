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
        self.transactions = []

    # checks the balance
    def check_bal(self):
        return self.bal

    # makes a deposit
    def deposit(self, amount):
        self.bal += amount
        self.transactions.append('You deposited $' + str(amount))



    # checks the withdrawal amount
    def check_withdrawal(self, amount):
        #return amount < self.bal
        if self.bal < amount:
            return False
        else:
            return True

    # executes the withdrawal
    def withdraw(self, amount):
        self.bal -= amount
        self.transactions.append('You withdrew $' + str(amount))


    # calculates the interest on the account
    def calc_interest(self):
        interest = 0.01
        return self.bal * interest

    def print_transactions(self):
        for i in range(len(self.transactions)):
            print(self.transactions[i])



account = ATMAccount(100.0, 0.01)

while True:
    command = input('what would you like to do? ')
    if command == 'done':
        break
    elif command == 'withdraw':
        amount = float(input('How much would you like to withdraw?: '))
        check = account.check_withdrawal(amount)
        if check == False:
            print('You cannot withdraw')
        else:
            account.withdraw(amount)
    elif command == 'deposit':
        amount = float(input('how much would you like to deposit?: '))
        account.deposit(amount)
    elif command == 'check bal':
        print(account.check_bal())
    else:
        print('INVALID')





# defines and prints the above class

account.print_transactions()
check_withdrawal()
print(account.calc_interest())
