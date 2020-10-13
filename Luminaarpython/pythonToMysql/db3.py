import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    auth_plugin='mysql_native_password',
    database='luminarpython'
)
cursor=db.cursor()
qry="INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX,SAL) VALUES('arun','kumar',22,'M',8000)"
try:
    cursor.execute(qry)
    db.commit()
except Exception as e:
    db.rollback() #changes are undone
    print(e.args)







finally:
    db.close()