import smtplib

mailFrom = 'Automation system'
mailTo = ['piotr.posiadala@plus.pl','piotrekbuu@gmail.com']
mailSubject='Processing finished successfully'
mailBody='''

This is message sent from smtplib. 

Have a nice day!'''

message = '''From: {}
Subject: {}

{}
'''.format(mailFrom, mailSubject, mailBody)

user = 'python.udemy.1@gmail.com'
password = 'Kartofel12.'

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(user, password)
    server.sendmail(user, mailTo, message)
    server.close()
    print('Mail sent')
except:
    print("Error sending mail")