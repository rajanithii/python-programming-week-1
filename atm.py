# Initial details
PIN = 1234
balance = 5000


def check_balance(balance):
    print("Your current balance is:", balance)


def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print("Amount deposited successfully.")
    return balance


def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print("Please collect your cash.")
    else:
        print("Insufficient balance.")
    return balance


# Login
user_pin = int(input("Enter your PIN: "))

if user_pin == PIN:
    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            check_balance(balance)
        elif choice == 2:
            balance = deposit(balance)
        elif choice == 3:
            balance = withdraw(balance)
        elif choice == 4:
            print("Thank you for using ATM.")
            break
        else:
            print("Invalid choice.")
else:
    print("Incorrect PIN. Access denied.")

