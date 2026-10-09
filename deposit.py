def deposit(money):
    m = 1000
    print(f"Balance: {m} baht")
    try:
        amount = int(money)
        if amount <= 0:
            raise ValueError("Deposit amount must be more than 0")
    except ValueError as error:
        print(f"Something went wrong: {error}")
    else:
        m += amount
        print(f"New balance: {m} baht")
    finally:
        print("Deposit complete")

deposit(input("Enter deposit amount: "))