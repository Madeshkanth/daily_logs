from business import withdrawl,dep
def main():
    def userinfo():
        name=input("Enter your name: ")
        acount_number=int(input("Enter your account number: "))
        account_balance=int(input("Enter your account balance: "))
        if account_balance<0:
                print("account balance cant be negative")
        else:
            withdraw=input("Do you want to Withdrawl['yes or No']:")
            if withdraw=='yes':
                a=int(input("enter the amount need to withdraw:"))
                withdrawl(account_balance,a)
            else:
                deposit=input("do u want to deposite['yes or no']:")
                if deposit =="yes":
                    c=int(input("enter the amount need to deposite:"))
                    dep(account_balance,c)
    print("Welecome to our bank website🏤 🏤 🏤\nOur services are\n1.withdrawl\n2.deposite\n3.Password change\n")
    print("enter your user information")
    userinfo()
if __name__=="__main__":
     main()