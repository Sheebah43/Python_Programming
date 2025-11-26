def show_account(accounts):
    acc_id = input("Account ID: ").strip()
    if not acc_id:
        print("No Account ID entered.")
        return
    acct = accounts.get(acc_id)
    if acct is None:
        print("Account not found.")
        return
    print(f"ID: {acc_id}\nName: {acct.get('name','<unknown>')}\nBalance: {acct.get('balance',0.0)}")

def deposit(accounts):
    acc_id = input("Account ID: ").strip()
    acct = accounts.get(acc_id)
    if not acct:
        print("Account not found.")
        return
    try:
        amt = float(input("Amount to deposit: ").strip())
        if amt <= 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Invalid amount.")
        return
    acct['balance'] = round(acct['balance'] + amt, 2)
    print(f"Deposited {amt}. New balance: {acct['balance']}")

def withdraw(accounts):
    acc_id = input("Account ID: ").strip()
    acct = accounts.get(acc_id)
    if not acct:
        print("Account not found.")
        return
    try:
        amt = float(input("Amount to withdraw: ").strip())
        if amt <= 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Invalid amount.")
        return
    if amt > acct['balance']:
        print("Insufficient funds.")
        return
    acct['balance'] = round(acct['balance'] - amt, 2)
    print(f"Withdrew {amt}. New balance: {acct['balance']}")

def main():
    accounts = {
        "1": {"name": "abc", "balance": 15090.00},
        "2": {"name": "def",   "balance": 25910.50},
        "3": {"name": "ghi",  "balance":  7520.27},
    }

    Options = (
        "\n1. Show account\n""2. Deposit\n""3. Withdraw\n""4. Exit\n"
    )
    while True:
        print(Options)
        choice = input("Choose an option: ").strip()
        if choice == "1":
            show_account(accounts)
        elif choice == "2":
            deposit(accounts)
        elif choice == "3":
            withdraw(accounts)
        elif choice == "4":
            print("Exited.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
