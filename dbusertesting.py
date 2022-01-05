#This script is used to test your database,please change your port and host as needed and also make necessary changes.
import mysql.connector
from mysql.connector import errorcode
try:
    connectt= mysql.connector.connect(
        user='root',
        password='',
        host='127.0.0.1',
        database='facerecognition'
    )
    print ("It Works!!")
except mysql.connector.Error as e:
    if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with username or Password")
    elif e.errno== errorcode.ER_BAD_DB_ERROR:
        print("DataBase Does not exist")
    else:
        print(e)
cursor=connectt.cursor()

selectquery="select * from students"

cursor.execute(selectquery)
records=cursor.fetchall()
print("No of user",cursor.rowcount)

for row in records:
    print("URoll",row[0])
    print("Name",row[1])
    print("Password",row[2])
    print("Email",row[3])
    print()
cursor.close()
connectt.close
