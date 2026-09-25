'''
Assignment 3: Bank Account Operations
 A bank wants to perform basic operations on a customer's account.

Create a class BankAccount with the following attributes:

Account number

Account holder name

Balance

Create the following methods:

deposit() - Add an amount to the balance.

withdraw() - Subtract an amount from the balance.

display_account() - Display account details and final balance.

Sample data:

Account Number: 1001
Account Holder: Rahul
Opening Balance: 25000
Deposit: 5000
Withdrawal: 3000

Expected result:

Final Balance: 27000
'''

class BankAccount:
    def deposit(self):
        self.dep = int(input("Enter amount to Deposit: "))
    def withdraw(self):
        self.wit = int(input("Enter amount to Withdrawn: "))        
    def display_result(self,bal):
        self.final = bal+self.dep-self.wit
        print("Final Balance:",self.final)


s1 = BankAccount()

acc = int(input("Enter Account Number: "))
name = input("Enter Account Holder Name: ")
bal = int(input("Enter Balance: "))

s1.deposit()
s1.withdraw()
s1.display_result(bal)
