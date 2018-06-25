#!/bin/bash

msg=$1

to='wayne.ngan@gmail.com'
from='TTC Subway alert <wayne.ngan@rogers.com>'
timestamp=$(date "+%A %D %H:%M")
subject="Subway delay $timestamp"

email=/home/pi/twitter_app/temp_email_body_$$
rm -f $email

echo "TO: $to" >> $email
echo "FROM: $from" >> $email
echo "SUBJECT: $subject" >> $email
cat $msg >> $email

/usr/sbin/sendmail $to < $email

rm $email

