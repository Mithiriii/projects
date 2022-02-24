import smtplib

mailFrom = 'Your automation system'
mailTo = ['magazynpamieci@gmail.com', 'rafal@mobio24.eu']
mailSubject = 'Processing finished successfully'
mailBody = '''
Hello

This mail confirm that processing has finished without problems,

Hava a nice day!'''

message = '''From: {}
Subject: {}

{}'''.format(mailFrom, mailSubject, mailBody)

user = 'magazynpamieci@gmail.com'
password = ''

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(user, password)
    server.sendmail(user, mailTo, message)
    server.close()
    print('mail sent')
except:
    print('error sending email')