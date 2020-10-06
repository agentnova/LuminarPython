import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    auth_plugin='mysql_native_password',
    database='luminarpython'
)
cursor=db.cursor()
try:
    sql="SELECT * FROM EMPLOYEE WHERE SAL>1000"
    cursor.execute(sql)
    res=cursor.fetchall()

    for x in res:
         print(x)
except Exception as e:
    print(e.args)

finally:
    db.close()
