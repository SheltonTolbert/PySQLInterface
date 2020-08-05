import mysql.connector
import sys

mydb = None
host = 'localhost'
user = 'root'
password = 'password'


def initialize_database():
    global mydb
    mydb = mysql.connector.connect(
        host=host, user=user, password=password)
    print(mydb)


def create_database(databaseName):
    print('created new database : ' + databaseName)
    global mydb
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE " + databaseName)
    for x in mycursor:
        print(x)

# arguments: string, string[], string[]


def insert(tableName, columns, values):
    global mydb
    mycursor = mydb.cursor()

    cols = ''
    for c in range(0, len(columns) - 1):
        cols += columns[c] + ', '
    cols += columns[len(columns) - 1]

    vals = ''
    for v in range(0, len(values) - 1):
        vals += "'" + values[v] + "'" + ', '
    vals += "'" + values[len(values) - 1] + "'"

    sql = "INSERT INTO " + tableName + " (" + cols + ") VALUES (" + vals + ")"

    mycursor.execute(sql)
    print(sql)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")


def disconnect():
    global mydb
    global mycursor
    mycursor.close()


def show_databases():
    global mydb
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
        print(x)
    mycursor.close()


def switch_database(databaseName):
    global mycursor
    mycursor = mydb.cursor()
    mycursor.execute("USE " + databaseName)
    mycursor.execute("SELECT DATABASE()")
    for x in mycursor:
        print(x)
    mycursor.close()


def main():
    print('initializing session')
    initialize_database()
    show_databases()
    switch_database('testdatabase')
    insert("testtable", ['firstname', 'lastname'], ['name1', 'name2'])


if __name__ == "__main__":
    main()
