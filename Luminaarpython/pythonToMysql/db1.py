import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    auth_plugin='mysql_native_password',
    database='luminarpython'
)
cursor=db.cursor()
sql= 'SELECT VERSION()'
cursor.execute(sql)
data=cursor.fetchone()
print("Database version : ",data)

db.close()