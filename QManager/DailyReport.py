#! /usr/bin/env python

import smtplib

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

class SendMail:
    def __init__(self):
        self.To = 'teampaper.teststats@blogger.com'
        self.domain = 'gmail.com'
        self.username = 'teampaper'
        self.passwd = 'b00lardy'
    def my_email(self):
        return self.username+'@'+self.domain
    def send_mail(self, subject, message, attachments=None):
        msg = MIMEMultipart()
        msg['To'] = self.To
        msg['From'] = self.my_email()
        msg['Subject'] = subject
        msg.attach(MIMEText(message,'html'))

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(self.username,self.passwd)
        server.sendmail(self.my_email(),[self.To],msg.as_string())
        server.quit()

class HtmlWriter:
    def __init__(self):
        self.message = ''
    def append_line(self,string):
        self.message += string+'<br>'
    def Hn(self,string,n=1):
        self.message += "<h%d>%s</h%d>"%(n,string,n)

class ParseFS:
    def __init__(self):
        self.home = '/home/obs/'
        self.datadirs = [self.home+'data'+str(d) for d in (0,1)]
        self.grid_output = self.home+'Share/grid_output'

H = HtmlWriter()

H.Hn('test')
H.append_line('WooHoo!!!')

S = SendMail()
S.send_mail('test',H.message)
