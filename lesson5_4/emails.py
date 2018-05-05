import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send(email, password):

    fromaddr = "elizabethanngreer@gmail.com"
    toaddr = email
    msg = MIMEMultipart()
    msg['From'] = "appname"
    msg['To'] = email
    msg['Subject'] = "Your appname password"

    body = "Dear user, \n\nYour password for your appname account is " + password + ". \n\nFrom,\nappname"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("elizabethanngreer@gmail.com", "Tinkygreen7")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)


