#! /bin/bash

HOSTS="$(echo Still{1..4})"

for HOST in $HOSTS; do
    echo "HOSTNAME: $HOST"
    ssh -q -o ConnectTimeout=3 $HOST "$*"
    if [ $? -ne 0 ]; then
        echo "---COULD NOT CONNECT TO HOST---"
    fi
done
