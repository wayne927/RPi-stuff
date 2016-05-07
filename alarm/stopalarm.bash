#!/bin/bash

pkill mpg123

myalarmfile=/home/pi/alarm/startalarm.bash


current_crontab=`crontab -l`

# This shouldn't happen. If an alarm was triggered, there must have been a cron job
# not to mention the backup job should still be there.
if [ "$current_crontab" == "" ]; then
  crontab -r
  exit
fi


new_crontab=`echo "$current_crontab" | grep -v "$myalarmfile"`

# There weren't any other jobs left in the crontab
if [ "$new_crontab" == ""  ]; then
  crontab -r
  exit
fi

# If this was an empty line, it'd actually add a blank entry to the crontab
echo "$new_crontab" | crontab

crontab -l
