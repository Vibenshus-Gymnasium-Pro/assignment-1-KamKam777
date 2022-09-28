#Classes and objects - Exercise 1

class BankAccount:
    def __init__(self, pin):
        self.balance = 0
        self.pin = "pin"

    def deposit(self, pin, amount):
        if pin == self.pin:
            self.balance += amount    #defining the state of the account after a deposit
            print("You now have ", end='')
            print(self.balance, end='')
            print(" dollar(s) in your account")
        else:
            print("Wrong pin")

    def withdraw(self, pin, amount):
        if pin == self.pin:
            if amount > self.balance:
                print("You are withdrawing more than what's in the account")
            else:
                self.balance -= amount    #defining the state of the account after a withdrawal
                print("You have ", end='')
                print(self.balance, end='')
                print(" dollar(s) left in your account")
        else:
            print("Wrong pin")

    def getbalance(self, pin):
        if pin == self.pin:
            print(self.balance)
        else:
            print("Wrong pin")

    def change_pin(self, oldpin, newpin):
        if oldpin == self.pin:
            if newpin == oldpin:
                print("Pin unchanged successfully?")
            else:
                self.pin = newpin
                print("Pin changed successfully!")

if __name__ == '__main__':    #making a main method
    account = BankAccount("pin")
    account.deposit("pin", 1000)
