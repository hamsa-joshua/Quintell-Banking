from databases import *
from datetime import datetime

class Bank:
    
    def __init__(self, username, account_number):
        self.__username = username
        self.__account_number = account_number
        self.create_transaction_table()
        
    def create_transaction_table(self):
        db_query(f"""
        CREATE TABLE IF NOT EXISTS {self.__username}_transaction (
            timedate VARCHAR(30),
            account_number INTEGER,
            remark VARCHAR(30),
            amount INTEGER,
            type VARCHAR(20)
        )
        """)
    
    def balanceenquiry(self):
        temp = db_query(f"SELECT balance FROM Customers WHERE username = '{self.__username}';")
        print(f"User {self.__username} your balance is : {temp[0][0]}")
        
    def deposit(self, amount):
        temp = db_query(f"SELECT balance FROM Customers WHERE username = '{self.__username}';")
        new_balance = temp[0][0] + amount
        db_query(f"UPDATE Customers SET balance = {new_balance} WHERE username = '{self.__username}';")
        self.balanceenquiry()
        db_query(f"""
        INSERT INTO {self.__username}_transaction (timedate, account_number, remark, amount, type)
        VALUES ('{datetime.now()}', {self.__account_number}, 'Amount Deposit', {amount},'Credit')
        """)
        print(f"User {self.__username} your Money is Sucessfully Deposited into Your Account {self.__account_number}")

    def withdraw(self, amount):
        temp = db_query(f"SELECT balance FROM Customers WHERE username = '{self.__username}';")
        if amount > temp[0][0]:
            print(f"Insufficient Balance. You have only {temp[0][0]}")
            return
        new_balance = temp[0][0] - amount
        db_query(f"UPDATE Customers SET balance = {new_balance} WHERE username = '{self.__username}';")
        self.balanceenquiry()
        db_query(f"""
        INSERT INTO {self.__username}_transaction (timedate, account_number, remark, amount, type)
        VALUES ('{datetime.now()}', {self.__account_number}, 'Amount Withdrawn', {amount},'Debit')
        """)
        print(f"User {self.__username} your Money is Successfully Withdrawn from your Account {self.__account_number}")



    def fundtransfer(self, receiver, amount):
        temp = db_query(f"SELECT balance FROM Customers WHERE username = '{self.__username}';")
        if amount > temp[0][0]:
            print(f"Insufficient Balance. You have only {temp[0][0]}")
            return
        temp2 = db_query(f"SELECT balance FROM Customers WHERE account_number = {receiver};")
        if not temp2:
            print("Receiver account does not exist.")
            return
        sender_new_balance = temp[0][0] - amount
        receiver_new_balance = temp2[0][0] + amount
        db_query(f"UPDATE Customers SET balance = {sender_new_balance} WHERE username = '{self.__username}';")
        db_query(f"UPDATE Customers SET balance = {receiver_new_balance} WHERE account_number = {receiver};")
        receiver_username = db_query(f"SELECT username FROM Customers WHERE account_number = '{receiver}';")
        self.balanceenquiry()
        
        db_query(f"""
        INSERT INTO {receiver_username[0][0]}_transaction (timedate, account_number, remark, amount, type)
        VALUES ('{datetime.now()}', {self.__account_number}, 'Fund Recieved From {self.__account_number}', {amount},'Credit')
        """)
        
        db_query(f"""
        INSERT INTO {self.__username}_transaction (timedate, account_number, remark, amount, type)
        VALUES ('{datetime.now()}', {self.__account_number}, 'Fund Transferred --> {receiver}', {amount},'Debit')
        """)
        
        print(f"User {self.__username} Money Successfully Transferred from your Account {self.__account_number} to {receiver}")
