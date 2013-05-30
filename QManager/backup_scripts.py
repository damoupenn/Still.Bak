#! /usr/bin/env python

import os
from datetime import date

EndDir = '/home/obs/Still.Bak/'
Backups = [
    '/home/obs/Share/scripts/*',
    '/home/obs/QManager',
    '/home/obs/SetupUtils']

for B in Backups:
    command = 'cp -r %s %s'%(B,EndDir)
    os.system(command)

os.system('rsync -zru /home/obs/Still.Bak damo@agena.physics.upenn.edu:~/')
