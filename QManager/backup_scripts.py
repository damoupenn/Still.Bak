#! /usr/bin/env python

import os
from datetime import date

EndDir = '/home/obs/Still.Bak/'
BackupDirs = [
    '/home/obs/Share/scripts/*',
    '/home/obs/QManager',
    '/home/obs/SetupUtils']

for B in BackupDirs:
    command = 'cp -r %s %s'%(B,EndDir)
    os.system(command)

ETCFiles = [
    '/etc/network/interfaces',
    '/etc/hosts',
    '/etc/fstab',]

if not os.path.exists(EndDir+'ETC'):
    os.system('mkdir %sETC'%EndDir)
for f in ETCFiles:
    command = 'cp %s %sETC/'%(f.split('/')[-1] + '.bak',EndDir)
    os.system(command)

os.system('rsync -zru /home/obs/Still.Bak damo@agena.physics.upenn.edu:~/')
