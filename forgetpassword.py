from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import forgetpasswordmail

class forget_sys:
    def __init__(self,master):

        self.master=master
        self.master.geometry("1440x900+0+0")
        self.master.title("Forget Password")
        self.img1=ImageTk.PhotoImage(file="loginbackkk.jpeg")
        self.lbl_img1=Label(master,image=self.img1,bd=0).place(x=-2,y=-2)
        frame=Frame(self.master,bd=0,relief=RIDGE,bg="#C7C2C8")
        frame.place(x=550,y=100,width=350,height=595)

        lbl_title=Label(frame,text="FORGET PASSWORD",font=("Comic Sans MS",30,"bold"),bg="#C7C2C8").place(x=0,y=30,relwidth=1)

        self.user = StringVar()
        self.admno = StringVar()
        self.emaile= StringVar()

        lbl_user=Label(frame,text="Username",font=("Comic Sans MS",20),bg="#C7C2C8",fg="#7395B0").place(x=50,y=150)
        txt_user=Entry(frame,textvariable=self.user,font=("Comic Sans MS",15),bg="#c7c2c8",bd=0).place(x=55,y=190,width=250)

        lbl_admno = Label(frame, text="Admission No.", font=("Comic Sans MS", 20), bg="#C7C2C8", fg="#7395B0").place(x=55,
                                                                                                               y=230)
        text_admno = Entry(frame, textvariable=self.admno, font=("Comic Sans MS", 15), bg="#c7c2c8", bd=0).place(x=55,
                                                                                                             y=270,
                                                                                                             width=250)
        lbl_email = Label(frame, text="Email", font=("Comic Sans MS", 20), bg="#C7C2C8", fg="#7395B0").place(x=50,
                                                                                                               y=310)
        txt_email = Entry(frame, textvariable=self.emaile, font=("Comic Sans MS", 15), bg="#c7c2c8", bd=0).place(x=55,
                                                                                                              y=350,
                                                                                                              width=250)

        btn_signup=Button(frame,text="Submit Request",font=("Comic Sans MS",15),fg="#000000",highlightbackground="#7395B0",command =self.forget,bd=0,activebackground="#FE0000",cursor="hand").place(x=55,y=410,width=250,height=35)

        btn_mail = Button(frame, text="Send Mail", font=("Comic Sans MS", 15), fg="#000000",
                        highlightbackground="#7395B0", command=self.forgmail, bd=0, activebackground="#FE0000",
                        cursor="hand").place(x=55, y=485, width=250, height=35)
    def forget(self):
        if not len(self.user.get() or self.admno.get() or self.emaile.get()) < 1:
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
                data = dict(zip(d, zip(email, ad)))
                print(data)

                try:
                    if data[(self.user.get())]:
                        try:
                            if self.emaile.get() == data[(self.user.get())][0] and self.admno.get() == data[(self.user.get())][1]:
                                sys.stdout.write('\rForgetting your password ...')
                                messagebox.showinfo("Information", "Your request get verified click on 'SEND MAIL' button to get password on mail.")
                                # print("\nLogin success!")
                                # print("\nHi", self.user.get())
                                # dbu = open("user.csv", "a")
                                # dbu.flush()
                                # dbu.write(self.user.get() + "\n")
                                # dbu.close()
                                # dbu.flush()
                                # dbp=open("user.csv","a")
                                with open("user.csv", 'w') as file:
                                    file.write(self.user.get()+"\n")
                                    # input('Press enter to continue')
                                    file.close()
                                # input('Press enter to continue')
                                with open("user.csv", 'a+') as file:
                                    file.write(self.user.get()+"\n")
                                    file.close()
                                    # print(self.getusername())
                                # self.welcome()
                                # forgetpasswordmail.main()
                                # dbp=open("user.csv","r")
                                # master.destroy()

                            else:
                                print("Your details not match.0")
                                messagebox.showerror("Error", "Your details not match.",icon="error")
                                # self.gainAccess()
                        except:
                            print("Your details not match.1")
                            messagebox.showerror("Error", "Your details not match.")
                            # self.gainAccess()
                    else:
                        print("Password or username doesn't exist please register below")
                        messagebox.showerror("Error", "Password or username doesn't exist please register below")
                        # self.register()
                except:
                    print("Password or username doesn't exist please register below")
                    messagebox.showerror("Error", "Password or username doesn't exist please register below")
                    # self.register()

            else:
                print("Error logging into the system")
                messagebox.showerror("Error", "Error ! Loggin into the system")
                # home()

        else:
            print("Please attempt login again")
            messagebox.showerror("Error", "Please attempt login again")
    def forgmail(self):
        forgetpasswordmail.main()

    if __name__ == "__init__":
        __init__()

master=Toplevel()
obj=forget_sys(master)
master.mainloop()