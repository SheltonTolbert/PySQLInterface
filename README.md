# PySQLInterface
An easy to use mySQL interface 

# connect to mySQL database
initialize_database(string host, string root, string password)

# insert records into table
insert(string tableName, string[] columns, string[][] values)

# terminate connection 
disconnect()
  
# change active database
switch_database(string databaseName)

