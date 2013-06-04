#! /usr/bin/env python
"""
Send an email to paperstats.blogger.com filled with the following information:
    - Summary plot of yesterday's RFI flags
    - Summary of yesterday's data compression
    - Summary of EoR Campaign to date.
    - disk usage.
        - pot0:/data0
        - pot0:/data1
        - QMaster:~/current_disk
        - QMaster:~/on_deck_disk
    - Summary of daily move to shredder.
"""

import MonitorAndControl as MnC

H = MnC.HtmlWriter()
FS = MnC.ParseFS()

######################
# Compression Status #
######################
H.Hn('Compression Status',center=True)

#####################
# Campaign Summmary #
#####################
H.Hn('Campaign Summary',center=True)

##############
# Disk Usage #
##############

H.Hn('Disk Usage',center=True)
for pot in range(2):
    d = FS.datadirs[pot]
    H.Hn('pot%d:'%pot,n=2)
    stanza = []
    if d.percent is None:
        stanza.append('Not mounted to system')
    else:
        stanza.append('Mounted on %s'%d.mount)
        stanza.append('%s\% full, which is %s'%(d.percent,d.full))
    H.make_list(stanza)

for lac in range(2):
    d = FS.lacies[lac]
    if d.name is None:
        H.Hn('No Disk mounted to %s'%d.mount,n=2)
    else:
        stanza = []
        H.Hn(d.name+':',n=2)
        stanza.append('Mounted on %s'%d.mount)
        stanza.append('%s\% full, which is %s'%(d.percent,d.full))
        H.make_list(stanza)

S = MnC.SendMail(To='teampaper.teststats@blogger.com')
S.send_mail('test',H.message)
