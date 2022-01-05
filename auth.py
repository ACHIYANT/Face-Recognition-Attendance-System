import sys
import time
import cv2
import numpy as np
import face_recognition
import os
from playsound import playsound
import load








load1='Authentication is in progress'

playsound('/Users/achiyant/Downloads/welcome.mp3');
data = ''
UserName = ''
# email=''
def welcome():
    # print(getdata())
    try:
        print("abc")
        exit()
    except:
        # exit()
        print("Welcome To Face Recognition Based Attendance System.")
    # break
def getusername():
    return UserName


# if call_get:
#     return getusername()
# def getemail():
#     return email


# def res():
#     try:
#         exit()
#     except:
#         # exit()
#         # print("Welcome To Face Recognition System.")
#         gainAccess()


def gainAccess(Username=None, Password=None, admno=None,email=None):
    global data
    global UserName
    UserName = input("Enter your username:")
    Password = input("Enter your Password:")
    admno = input("Enter your admission no.:")
    if not len(UserName or Password or admno) < 1:

        if True:
            db = open("database.csv", "r")
            d = []
            f = []
            ad = []
            email = []
            for i in db:
                a, b, no, mail = i.split(",")
                # a=a.strip()
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
            # , zip(f, ad)
            # print(data)
            # print("1", data[(Username)][0])

            try:
                if data[(UserName)]:
                    try:
                        if Password == data[(UserName)][0] and admno == data[(UserName)][1]:
                            # for x in range(3):
                            #         sys.stdout.write('\rAuthentication is in progress |')
                            #         time.sleep(0.1)
                            #         sys.stdout.write('\rAuthentication is in progress /')
                            #         time.sleep(0.1)
                            #         sys.stdout.write('\rAuthentication is in progress -')
                            #         time.sleep(0.1)
                            #         sys.stdout.write('\rAuthentication is in progress \\')
                            #         time.sleep(0.1)
                            # load1,load2,load3,load4='Authentication is in progress'
                            load.main(load1)
                            sys.stdout.write('\rLogin Success')
                            # print("\nLogin success!")
                            print("\nHi", UserName)
                            welcome()
                        else:
                            print("Incorrect password or username or Admission no.")
                            gainAccess()
                    except:
                        print("Incorrect password or username or Admission no.")
                        gainAccess()
                else:
                    print("Password or username doesn't exist please register below")
                    register()
            except:
                print("Password or username doesn't exist please register below")
                register()

        else:
            print("Error logging into the system")
            home()

    else:
        print("Please attempt login again")
        gainAccess()
    # return Username

    # b = b.strip()


# accessDb()


def register(Username=None, Password1=None, Password2=None, admno=None, email=None):
    Username = input("Enter a username:")
    Password1 = input("Create password:")
    Password2 = input("Confirm Password:")
    admno = input("Enter admission no .: ")
    email = input("Enter your Email Id: ")
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

    if not len(Password1) <= 4:
        db = open("database.csv", "r")
        # print(123)
        if not Username == None:
            if len(Username) < 1:
                print("Please provide a username")
                register()
            elif Username in d:
                print("Username exists please login below with correct credentials")
                gainAccess()
            else:

                if Password1 == Password2:
                    db = open("database.csv", "a")
                    db.write(Username + ", " + Password1 + ", " + admno + ", " + email + "\n")
                    cam = cv2.VideoCapture(0)
                    cv2.namedWindow("REGISTERING IMAGE")
                    img_counter = 0

                    # Username = "achi"
                    fext = '.jpeg'
                    imagepath = f'{Username}{fext}'

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
                            print("failed to grab frame")
                            break

                        cv2.imshow("Registering Window", frame)
                        k = cv2.waitKey(1)
                        if k % 256 == 27:
                            # ESC pressed
                            print("Escape hit, closing...")
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
                    print("Please login to proceed:")
                    quit()
                    # time.sleep(5)
                    # gainAccess()
                    # home()
                    # res()

                else:
                    print("Passwords do not match")
                    register()

    else:
        print("Password too short")
        register()


def home(option=None):
    # cause_to_do_something()
    print("Welcome, please select an option")
    option = input("Login | Signup:")
    if option == "l":
        gainAccess()
    elif option == "s":
        register()
    else:
        print("Please enter a valid parameter, this is case-sensitive")
        home()
# register(Username, Password1, Password2)
# gainAccess(Username, Password1)

home()



#
# if __name__ == "__main__":
#     main()
