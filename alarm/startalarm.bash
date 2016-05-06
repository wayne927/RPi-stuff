#!/bin/bash

# turn on the TV
echo "on 0" | cec-client -s > /dev/null

sleep 10

# set this client as the active source
echo "as" | cec-client -s > /dev/null

sleep 10

musicpath='/home/pi/Music'

Nfiles=`ls $musicpath | wc -l`

let "filenum=$RANDOM % $Nfiles + 1"

file=`ls $musicpath | head -$filenum | tail -1`

mpg123 --loop 20 "$musicpath/$file"


