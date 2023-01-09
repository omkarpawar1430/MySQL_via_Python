import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
cursor = mydb.cursor()
cursor.execute("use testdb")
# Execute a SELECT statement and fetch all rows
cursor.execute('SELECT * FROM test_table')
rows = cursor.fetchall()

# Close the cursor
cursor.close()

# Do something with the rows
for row in rows:
    print(row)

# Close the connection
mydb.close()