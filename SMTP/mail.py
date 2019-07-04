
"""
#!/usr/bin/python
import smtplib

sender = 'root@localhost'
receivers = ['joel@localhost','jessi@localhost']

message = """From: From Person <root@localhost>
To: To Person <joel@localhost>
Subject: SMTP e-mail test

This is a test e-mail message.
"""
try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)
   print ("Successfully sent email")
except SMTPException:
   print ("Error: unable to send email")

"""

#!/usr/bin/python
import smtplib

sender = 'enrique.abiel@gmail.com'
receivers = ['keshav.kummari@gmail.com']

message = """From: From Person <enrique.abiel@gmail.com>
To: To Person <keshav.kummari@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('smtp.gmail.com',465)
   smtpObj.sendmail(sender, receivers, message)
   print ("Successfully sent email")
except SMTPException:
   print ("Error: unable to send email")
