#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
import string
import time
from email.mime.text import MIMEText
from email.header import Header
from urllib2 import urlopen
 
def get_current_date():
    return time.strftime("%Y-%m-%d %a %H:%M:%S ", time.localtime()) 

def get_current_IP():
    return urlopen('http://ip.42.pl/raw').read()

def send_email(to_email,msg):
    sender = 'send@aliyun.com'
    receiver = to_email

    mail_host = "smtp.aliyun.com"
    mail_pwd = '#'

    message = MIMEText('Raspberry pi address report','plain','utf-8')
    message['From'] = 'sender<send@aliyun.com>'
    message['To'] = 'receiver'

    subject = msg
    message['Subject'] = Header(subject,'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host,25)
        smtpObj.login(sender,mail_pwd)
        smtpObj.sendmail(sender,receiver,message.as_string())
        print "success"

    except smtplib.SMTPException as e:
        print "failed %s" % e

if __name__=="__main__":
    to_addr = 'receiver@163.com'
    message = get_current_date() + 'The PI\'s IP:'  + get_current_IP()
    send_email(to_addr,message)