#************************************
import sys
import time
import cv2
import numpy as np
import face_recognition
import os
from playsound import playsound
import load
import mysql.connector
from mysql.connector import errorcode
#************************************
#
from tkinter import *
# class Login_system:
#     def __init__(self,root):
#         self.root=root
#         self.root.title("Login")
#         self.root.geometry("1350x700+0+0")
#
# root=Tk()
# # obj=Login_system(root)
# root.mainloop()

# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
# from tkinter.ttk import *

# creates a Tk() object
# def main():
#     pass
class register_sys:
    def __init__(self,master):
        # self.master = Tk()

        # sets the geometry of main
        # root window
        self.master=master
        self.master.geometry("1440x900+0+0")
        self.master.title("Register")
        # label = Label(master,
        #               text="This is the main window")
        #
        # label.pack(pady=10)

        self.img1=ImageTk.PhotoImage(file="loginbackkk.jpeg")
        self.lbl_img1=Label(master,image=self.img1,bd=0).place(x=-2,y=-2)
        # a button widget which will open a
        # new window on button click
        # btn = Button(master,
        #              text="Click to open a new window",
        #              command=openNewWindow)
        # btn.pack(pady=10)
        # btn_login=Button(master,text="LOGIN",bg="#C7C2C8",command = master.destroy).place(x=0,y=0,width=250,height=35)
        # btn = Button(master, text = 'Click me !', bd = '5',
        #                           command = master.destroy)
        # btn.pack(side = 'top')
        # mainloop, runs infinitely
        frame=Frame(self.master,bd=0,relief=RIDGE,bg="#C7C2C8")
        frame.place(x=550,y=50,width=350,height=647)
        # master.wm_attributes('-transparent',1)
        lbl_title=Label(frame,text="SIGNUP",font=("Comic Sans MS",30,"bold"),bg="#C7C2C8").place(x=0,y=30,relwidth=1)

        self.user = StringVar()
        self.passw = StringVar()
        self.admno = StringVar()
        self.passwc= StringVar()
        self.emaile= StringVar()

        lbl_user=Label(frame,text="Username",font=("Comic Sans MS",20),bg="#C7C2C8",fg="#7395B0").place(x=50,y=150)
        txt_user=Entry(frame,textvariable=self.user,font=("Comic Sans MS",15),bg="#c7c2c8",bd=0).place(x=55,y=190,width=250)

        lbl_passw=Label(frame,text="Password",font=("Comic Sans MS",20),bg="#C7C2C8",fg="#7395B0").place(x=50,y=230)
        txt_passw=Entry(frame,textvariable=self.passw,show="*",font=("Comic Sans MS",15),bg="#c7c2c8",bd=0).place(x=55,y=270,width=250)

        lbl_passwc = Label(frame, text="Confirm Password", font=("Comic Sans MS", 20), bg="#C7C2C8", fg="#7395B0").place(x=50,
                                                                                                                y=310)
        txt_passwc = Entry(frame, textvariable=self.passwc, show="*", font=("Comic Sans MS", 15), bg="#c7c2c8",
                          bd=0).place(x=55, y=350, width=250)

        lbl_admno = Label(frame, text="Admission No.", font=("Comic Sans MS", 20), bg="#C7C2C8", fg="#7395B0").place(x=55,
                                                                                                               y=390)
        text_admno = Entry(frame, textvariable=self.admno, font=("Comic Sans MS", 15), bg="#c7c2c8", bd=0).place(x=55,
                                                                                                             y=430,
                                                                                                             width=250)
        lbl_email = Label(frame, text="Email", font=("Comic Sans MS", 20), bg="#C7C2C8", fg="#7395B0").place(x=50,
                                                                                                               y=470)
        txt_email = Entry(frame, textvariable=self.emaile, font=("Comic Sans MS", 15), bg="#c7c2c8", bd=0).place(x=55,
                                                                                                              y=510,
                                                                                                              width=250)

        btn_signup=Button(frame,text="Signup",font=("Comic Sans MS",15),fg="#000000",highlightbackground="#7395B0",command =self.register,bd=0,activebackground="#FE0000",cursor="hand").place(x=55,y=570,width=250,height=35)

        # hr=Label(frame,bg="#ffffff").place(x=55,y=465,width=250,height=2)
        # btn_forget=Button(frame,text="Forget Password ?",font=("Comic Sans MS",15),fg="#000000",highlightbackground="#7395B0",command = master.destroy,bd=0,activeforeground="#FE0000",cursor="hand").place(x=110,y=507,width=125,height=35)
        #
        #
        # frame2=Frame(self.master,bd=0,relief=RIDGE,bg="#C7C2C8")
        # frame2.place(x=550,y=750,width=350,height=60)
        #
        # lbl_dont=Label(frame2,text="Don't have an account ?",font=("Comic Sans MS",20),bg="#C7C2C8",fg="#7395B0").place(x=0,y=10)
        # btn_reg=Button(frame2,text="Sign up",font=("Comic Sans MS",15),fg="#000000",highlightbackground="#7395B0",command = master.destroy,bd=0,activeforeground="#FE0000",cursor="hand").place(x=230,y=17,width=115,height=25)

        #*******************************
    def register(self):
        # Username = input("Enter a username:")
        # Password1 = input("Create password:")
        # Password2 = input("Confirm Password:")
        # admno = input("Enter admission no .: ")
        # email = input("Enter your Email Id: ")
        db = open("database.csv", "r")
        d = []
        # print("12")
        for i in db:
            a, b, no, mail = i.split(",")
            # a=a.strip()
            b = b.strip()
            no = no.strip()
            mail = mail.strip()
            c = a, b, no, mail
            d.append(a)
            # d.append(no)

        if not len(self.passw.get()) <= 4:
            db = open("database.csv", "r")
            # print(123)
            if not self.user.get() == None:
                if len(self.user.get()) < 1:
                    print("Please provide a username")
                    messagebox.showerror("Error", "Please provide a username")
                    # register()
                elif self.user.get() in d:
                    print("Username exists please login below with correct credentials")
                    messagebox.showerror("Error", "Username exists please login below with correct credentials")
                    # self.gainAccess()
                else:

                    if self.passw.get() == self.passwc.get():
                        db = open("database.csv", "a")
                        db.write(self.user.get() + ", " + self.passw.get() + ", " + self.admno.get() + ", " + self.emaile.get() + "\n")
                        # **************************#
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
                        insertquery = "insert into students values(%s,%s,%s,%s)"
                        val = (self.admno.get(), self.user.get(), self.passw.get(), self.emaile.get())
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
                        # *******************#
                        cam = cv2.VideoCapture(0)
                        cv2.namedWindow("REGISTERING IMAGE")
                        img_counter = 0

                        # Username = "achi"
                        fext = '.jpeg'
                        imagepath = f'{self.user.get()}{fext}'

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

                        while True:
                            ret, frame = cam.read()
                            frame = cv2.resize(frame, None, fx=0.4, fy=0.4, interpolation=cv2.INTER_AREA)
                            imgSmall = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
                            faceCurrent = face_recognition.face_locations(imgSmall)
                            for faceloc in faceCurrent:
                                y1, x2, y2, x1 = faceloc
                                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                                # cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)
                                draw_border(frame, (x1, y1), (x2, y2), (255, 255, 127), 2, 10, 20)
                            if not ret:
                                print("Failed to grab frame")
                                messagebox.showerror("Error", "Failed to grsb frame")
                                break

                            cv2.imshow("Registering Window", frame)
                            k = cv2.waitKey(1)
                            if k % 256 == 27:
                                # ESC pressed
                                print("Escape hit, closing...")
                                messagebox.showerror("Error", "You are not registered yet please register again")
                                print("You are not registered yet please register again")
                                quit()
                                break
                            elif k % 256 == 32:
                                # SPACE pressed
                                # img_name = "opencv_frame_{}.png".format(img_counter)
                                path = '/Users/achiyant/PycharmProjects/FaceRecognition/ImagesRegistered'
                                cv2.imwrite(os.path.join(path, imagepath), frame)
                                print("{} written!".format(imagepath))
                                img_counter += 1
                                break

                        cam.release()
                        cv2.destroyAllWindows()

                        print("User created successfully!")
                        messagebox.showerror("Error", "User Created Successfully \n please proceed to login")
                        print("Please login to proceed:")
                        master.destroy()
                        # time.sleep(5)
                        # gainAccess()
                        # home()
                        # res()

                    else:
                        print("Passwords do not match")
                        messagebox.showerror("Error", "Passwords do not match")
                        # register()

        else:
            print("Password too short")
            messagebox.showerror("Error", "Password too short")
            # register()

        # def home(option=None):
        #     # cause_to_do_something()
        #     print("Welcome, please select an option")
        #     option = input("Login | Signup:")
        #     if option == "l":
        #         # self.gainAccess()
        #     elif option == "s":
        #         # register()
        #     else:
        #         print("Please enter a valid parameter, this is case-sensitive")
        #         # home()
            # register(Username, Password1, Password2)
            # gainAccess(Username, Password1)

            # home()//uncomment this...

            #
    if __name__ == "__init__":
        __init__()

            # *******************************


master=Toplevel()
obj=register_sys(master)
master.mainloop()
# if __name__ == "__main__":
#     main()