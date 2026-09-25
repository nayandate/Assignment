from models.account import Account


def create_accounts():
    return [
        Account(101, "Amit", 45000),
        Account(102, "Rahul", 75000),
        Account(103, "Priya", 35000),
        Account(104, "Neha", 90000),
        Account(105, "Rohit", 55000),
    ]


def find_account(accounts, account_no):
    return next(
        (account for account in accounts if account.account_no == account_no),
        None,
    )


def display_accounts(accounts):
    for account in accounts:
        account.display()


def main():
    accounts = create_accounts()

    print("All Accounts:")
    display_accounts(accounts)

    account = find_account(accounts, 101)
    if account is not None:
        account.deposit(10000)
        print("\nAfter Deposit:")
        account.display()

    account = find_account(accounts, 103)
    if account is not None:
        account.withdraw(5000)
        print("\nAfter Withdrawal:")
        account.display()

    print("\nAccounts having balance greater than 50000:")
    display_accounts([account for account in accounts if account.balance > 50000])

    highest_balance_account = max(accounts, key=lambda account: account.balance)
    print("\nHighest Balance Account:")
    highest_balance_account.display()


if __name__ == "__main__":
    main()
