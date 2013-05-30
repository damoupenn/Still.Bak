#! /bin/bash

PASSWD="P9ls4R*@"
DEFAULT_HOSTS="$(echo still{1..4})"

HOSTS="${@:-${DEFAULT_HOSTS}}"
for HOST in $HOSTS
do
    echo $PASSWD | ssh-copy-id -i ~/.ssh/id_dsa.pub $HOST
    ssh $HOST "echo $PASSWD | ssh-copy-id -i ~/.ssh/id_dsa.pub qmaster"
done
