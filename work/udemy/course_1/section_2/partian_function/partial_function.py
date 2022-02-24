import smtplib
import functools


def send_info_email(user, password, mailFrom, mailTo, mailSubject, mailBody):

    message = '''From: {}
    Subject: {}
    
    {}'''.format(mailFrom, mailSubject, mailBody)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(user, password)
        server.sendmail(user, mailTo, message)
        server.close()
        print('mail sent')
        return True
    except:
        print('error sending email')
        return False


mailFrom = 'Your automation system'
mailTo = ['nagrodzkitom2@gmail.com']
mailSubject = 'Processing finished successfully'
mailBody = '''
Hello

This mail confirm that processing has finished without problems,

Hava a nice day!'''

user = 'nagrodzkitom2@gmail.com'
password = 'xxxx'


SendInfoEmailFromGmail = functools.partial(send_info_email, user, password, mailSubject='Execution alert')

SendInfoEmailFromGmail(mailFrom=mailFrom, mailTo=mailTo, mailBody=mailBody)