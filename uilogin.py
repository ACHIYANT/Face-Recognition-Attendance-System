import sys
import time
import cv2
import numpy as np
import face_recognition
import os, signal
from playsound import playsound
import load
from tkinter import *

from playsound import playsound
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

playsound('/Users/achiyant/Downloads/welcome.mp3')
with open("interrupt.csv", 'w') as file:
    file.write('-1' + "\n")
    file.close()
with open("interrupt.csv", 'a+') as file:
    file.write('-1' + "\n")
    file.close()

class login_sys:
    def __init__(self, master):

        self.master = master
        self.master.geometry("1440x900+0+0")
        self.master.title("Login     |    Register")
        self.img1 = ImageTk.PhotoImage(file="loginbackkk.jpeg")
        self.lbl_img1 = Label(master, image=self.img1, bd=0).place(x=-2, y=-2)

        frame = Frame(self.master, bd=0, relief=RIDGE, bg="#C7C2C8")
        frame.place(x=550, y=150, width=350, height=547)

        lbl_title = Label(frame, text="LOGIN   |   SIGNUP", font=("Comic Sans MS", 30, "bold"), bg="#C7C2C8").place(x=0,
                                                                                                                    y=30,
                                                                                                                    relwidth=1)
        lbl_user = Label(frame, text="Username", font=("Comic Sans MS", 20), bg="#C7C2C8", fg="#7395B0").place(x=50,
                                                                                                               y=150)
        self.user = StringVar()
        self.passw = StringVar()
        self.admno = StringVar()
        txt_user = Entry(frame, textvariable=self.user, font=("Comic Sans MS", 15), bg="#c7c2c8", bd=0).place(x=55,
                                                                                                              y=190,
                                                                                                              width=250)

        lbl_passw = Label(frame, text="Password", font=("Comic Sans MS", 20), bg="#C7C2C8", fg="#7395B0").place(x=50,
                                                                                                                y=230)
        txt_passw = Entry(frame, textvariable=self.passw, show="*", font=("Comic Sans MS", 15), bg="#c7c2c8",
                          bd=0).place(x=55, y=270, width=250)

        lbl_admno = Label(frame, text="Admission No.", font=("Comic Sans MS", 20), bg="#C7C2C8", fg="#7395B0").place(
            x=55,
            y=310)
        text_admno = Entry(frame, textvariable=self.admno, font=("Comic Sans MS", 15), bg="#c7c2c8", bd=0).place(x=55,
                                                                                                                 y=350,
                                                                                                                    width=250)

        btn_login = Button(frame, text="LOG IN", font=("Comic Sans MS", 15), fg="#000000",
                           highlightbackground="#7395B0", command=self.gainAccess, bd=0, activebackground="#FE0000",
                           cursor="hand").place(x=55, y=400, width=250, height=35)

        hr = Label(frame, bg="#ffffff").place(x=55, y=465, width=250, height=2)
        btn_forget = Button(frame, text="Forget Password ?", font=("Comic Sans MS", 15), fg="#000000",
                            highlightbackground="#7395B0", command=self.callforg, bd=0, activeforeground="#FE0000",
                            cursor="hand").place(x=110, y=507, width=125, height=35)

        frame2 = Frame(self.master, bd=0, relief=RIDGE, bg="#C7C2C8")
        frame2.place(x=550, y=750, width=350, height=60)

        lbl_dont = Label(frame2, text="Don't have an account ?", font=("Comic Sans MS", 20), bg="#C7C2C8",
                         fg="#7395B0").place(x=0, y=10)
        btn_reg = Button(frame2, text="Sign up", font=("Comic Sans MS", 15), fg="#000000",
                         highlightbackground="#7395B0", command=self.callsm, bd=0, activeforeground="#FE0000",
                         cursor="hand").place(x=230, y=17, width=115, height=25)

        def close_program():
            print("reach close")
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                master.destroy()
            with open("interrupt.csv", 'w') as file:
                print("reach 1091")
                file.write('109' + "\n")
                file.close()
            with open("interrupt.csv", 'a+') as file:
                print("reach 1092")
                file.write('109' + "\n")
                file.close()

        def disable_event():
            pass

        btn = Button(master, text="Click me to close", font=("Comic Sans MS", 10), bg="#C7C2C8",
                         fg="#7395B0",command=close_program).place(x=0, y=0)
        # btn.pack()
        master.protocol("WM_DELETE_WINDOW", disable_event)
        # print("Reach1")

        load1 = 'Authentication is in progress'

    def welcome(self):
        try:
            exit()
        except:
            print("Welcome To Face Recognition Based Attendance System.")

    def getusername(self):
        return self.user.get()

    def gainAccess(self):
        if not len(self.user.get() or self.passw.get() or self.admno.get()) < 1:

            if True:
                db = open("database.csv", "r")
                d = []
                f = []
                ad = []
                email = []
                for i in db:
                    a, b, no, mail = i.split(",")
                    b = b.strip()
                    no = no.strip()
                    mail = mail.strip()
                    # c = a, b
                    # print(a)
                    # print(b)
                    d.append(a)
                    f.append(b)
                    ad.append(no)
                    email.append(mail)
                    # x = 2
                data = dict(zip(d, zip(f, ad)))
                try:
                    if data[(self.user.get())]:
                        try:
                            if self.passw.get() == data[(self.user.get())][0] and self.admno.get() == \
                                    data[(self.user.get())][1]:
                                sys.stdout.write('\rLogin Success')
                                messagebox.showinfo("Information", "Login Success")
                                print("\nHi", self.user.get())
                                with open("user.csv", 'w') as file:
                                    file.write(self.user.get() + "\n")
                                    file.close()
                                with open("user.csv", 'a+') as file:
                                    file.write(self.user.get() + "\n")
                                    file.close()
                                with open("userURoll.csv", 'w') as fileroll:
                                    fileroll.write(self.admno.get() + "\n")
                                    fileroll.close()
                                with open("userURoll.csv", 'a+') as fileroll:
                                    fileroll.write(self.admno.get() + "\n")
                                    fileroll.close()
                                self.welcome()
                                master.destroy()

                            else:
                                print("Incorrect password or username or Admission no. 1")
                                messagebox.showerror("Error", "Incorrect password or username or Admission no.",
                                                     icon="error")
                        except:
                            print("Incorrect password or username or Admission no.")
                            messagebox.showerror("Error", "Incorrect password or username or Admission no.")
                    else:
                        print("Password or username doesn't exist please register below")
                        messagebox.showerror("Error", "Password or username doesn't exist please register below")
                except:
                    print("Password or username doesn't exist please register below")
                    messagebox.showerror("Error", "Password or username doesn't exist please register below")

            else:
                print("Error logging into the system")
                messagebox.showerror("Error", "Error ! Loggin into the system")

        else:
            print("Please attempt login again")
            messagebox.showerror("Error", "Please attempt login again")

    def callsm(self):
        import uiregister

    def callforg(self):
        import forgetpassword


master = Tk()
obj = login_sys(master)
master.mainloop()
