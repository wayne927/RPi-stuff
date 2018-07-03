#!/usr/bin/python

import twitter
import datetime
from datetime import timedelta
import calendar
import os
import sys
from readkeys import *
from send_gmail import *

def getLocalTime(date_in) :
    utc = datetime.datetime.strptime(date_in, '%a %b %d %H:%M:%S +0000 %Y')
    # TODO: deal with daylight saving time...
    offset = -5
    local_time = utc + timedelta(hours=offset)

    return local_time
    

def shouldPrintTweet(status) :
    # Don't care if it's weekend (note: weekday() is 0 for Monday)
    local_time = getLocalTime(status.created_at)
    if local_time.weekday() >= 5 : 
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
        return False

    for w in exclude_all :
        if w in tweet :
            return False

    return True

def printTweet(status, output) :
    local_time = getLocalTime(status.created_at)
    out = ""
    #out = out + str(status.id) + '\n'
    out = out + calendar.day_name[local_time.weekday()] + " "
    out = out + str(local_time) + '\n' + status.text + '\n\n'
    
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
    fileMRS = fileMRS.close()
    print('Most recent status ID read from file = ' + str(MRS_id))
except :
    # File not found? Bad id? Meh
    MRS_id = 0

if MRS_id == 0 :
    print('MRS ID invalid. Just read the last 100.')
    statuses = api.GetUserTimeline(screen_name='TTCnotices', count=100)
    MRS_id = statuses[0].id
else :
    statuses = api.GetUserTimeline(screen_name='TTCnotices', since_id=MRS_id)
    print('Number of statuses since last MRS = ' + str(len(statuses)))
    if len(statuses) == 0 :
        sys.exit()
    else :
        MRS_id = statuses[0].id

fileMRS = open('mrs.txt', 'w')
fileMRS.write(str(MRS_id))
fileMRS.close()

output = ""

for s in statuses :
    tweet = ''.join(s.text.lower().split())
    if shouldPrintTweet(s) :
        output = printTweet(s, output)

if not output :
    sys.exit()

timenow = datetime.datetime.now()
email_subject = 'TTC Update: ' + timenow.strftime('%a %b %d %H:%M:%S')
send_gmail(email_subject, output)

print(output)
