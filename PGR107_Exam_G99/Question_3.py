
# ==============================================================================
# Question 3 (25 points)
# Bank Account Management System
# Date: may, 2025
# Author: 21 - 363 - 287 - 41
# ==============================================================================

# ==============================================================================
# BANK ACCOUNT CLASS
# ==============================================================================
# A class for managing a bank account.
# Features:
# - Deposit and withdraw operations
# - Balance inquiry
# - Add interest based on the users inputed %
# ==============================================================================

class BankAccount:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount:.2f} kr deposited")
        else:
            print("Amount must be more than 0")
    
    # Withdraws money from the created account
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        elif amount <= 0:
            print("Amount must be more than 0")
        else:
            self.balance -= amount
            print(f"{amount:.2f} kr withdrawn, you have {self.balance:.2f} kr left")

    # Add interest based on the users input
    def add_interest(self, rate):
        interest = self.balance * rate / 100
        self.balance += interest
        print(f"{rate:.1f}% interest added, which equals to {interest:.2f} kr")
        print(f"You now have {self.balance:.2f} kr")
       
    # Returns the created accounts balance
    def get_balance(self):
        return self.balance


# ==============================================================================
# MENU CLASS
# ==============================================================================
# This class handles the interactive menu for the user.
# It stores a list of options and handles user input validations
# ==============================================================================
class Menu:
    def __init__(self):
        self.options = []
        self.add_option("Open a new account")
        self.add_option("Deposit money into your account")
        self.add_option("Withdraw money from your account")
        self.add_option("Add interests to your account")
        self.add_option("Get the current balance of your account")
        self.add_option("Quit")

    def add_option(self, option):
        self.options.append(option)
    
    # Shows the menu and gets the user input to initiate choosen method
    def get_input(self):
        print("\n\n=================================")
        print("Bank Account Management System")
        print("=================================")

        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")
        try:
            print("----------------------------------")
            choice = int(input("Enter your choice (1-6): "))
            print("----------------------------------")
            if 1 <= choice <= 6:
                return choice
            else:
                print("Please enter a number between 1 and 6")
                return self.get_input()
        except ValueError:
            print("Invalid input. Please enter a number. between 1 and 6")
            return self.get_input()

# ==============================================================================
# MAIN PROGRAM
# ==============================================================================
# Runs the main loop the bank management system
# The user can:
# - Open a new account
# - Deposit or withdraw money
# - Add interest using a custom rate %
# - Check the current balance of the account
# - Exits the program
# ==============================================================================

def main():
    menu = Menu()
    account = None

    while True:
        choice = menu.get_input()
        
        # Creates a new account
        if choice == 1:
            account = BankAccount()
            print("New account was created successfully")
            
        # Deposit money to the created account
        elif choice == 2:
            if account:
                try:
                    amount = float(input("Enter amount to deposit (kr): "))
                    print("----------------------------------")
                    account.deposit(amount)
                except ValueError:
                    print("Invalid input. Please enter a number")
            else:
                print("Please open an account first")

        # Withdraw money from the created account
        elif choice == 3:
            if account:
                try:
                    amount = float(input("Enter amount to withdraw (kr): "))
                    print("----------------------------------")
                    account.withdraw(amount)
                except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                print("Please open an account first")

        # Adds interest with user-defined rate to the created account
        elif choice == 4:
            if account:
                try:
                    rate = float(input("Enter interest (%) to your account balance: "))
                    print("----------------------------------")
                    account.add_interest(rate)
                except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                print("Please open an account first")

        # Shows the balance of the account
        elif choice == 5:
            if account:
                balance = account.get_balance()
                print(f"Current balance: {balance:.2f} kr")
            else:
                print("Please open an account first")

        # Stops the program
        elif choice == 6:
            print("Goodbye, spend your wisely!")
            break
        else:
            print("Invalid choice. Please select from 1 to 6")

if __name__ == "__main__":
    main()