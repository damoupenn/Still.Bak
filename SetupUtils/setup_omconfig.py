#! /usr/bin/env python

import sys,os

for line in open('omconfig_help.txt').readlines():
    if line.startswith('event'):
        event = line.split('Set')[0]
        event = event.split('=')[1]
        command = '/opt/dell/srvadmin/bin/omconfig system alertaction event=%s alert=true broadcast=true execappath="/usr/bin/om-alert.sh"' % event
        print command
        os.system(command)
