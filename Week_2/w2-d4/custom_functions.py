import sqlite3
from sqlite3 import Error

connection = 'test'

# sql modules
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

# To execute queries in SQLite, use cursor.execute().
def ex_q(connection, query): # execute query
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
        
def er_q(connection, query): #execute read query
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

def display_query(query,connection=connection):
    q = er_q(query,connection)
    return pd.read_sql_query(q, connection)