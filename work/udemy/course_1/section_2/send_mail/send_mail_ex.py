import smtplib

mailFrom = 'Your automation system'
mailTo = ['nagrodzkitom2@gmail.com']
mailSubject = 'Processing finished successfully'
mailBody = '''
Hello

This mail confirm that processing has finished without problems,

Hava a nice day!'''

message = '''From: {}
Subject: {}

{}'''.format(mailFrom, mailSubject, mailBody)

user = 'nagrodzkitom2@gmail.com'
password = 'xxxx'

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(user, password)
    server.sendmail(user, mailTo, message)
    server.close()
    print('mail sent')
except:
    print('error sending email')