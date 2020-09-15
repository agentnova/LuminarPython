import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    auth_plugin='mysql_native_password',
    database='luminarpython'
)
cursor=db.cursor()
cursor.execute("DROP TABLE IF EXISTS employee")
sql="CREATE TABLE EMPLOYEE(FIRST_NAME CHAR(20),lAST_NAME CHAR(20),AGE INT,SEX CHAR(1),SAL INT)"
cursor.execute(sql)


db.close()