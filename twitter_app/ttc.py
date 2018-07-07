#!/usr/bin/python

import twitter
import datetime
from datetime import timedelta
import pytz
import calendar
import os
import sys
from readkeys import *
from send_gmail import *

def getLocalTime(date_in) :
    utc = datetime.datetime.strptime(date_in, '%a %b %d %H:%M:%S +0000 %Y')
    # TODO: deal with daylight saving time...
    #offset = -5
    #local_time = utc + timedelta(hours=offset)

    utc_tz = pytz.timezone('UTC')
    eastern_tz = pytz.timezone('US/Eastern')
    
    utc_time = utc_tz.localize(utc)
    local_time = utc_time.astimezone(eastern_tz)

    return local_time
    

def shouldPrintTweet(status) :
    debug_str = str(status.id) + ' '

    # Don't care if it's weekend (note: weekday() is 0 for Monday)
    local_time = getLocalTime(status.created_at)
    if local_time.weekday() >= 5 : 
        debug_str = debug_str + 'weekend'
        print(debug_str)
        return False

    # convert to lower cases, strip all white spaces
    tweet = ''.join(status.text.lower().split())

    include_any = ['line1', 'line2', 'line4']
    exclude_all = ['elevator']

    inc = False

    for w in include_any :
        if w in tweet :
            inc = True
            break

    # Doesn't have any include keywords. Don't need to filter excludes
    if inc == False :
        debug_str = debug_str + 'keyword'
        print(debug_str)
        return False

    for w in exclude_all :
        if w in tweet :
            debug_str = debug_str + 'excluded'
            print(debug_str)
            return False

    debug_str = debug_str + 'y'
    print(debug_str)
    return True

def printTweet(status, output) :
    local_time = getLocalTime(status.created_at)
    date_fmt = '%A %b-%d  %H:%M'
    out = ""
    #out = out + str(status.id) + '\n'
    out = out + local_time.strftime(date_fmt) + '\n' + status.text + '\n\n'
    
    return output + out

keys = readKeys('binkeys.apikey')

api = twitter.Api(consumer_key=keys[0],
                  consumer_secret=keys[1],
                  access_token_key=keys[2],
                  access_token_secret=keys[3])

# read the most recent status (MRS) id that we got last time
try :
    fileMRS = open('mrs.txt', 'r')
    MRS_id = int(fileMRS.readline())
    fileMRS.close()
except :
    # File not found? Bad id? Meh
    MRS_id = 0

if MRS_id == 0 :
    # MRS ID invalid. Just read the last 100
    statuses = api.GetUserTimeline(screen_name='TTCnotices', count=100)
    MRS_id = statuses[0].id
else :
    statuses = api.GetUserTimeline(screen_name='TTCnotices', since_id=MRS_id, count=100)
    if len(statuses) > 0 :
        MRS_id = statuses[0].id

fileMRS = open('mrs.txt', 'w')
fileMRS.write(str(MRS_id))
fileMRS.close()

timenow = datetime.datetime.now().strftime('%a %b-%d  %H:%M')
print(timenow + '  MRS=' + str(MRS_id) + '  len=' + str(len(statuses)))

if len(statuses) == 0 :
    sys.exit()

output = ""
for s in statuses :
    tweet = ''.join(s.text.lower().split())
    if shouldPrintTweet(s) :
        output = printTweet(s, output)

if not output :
    sys.exit()

email_subject = 'TTC Update: ' + timenow
send_gmail(email_subject, output)

#print(output)
