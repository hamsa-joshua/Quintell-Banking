from register import *

print("WELCOME TO QUINTELL BANKING")

while True:
    try:
        register = int(input("1. SIGN UP\n""2. SIGN IN"))
        
        if register ==  1 or register == 2:
            if register == 1:
                SignUp()
            elif register == 2:
                SignIn()    
        else:
            print("Please enter a Valid input From Options.")
            
    except ValueError:
        print("Invalid input. Please enter Numeric input")
        