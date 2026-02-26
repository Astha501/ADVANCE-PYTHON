balance = 0
transactions = []
PASSWORD = "1234"



def login():
    attempts = 3
    while attempts > 0:
        entered_password = input("Enter your password: ")
        if entered_password == PASSWORD:
            print("Login successful!")
            return True
        else:
            attempts -= 1
            print(f"Wrong password. Attempts left: {attempts}")
    print("Too many wrong attempts. Try again later.")
    return False



def deposit():
    global balance
    amount = float(input("Enter deposit amount: "))
    if amount > 0:
        balance += amount
        transactions.append(f"Deposited: ${amount:.2f}")
        print(f"${amount:.2f} deposited successfully.")
    else:
        print("Invalid amount.")



def withdraw():
    global balance
    amount = float(input("Enter withdrawal amount: "))
    if 0 < amount <= balance:
        balance -= amount
        transactions.append(f"Withdrew: ${amount:.2f}")
        print(f"${amount:.2f} withdrawn successfully.")
    else:
        print("Invalid amount or insufficient balance.")



def check_balance():
    print(f"Current balance: ${balance:.2f}")



def view_transactions():
    if transactions:
        print("Transaction History:")
        for transaction in transactions:
            print(transaction)
    else:
        print("No transactions yet.")



def menu():
    while True:
        print("\nMenu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transactions")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            deposit()
        elif choice == '2':
            withdraw()
        elif choice == '3':
            check_balance()
        elif choice == '4':
            view_transactions()
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice.")



if login():
    menu()
