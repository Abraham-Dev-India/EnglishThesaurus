import mysql.connector

con = mysql.connector.connect(
user = "",     #provide username
password = "", #provide password
host = "",     #provide hostname
database = ""  #provide database name
)

cursor = con.cursor()

word = input("Enter your word")

query = cursor.execute(f"SELECT Definition FROM Dictionary WHERE Expression = '{word}' ")
results = cursor.fetchall()

for result in results:
   print(result)
