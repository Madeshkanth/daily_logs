def withdrawl(account_balance,amount):
    if account_balance >= amount:
        account_balance -= amount
        print(f"Withdrawal successful! New balance: {account_balance}")
    else:
        print("Insufficient funds for withdrawal.")
def dep(account_balance,amount):
    account_balance+=amount
    print(f"Successfull deposite☑️ ☑️ ☑️\nYour new balance is:{account_balance}")
def password(current,new):
    new_password=new
    print(f"Successfull password changed☑️ ☑️ ☑️\nYour new password is:",new_password)
