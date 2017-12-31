#!/bin/bash

logfile=$1

to='wayne.ngan@gmail.com'
from='Raspbery Pi Alarm <wayne.ngan@rogers.com>'
timestamp=$(date "+%D %H:%M")
subject="ALARM EMAIL $timestamp"

email=/home/pi/alarm/temp_email_body_$$
rm -f $email

echo "TO: $to" >> $email
echo "FROM: $from" >> $email
echo "SUBJECT: $subject" >> $email
cat $logfile >> $email

/usr/sbin/sendmail $to < $email

rm $email

