# import time
# import sys
# import tkinter
import cv2
import face_recognition
from tkinter import *
from datetime import datetime
import face_recognition as fr
# import global_vars
import numpy as np
import os
import email_send
# import auth
import load
import uilogin
# import uiregister
load2='Please wait'



# load1='Authentication is in progress'
# def loaddata():
#     return load1
# from tkinter import messagebox
# import curses

# email_send.main()

from playsound import playsound
with open('interrupt.csv', 'r') as finterrupt:
    interruptlines = finterrupt.read().splitlines()
    lastinterrupt_line = interruptlines[-1]
    print("reading.....")
    interruptgen=lastinterrupt_line
    print(interruptgen)
if interruptgen=="109":
    print("interrut gen")
    quit()
# print("before")
# quit()
# playsound('/Users/achiyant/Music/iTunes/iTunes Media/Music/Unknown Artist/Unknown Album/Tujhe kaise pta na chla.mp3')

# text = '  ** Press ''q'' to quit this Window . **  '
# def main(s):
#     curses.curs_set(False)
#     num_letters = len(text)
#     for i in range(100000):
#         for i2 in range(170):
#             letter_position = (i + i2) % num_letters
#             s.addstr(10, i2, text[letter_position])
#         s.refresh()
#         time.sleep(0.25)
#     s.getch()
# curses.wrapper(main)




# Username = auth.getusername()
with open('user.csv', 'r') as f:
    lines = f.read().splitlines()
    last_line = lines[-1]
    # print(last_line)
Username =last_line
with open('userURoll.csv', 'r') as fad:
    liness = fad.read().splitlines()
    last_line_admno = liness[-1]
    # print(last_line)
admno =last_line_admno
# print(Username)
# print("reached")
# Username = 'billgates'
# print("123456789")
# print(Username)

def draw_border(img, pt1, pt2, color, thickness, r, d):
    x1, y1 = pt1
    x2, y2 = pt2
    # Top left
    cv2.line(img, (x1 + r, y1), (x1 + r + d, y1), color, thickness)
    cv2.line(img, (x1, y1 + r), (x1, y1 + r + d), color, thickness)
    cv2.ellipse(img, (x1 + r, y1 + r), (r, r), 180, 0, 90, color, thickness)

    # Top right
    cv2.line(img, (x2 - r, y1), (x2 - r - d, y1), color, thickness)
    cv2.line(img, (x2, y1 + r), (x2, y1 + r + d), color, thickness)
    cv2.ellipse(img, (x2 - r, y1 + r), (r, r), 270, 0, 90, color, thickness)

    # Bottom left
    cv2.line(img, (x1 + r, y2), (x1 + r + d, y2), color, thickness)
    cv2.line(img, (x1, y2 - r), (x1, y2 - r - d), color, thickness)
    cv2.ellipse(img, (x1 + r, y2 - r), (r, r), 90, 0, 90, color, thickness)

    # Bottom right
    cv2.line(img, (x2 - r, y2), (x2 - r - d, y2), color, thickness)
    cv2.line(img, (x2, y2 - r), (x2, y2 - r - d), color, thickness)
    cv2.ellipse(img, (x2 - r, y2 - r), (r, r), 0, 0, 90, color, thickness)

count = 0
once = 0
# Username = 'a.jpeg'
pathad='.jpeg'
path = "ImagesRegistered"
images = []
names = []
myList = os.listdir(path)
# print(myList)
for x in myList:
    currentImage = cv2.imread(f'{path}/{Username}{pathad}')#replace x with Username
    images.append(currentImage)
    names.append(os.path.splitext(Username)[0])#replace 'x' with Username
    # print(images)
    # print(names)

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
def counter():
    counter.cont += 1
    return counter.cont
counter.cont=0

def markAttendance(name):
    # print("1")
    once=counter()
    # with open("interrupt.csv", 'w') as file:
    #     print("reach -11")
    #     file.write('-1' + "\n")
    #     file.close()
    # with open("interrupt.csv", 'a+') as file:
    #     print("reach -12")
    #     file.write('-1' + "\n")
    #     file.close()

    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        namelist = []
        # print("ABC");

        for line in myDataList:
            entry = line.split(',')
            namelist.append(entry[0])
        if name not in namelist:
            email_send.main()
            now = datetime.now()
            dtstring = now.strftime('%H:%M:%S')
            #***************************************#
            import mysql.connector
            from mysql.connector import errorcode
            try:
                connectt = mysql.connector.connect(
                    user='root',
                    password='',
                    host='127.0.0.1',
                    database='facerecognition'
                )
                print("It Works!!")
            except mysql.connector.Error as e:
                if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Something is wrong with username or Password")
                elif e.errno == errorcode.ER_BAD_DB_ERROR:
                    print("DataBase Does not exist")
                else:
                    print(e)
            cursor = connectt.cursor()

            selectquery = "select * from students"
            insertquery = "insert into attendance values(%s,%s,CURRENT_TIMESTAMP)"
            val = (admno,Username)
            cursor.execute(insertquery, val)
            connectt.commit()
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
            cursor.close()
            connectt.close
            #**************************************************#
            f.writelines(f'\n{name},{dtstring}')
            playsound('/Users/achiyant/Downloads/successfully marked.mp3');
        elif once==1:
            load.main(load2)
            print("Your attendance is already marked.")
            playsound('/Users/achiyant/Downloads/already.mp3')


            # break

            # email_send.main()
# markAttendance('aachiyant')

        # print(myDataList)


# markAttendance('a')

# for x in range(2):
#     sys.stdout.write('\rEncoding is in progress |')
#     time.sleep(0.1)
#     sys.stdout.write('\rEncoding is in progress /')
#     time.sleep(0.1)
#     sys.stdout.write('\rEncoding is in progress -')
#     time.sleep(0.1)
#     sys.stdout.write('\rEncoding is in progress \\')
#     time.sleep(0.1)
# print(images)
encodeListKnown = findEncodings(images)

sys.stdout.write('\rEncoding Complete\n')
cam = cv2.VideoCapture(0)

while True:
    _, img = cam.read()
    imgSmall = cv2.resize(img,  (0, 0), None, 0.25, 0.25)
    imgSmall = cv2.cvtColor(imgSmall, cv2.COLOR_BGR2RGB)

    faceCurrent = face_recognition.face_locations(imgSmall)
    encodeCurrent = face_recognition.face_encodings(imgSmall, faceCurrent)

    for encodeFace, faceLoc in zip(encodeCurrent, faceCurrent):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
        # print(faceDis)
        matchIndex = np.argmin(faceDis)
        if matches[matchIndex]:
            # k = cv2.waitKey(1)
            # if k % 256 == 32:
            name = names[matchIndex].upper()
            # print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            # cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            draw_border(img, (x1, y1), (x2, y2), (255, 255, 127), 2, 10, 20)
            cv2.rectangle(img, (x1, y2+40), (x2, y2+100), (200, 200, 200), 3)
            cv2.putText(img, name, (x1+6, y2+80), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            cv2.putText(img,'*If you want to stop Webcam press ''q'' *',(25,25),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markAttendance(name)
            # email_send.main()
        else:
            # print('No Match')
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            # cv2.rectangle(img, (xq1, y1), (x2, y2), (0, 0, 255), 2)
            draw_border(img, (x1, y1), (x2, y2), (255, 255, 127), 2, 10, 20)
            cv2.rectangle(img, (x1, y2 + 40), (x2+500, y2), (0, 0, 0), cv2.FILLED)
            text = '  ** Press ''q'' to quit this Window . **  '
            cv2.putText(img, 'You are not the eligible person for this account', (x1 + 6, y2+30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
    img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    # if count == 0:
    #     top = tkinter.Tk()
    #     top.geometry("100x100")
    #     top.withdraw()
    #     messagebox.showinfo('info', "Press q to quit")
    #     count += 1
    #     top.deiconify()
    #     top.destroy()
    #     top.quit()
    #     top.mainloop()
    cv2.imshow("WebCam", img)
    cv2.setWindowProperty("WebCam", cv2.WND_PROP_TOPMOST, 1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        quit()
cam.release()
cv2.destroyAllWindows()




