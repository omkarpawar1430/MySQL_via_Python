import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)

cur = mydb.cursor()

# cur.execute("create database testdb")
"""
1. We can run create database command only once for one database:
Else it will raise an error called as database already exists.
Hence we need to comment out above line of code.
"""

cur.execute("use testdb") 

# it is important to tell system to access exactly which DB.
# for tables also above commet 1. is aplicable

# cur.execute("create table test_table(name varchar(40), roll_no int, email varchar(40))")

"""
2. The no of times my code gets exucuted that many no of times data gets added.
"""

cur.execute("insert into test_table value('Omkar', 143, 'pawaromkar143@gmail.com' )")

"""
3. We can add multiple tuples in single cammand to add value in bulk.
"""
cur.execute("insert into test_table value('Aparna', 235, 'pawaraparna235@gmail.com'),('Asmita', 453, 'pawarasmita453@gmail.com')")

"""
4. in order to save all changes we need to use commit at the end. 
"""
mydb.commit()


