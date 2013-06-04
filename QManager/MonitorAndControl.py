#! /usr/bin/env python

import smtplib

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

class SendMail:
    def __init__(self,To):
        self.To = To
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
    def make_list(self,list_of_lines):
        self.message += '<ul>'
        self.message += ''.join(['<li>%s</li>'%l for l in list_of_lines])
        self.message += '</ul>'
    def Hn(self,string,n=1,center=False):
        options = ''
        if center:
            options += ' align="center"'
        self.message += "<h%d%s>%s</h%d>"%(n,options,string,n)

import os

class Disk:
    def __init__(self,mount):
        self.mount = mount
        self.full = None
        self.percent = None
        self.name = None
    def du(self):
        try:
            duline = os.popen('df -h | grep %s'%self.mount).readlines()
            self.full = duline[2]
            self.percent = duline[4]
        except(IndexError):
            pass
    def name_me(self):
        try:
            self.name = open(self.mount+'/README').read().split('(')[0][:-1]
        except(IOError):
            pass

class ParseFS:
    def __init__(self):
        self.home = '/home/obs/'
        self.grid_output = self.home+'Share/grid_output'
        self.datadirs = []
        self.lacies = []
        for i in range(2):
            self.datadirs.append(Disk(self.home+'data%d'%i))
            self.datadirs[-1].du()
            self.datadirs[-1].name_me()
        for disk in ('current_disk','on_deck_disk'):
            self.lacies.append(Disk(self.home+disk))
            self.datadirs[-1].du()
            self.datadirs[-1].name_me()
    def ls_list(self,path):
        return os.popen('ls -dt %s'%path).readlines()
