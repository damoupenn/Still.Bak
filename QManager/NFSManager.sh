#! /bin/bash

#MOUNT
if [ "${1}" == "-m" -o "${1}" == "--mount" ]
then
    echo "+++ /home/obs/Share +++"
    su-allhosts.sh "mount -v -t nfs -o rw qmaster:/home/obs/Share /home/obs/Share"
fi

#UMOUNT
if [ "${1}" == "-u" -o "${1}" == "--umount" ]
then
    echo "+++ /home/obs/Share +++"
    su-allhosts.sh "umount /home/obs/Share"
fi

