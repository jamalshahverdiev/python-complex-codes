#!/usr/bin/env python

import smtplib

user = 'smtprelayuser'
pwd = 'Securep@$$'

FROM = 'username@domain.az'
TO = ['username@gmail.com']
SUBJECT = 'Test email from Sales'
TEXT = 'Testing sending mail using exchange servers'

# Prepare actual message
message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

try:
    server = smtplib.SMTP("mail.domain.az", 25)
    server.set_debuglevel(1)
    server.ehlo('mail.domain.az')
    server.esmtp_features['auth'] = 'LOGIN'
    server.login(user, pwd)
    server.sendmail(FROM, TO, message)
    server.close()
    print 'Successfully sent the mail'
except:
    print 'Failed to send mail'
