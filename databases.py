import mysql.connector as sql

import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="quintelluser",
    passwd="josh1234",
    db="quintellbank"
)

cursor = db.cursor()

def db_query(str):
    cursor.execute(str)
    result = cursor.fetchall()
    return result   

def createcustomertable():
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Customers
            (username VARCHAR(20),
            password VARCHAR(20),
            name VARCHAR(20),
            age INTEGER,
            city VARCHAR(20),
            account_number INTEGER,
            balance INTEGER,
            status BOOLEAN)

''') 

db.commit()

if __name__ == "__main__":
    createcustomertable()