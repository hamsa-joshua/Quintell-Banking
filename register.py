#User Registration SIGN IN AND SIGN UP
from databases import *
from customer import *
from bank import Bank
import random
def SignUp():
    username = input("Create username: ")
    temp = db_query(f"SELECT username FROM Customers WHERE username = '{username}'")
    if temp:
        print("Username already exists. Please choose a different one.")
        SignUp()
    else:
        print("Username available for registration")
        password = input("Create password: ")
        name = input("Enter your full name: ")
        age = int(input("Enter your age: "))
        city = input("Enter your city: ")
        while True:
            account_number = int(random.randint(10000000,  99999999))
            temp = db_query(f"SELECT account_number FROM Customers WHERE account_number = '{account_number}';")
            if temp:
                continue
            else:
                print("Your account number: " + str(account_number))
                break                
    
    cobj = Customer(username , password , name , age , city , account_number)
    cobj.createuser()
    bobj = Bank(username, account_number)
    bobj.create_transaction_table()
def SignIn():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        temp = db_query(f"SELECT * FROM Customers WHERE username = '{username}' AND password = '{password}';")
        if temp:
            print("Sign in successful")
            return username 
        else:
            print("Invalid username or password Try again")
            continue
        