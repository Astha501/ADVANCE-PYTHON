balance = 0
transactions = []

while True:
    print("\nMenu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. View Transactions")
    print("5. Exit")
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            transactions.append(f"Deposited: ${amount:.2f}")
            print(f"${amount:.2f} deposited successfully.")
        else:
            print("Invalid amount. Please enter a positive number.")
    elif choice == '2':
        amount = float(input("Enter withdrawal amount: "))
        if 0 < amount <= balance:
            balance -= amount
            transactions.append(f"Withdrew: ${amount:.2f}")
            print(f"${amount:.2f} withdrawn successfully.")
        else:
            print("Invalid amount. Please enter a positive number not exceeding your balance.")
    elif choice == '3':
        print(f"Current balance: ${balance:.2f}")
    elif choice == '4':
        if transactions:
            print("Transaction History:")
            for transaction in transactions:
                print(transaction)
        else:
            print("No transactions yet.")
    elif choice == '5':
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
        
        
        
        
        
        balance = 0
transactions = []

PASSWORD = "1234"
attempts = 3

# Password checking
while attempts > 0:
    entered_password = input("Enter your password: ")
    if entered_password == PASSWORD:
        print("Login successful!")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Wrong password. Attempts left: {attempts}")
        else:
            print("Too many wrong attempts. Try again later.")
            exit()

# Main menu
while True:
    print("\nMenu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. View Transactions")
    print("5. Exit")
    
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            transactions.append(f"Deposited: ${amount:.2f}")
            print(f"${amount:.2f} deposited successfully.")
        else:
            print("Invalid amount.")

    elif choice == '2':
        amount = float(input("Enter withdrawal amount: "))
        if 0 < amount <= balance:
            balance -= amount
            transactions.append(f"Withdrew: ${amount:.2f}")
            print(f"${amount:.2f} withdrawn successfully.")
        else:
            print("Invalid amount or insufficient balance.")

    elif choice == '3':
        print(f"Current balance: ${balance:.2f}")

    elif choice == '4':
        if transactions:
            print("Transaction History:")
            for transaction in transactions:
                print(transaction)
        else:
            print("No transactions yet.")

    elif choice == '5':
        print("Exiting the system.")
        break

    else:
        print("Invalid choice.")