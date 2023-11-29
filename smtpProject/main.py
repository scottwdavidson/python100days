from smtplib import SMTP
import os

'''
Sensitive data is stored in environmental variables w/in PyCharm as follows: 
  export <env var>=<value> 
  
Note: no spaces around "=" sign
'''

GMAIL_SMTP_URL = "smtp.gmail.com"
SCOTT_DAVIDSON_GMAIL_USERNAME = "sdavi1010@gmail.com"
SCOTT_DAVIDSON_GMAIL_APP_PASSWORD_ENVIRON_VARIABLE = "SCOTT_DAVIDSON_GMAIL_APP_PASSWORD"
password = os.environ.get(SCOTT_DAVIDSON_GMAIL_APP_PASSWORD_ENVIRON_VARIABLE)
print(password)
EMAIL_CONTENT = "Subject:Hello from Python 2\n\nHello, Scott - testing 1 .. 2 .. 3 .. "

with SMTP(GMAIL_SMTP_URL) as connection:
    connection.starttls()
    connection.login(user=SCOTT_DAVIDSON_GMAIL_USERNAME, password=password)
    connection.sendmail(from_addr=SCOTT_DAVIDSON_GMAIL_USERNAME,
                  to_addrs="scott@scott-davidson.com",
                  msg=EMAIL_CONTENT)
