def show_menu():
    print("\nSimple Budget Tracker")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Current Balance")
    print("4. View All Transactions")
    print("5. Exit")

def add_income(balance):
    try:
        amount = float(input("Enter income amount: "))
        if amount <= 0:
            print("Income must be a positive value.")
        else:
            balance += amount
            print(f"Income of {amount} added successfully!")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    return balance

def add_expense(balance, transactions):
    try:
        amount = float(input("Enter expense amount: "))
        if amount <= 0:
            print("Expense must be a positive value.")
        else:
            balance -= amount
            description = input("Enter expense description: ")
            transactions.append(f"Expense: {description} - {amount}")
            print(f"Expense of {amount} added successfully!")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    return balance, transactions

def view_balance(balance):
    print(f"Current balance: {balance}")

def view_transactions(transactions):
    if transactions:
        print("\nTransactions History:")
        for transaction in transactions:
            print(transaction)
    else:
        print("No transactions recorded yet.")

def budget_tracker():
    balance = 0.0
    transactions = []

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            balance = add_income(balance)
        elif choice == '2':
            balance, transactions = add_expense(balance, transactions)
        elif choice == '3':
            view_balance(balance)
        elif choice == '4':
            view_transactions(transactions)
        elif choice == '5':
            print("Thank you for using the Budget Tracker!")
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    budget_tracker()
