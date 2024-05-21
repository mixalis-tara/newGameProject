import mysql.connector
from mysql.connector import Error

def connect():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='dbgameproject'
        )

        if connection.is_connected():
            print("Connected to MySQL db")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def insert_classes_data(connection):
    try:
        cursor = connection.cursor()

        classes_data = [
            ("Warrior", 100, 50),
            ("Mage", 60, 30),
            ("Rogue", 80, 40)
        ]

        insert_query = """
        INSERT INTO classes(class_name, hp, def) VALUES(%s, %s, %s)"""

        cursor.executemany(insert_query, classes_data)
        connection.commit()
        print(f"{cursor.rowcount} records inserted successfully into 'classes' table")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()


if __name__ == "__main__":
    conn = connect()
    if conn:
        insert_classes_data(conn)
        conn.close()