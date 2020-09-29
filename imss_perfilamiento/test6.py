from pyhive import hive

import pandas as pd

#Create Hive connection

conn = hive.Connection(host="127.0.0.1", port=10000, username="username")


#conn = hive.Connection(host="10.111.22.11", port=10000, username="user1", database="default")

# Read Hive table and Create pandas dataframe

df = pd.read_sql("SELECT * FROM db_Name.table_Name limit 10", conn)

print(df.head())


***************************************

I am using pyhive to interact with hive.

The SELECT statement going well using this code bellow.

# Import hive module and connect
from pyhive import hive
conn = hive.Connection(host="HOST")
cur = conn.cursor()

# Import pandas
import pandas as pd

# Store select query in dataframe
all_tables = pd.read_sql("SELECT * FROM table LIMIT 5", conn)
print all_tables

# Using curssor
cur = conn.cursor()
cur.execute('SELECT * FROM table LIMIT 5')
print cursor.fetchall()