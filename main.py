from register import *
from bank import *

status = False

print("WELCOME TO QUINTELL BANKING")

while True:
    try:
        register = int(input("1. SIGN UP\n""2. SIGN IN"))
        
        if register ==  1 or register == 2:
            if register == 1:
                SignUp()
            elif register == 2:
                user = SignIn()
                status = True
                break    
        else:
            print("Please enter a Valid input From Options.")
            
    except ValueError:
        print("Invalid input. Please enter Numeric input")
        
        

account_number = db_query(f"SELECT account_number FROM Customers WHERE username = '{user}';")

print(f"YOUR BANKING OPTIONS\n")

while status:
    try:
        facility = int(input("1. BALANCE ENQUIRY\n"
                            "2. CASH DEPOSIT\n"
                            "3. CASH WITHDRAW\n"
                            "4. FUND TRANSFER\n"))
        
        if facility >=  1 or facility <= 4:
            if facility == 1:
                bobj = Bank(user,account_number[0][0])
                bobj.balanceenquiry()
                
            elif facility == 2:
                amount = int(input("Enter the amount to Deposit"))
                bobj = Bank(user,account_number[0][0])
                bobj.deposit(amount)
                
                
            elif facility == 3: 
                amount = int(input("Enter the amount to Withdraw"))
                bobj = Bank(user,account_number[0][0])
                bobj.withdraw(amount)
                
                
            elif facility == 4:
                while True:
                    try:
                        receiver = int(input("Enter Receiver Account Number"))
                        amount = int(input("Enter the amount to Transfer"))
                        bobj = Bank(user,account_number[0][0])
                        bobj.fundtransfer(receiver, amount)   
                        break
                    except ValueError:
                        print("Invalid input. Please enter Numeric input")
                        continue
                        
        else:
            print("Please enter a Valid input From Options.")
            
    except ValueError:
        print("INVALID INPUT TRY AGAIN WITH CORRECT OPTION")
        continue