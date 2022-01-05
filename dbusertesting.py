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
# insertquery="insert into students values(%s,%s,%s,%s)"
# val=(182987,"eyuq","bchdjb","yedboi@jcnwi.com")
# cursor.execute(insertquery,val)
# connectt.commit()
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
#
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)
#
# mydb.commit()





#8888888888888888888888888888888888888






# import mysql.connector
# from mysql.connector import (connection)
#
# config = {
#   'user': 'root',
#   'password': '',
#   'host': '127.0.0.1',
#   'database': 'facerecognition',
#   'raise_on_warnings': True
# }
#
# cnx = mysql.connector.connect(**config)
#
# cursor=cnx.cursor()
# selectquery="select * from students"
# cursor.execute(selectquery)
# records=cursor.fetchall()
# print("No of user",cursor.rowcount)
#
# for row in records:
#     print("URoll",row[0])
#     print("Name",row[1])
#     print("Password",row[2])
#     print("Email",row[3])
#     print()
# cnx.close()






#888888888888888888888888888888888






