import mysql.connector as abc
from mysql.connector import Error

def connect_to_mysql():
    try:
        mycon = abc.connect(
            host='localhost',
            database='nasa',
            user='root',
            password='Anubhav@2007'
        )
        
        if mycon.is_connected():
            print('Connected to MySQL database')

        return conn

    except Error as e:
        print(f"Error: {e}")
        return None

    finally:
        if conn and conn.is_connected():
            conn.close()

# Call the function to connect to MySQL
connect_to_mysql()
