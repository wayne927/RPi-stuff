#!/usr/bin/python

import cgi
import cgitb
import os
import sys
import subprocess

cgitb.enable()
print "Content-type: text/html\n"
print "<html><head><style> body {font-family: sans-serif; font-size:70px}"
print "#time-box { display: inline-block; font-size: 80px; padding: 20px; background-color: #AAFFAA; }"
print "</style></head><body>\n"

#command = 'echo on 0 | cec-client -s > /dev/null'

form = cgi.FieldStorage()

def has_var(var):
    return (var in form and form[var].value != "")

if(has_var("remove_alarm")):
    command = "crontab -r > /dev/null"
    os.system(command)
    print "Alarm removed!"

elif(has_var("check_crontab")):
    try:
        output = subprocess.check_output(['crontab','-l'])
        print output
    except:
        print "Crontab empty."

elif(has_var("alarm_hour") and has_var("alarm_minute")):
    hour = int(form['alarm_hour'].value)
    minute = int(form['alarm_minute'].value)
    
    if(hour < 0 or hour > 23 or minute < 0 or minute > 59):
        print "Invalid time format. Try again"
    else:
        command = "/home/pi/alarm/setalarm.bash %s %s > /dev/null" % (hour, minute)
        os.system(command)
        print "Alarm set: <br/><div id='time-box'>%s:%s</div>" % (hour, minute)

else:
    print "Input error. Try again."

print "</body></html>"
