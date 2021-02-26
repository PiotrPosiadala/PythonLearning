import smtplib
import functools

def SendInfoEmail(user,password, mailFrom, mailTo, mailSubject, mailBody):
    message = '''From: {}
    Subject: {}

    {}
    '''.format(mailFrom, mailSubject, mailBody)


    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(user, password)
        server.sendmail(user, mailTo, message)
        server.close()
        print('Mail sent')
        return True
    except:
        print("Error sending mail")
        return False


mailFrom = 'Automation system'
mailTo = ['piotr.posiadala@plus.pl','piotrekbuu@gmail.com']
mailSubject='Processing finished successfully'
mailBody='''
This is message sent from smtplib. 
Have a nice day!'''
user = 'python.udemy.1@gmail.com'
password = 'Kartofel12.'


SendInfoEmailFromGmail = functools.partial(SendInfoEmail, user, password, mailSubject='Execution alert')
SendInfoEmailFromGmail(mailFrom = mailFrom, mailTo = mailTo, mailBody = mailBody)

#SendInfoEmail(user, password, mailFrom, mailTo, mailSubject, mailBody)
