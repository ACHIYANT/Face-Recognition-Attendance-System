import smtplib as s
from datetime import datetime

def main():
    ob = s.SMTP("smtp.gmail.com",587)
    ob.starttls()
    ob.login("enteryourmailid@gmail.com", "enteryourpasswordofemail")
    now = datetime.now()
    d1 = now.strftime("%B %d, %Y at %H:%M:%S")
    subject = "Attendance notification"
    body = "your attendace is marked for "
    with open('user.csv', 'r') as f:
        lines = f.read().splitlines()
        last_line = lines[-1]
    UserName = last_line
    message = "Subject:{}\n\n{}, {}{}".format(subject, UserName, body, d1)
    print(message)
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
        address = data[UserName]
    listofaddress = address
    ob.sendmail("enteryourmailid@gmail.com", listofaddress, message)
    print("\nEmail Send Successfully")
    ob.quit()


if __name__ == "__main__":
    main()


