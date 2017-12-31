#!/bin/bash

alarmpath=/home/pi/alarm

# detect if the TV is connected
num=$( echo "scan" | cec-client -s -d 1 | grep TV | wc -l )
if [ "$num" -eq "0" ]; then
    echo "TV is not connected! Sending email."

    logfile=$alarmpath/scanlog_$(date "+%Y-%m-%d_%H.%M")
    echo "scan" | cec-client -s > $logfile
    $alarmpath/sendemail.sh $logfile
    rm $logfile
fi

# even if the TV is not on, don't stop trying anyway

# turn on the TV
echo "on 0" | cec-client -s > /dev/null

sleep 10

# set this client as the active source
echo "as" | cec-client -s > /dev/null

sleep 10

musicpath='/home/pi/Music'

# number of files in the music dir
Nfiles=`ls $musicpath | wc -l`

# pick a random number r
let "filenum=$RANDOM % $Nfiles + 1"

# choose the rth file in the dir
file=`ls $musicpath | head -$filenum | tail -1`

# play that music file 20 times
mpg123 --loop 20 "$musicpath/$file"


