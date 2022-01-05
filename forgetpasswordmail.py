import smtplib as s
from datetime import datetime

# import auth
# import uiregister
# import  uilogin


def main():
    ob = s.SMTP("smtp.gmail.com",587)
    ob.starttls()
    ob.login("enteryouremailid@gmail.com", "enteryourpassword")
    now = datetime.now()
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
            d.append(a)
            f.append(b)
            ad.append(no)
            email.append(mail)
        data = dict(zip(d, email))
        data1 = dict(zip(d, f))
        with open('user.csv', 'r') as f:
            lines = f.read().splitlines()
            last_line = lines[-1]
        UserName = last_line
        address = data[UserName]
        passw = data1[UserName]
    d1 = now.strftime("%B %d, %Y at %H:%M:%S")
    subject = "Forget Password notification"
    body = "your request for Forget Password is successfully fulfilled and your password is "
    message = "Subject:{}\n\n{}, {}{}".format(subject, UserName, body, passw)
    print(message)
    listofaddress = address
    ob.sendmail("enteryourmailid@gmail.com", listofaddress, message)
    print("\nEmail Send Successfully")
    ob.quit()


if __name__ == "__main__":
    main()


