#! /bin/bash

HOSTS="$(echo Still{1..4})"

for HOST in $HOSTS; do
    echo "sending $1 to $2"
    rsync -rvuP $1 $HOST:$2
done
