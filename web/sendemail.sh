#!/bin/bash

to='wayne.ngan@gmail.com'
from='Raspbery Pi Alarm <wayne.ngan@rogers.com>'
timestamp=$(date "+%D %H:%M")
subject="ALARM EMAIL $timestamp"

sendmail $to << EOF
TO: $to
FROM: $from
SUBJECT: $subject
This is an email sent from the raspbery pi
EOF


