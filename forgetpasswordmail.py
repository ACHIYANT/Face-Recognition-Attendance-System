import smtplib as s
from datetime import datetime

# import auth
# import uiregister
# import  uilogin


def main():
    ob = s.SMTP("smtp.gmail.com",587)
    ob.starttls()
    ob.login("alert.attendancenotification@gmail.com", "password123@")
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
    # if True:
    #     db = open("database.csv", "r")
    #     d = []
    #     f = []
    #     ad = []
    #     email = []
    #     for i in db:
    #         a, b, no, mail = i.split(",")
    #         b = b.strip()
    #         no = no.strip()
    #         mail = mail.strip()
    #         d.append(a)
    #         f.append(b)
    #         ad.append(no)
    #         email.append(mail)
    #     data = dict(zip(d, email))
    #     address = data[UserName]
    listofaddress = address
    ob.sendmail("alert.attendancenotification@gmail.com", listofaddress, message)
    print("\nEmail Send Successfully")
    ob.quit()


if __name__ == "__main__":
    main()


# from ssl import create_default_context
# from email.message import EmailMessage
# import smtplib as s
#
# sender = 'alert.attendancenotification@gmail.com'
# description = "This is the test description supposed to be in body of the email."
# msg = EmailMessage()
# msg.set_content(description)
# msg['Subject'] = 'This is a test title'
# msg['From'] = f"Python SMTP <{sender}>"
# msg['To'] = 'hemabhagat05022013@gmail.com'
#
#
# def using_ssl():
#     try:
#         server = s.SMTP_SSL(host='smtp.gmail.com', port=465, context=create_default_context())
#         server.login(sender, 'password123@')
#         server.send_message(msg=msg)
#         server.quit()
#         server.close()
#     except s.SMTPAuthenticationError:
#         print('Login Failed')
#
#
# def using_tls():
#     try:
#         server = s.SMTP(host='smtp.gmail.com', port=587)
#         server.starttls(context=create_default_context())
#         server.ehlo()
#         server.login(sender, 'password123@')
#         server.send_message(msg=msg)
#         server.quit()
#         server.close()
#     except s.SMTPAuthenticationError:
#         print('Login Failed')