import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="idunno2306"
)

print(mydb)  

