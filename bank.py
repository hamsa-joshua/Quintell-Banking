from databases import *

class Bank:
    
    def __init__(self, username, account_number):
        self.__username = username
        self.__account_number = account_number
        
    def create_transaction_table(self):
        db_query(f"CREATE TABLE IF NOT EXISTS {self.__username}_trasaction ("
                f"timedate VARCHAR(30),"
                f"account_number INTEGER,"
                f"remark  VARCHAR(30),"
                f"amount INTEGER,"
                f"type VARCHAR(20))")
        
    def deposit(self, amount):
        temp = db_query()