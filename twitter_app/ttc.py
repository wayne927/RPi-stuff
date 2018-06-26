#!/usr/bin/python

import twitter
import datetime
from datetime import timedelta
import calendar
import os
import sys
from readkeys import *

def getLocalTime(date_in) :
    utc = datetime.datetime.strptime(date_in, '%a %b %d %H:%M:%S +0000 %Y')
    offset = -5
    local_time = utc + timedelta(hours=offset)

    return local_time
    

def shouldPrintTweet(status) :
    # Don't care if it's weekend
    local_time = getLocalTime(status.created_at)
    if local_time.weekday() > 5 : 
        return False

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

def printTweet(status) :
    local_time = getLocalTime(status.created_at)
    print(calendar.day_name[local_time.weekday()] + " " +str(local_time))
    print(status.text + "\n")

keys = readKeys('binkeys.apikey')

api = twitter.Api(consumer_key=keys[0],
                  consumer_secret=keys[1],
                  access_token_key=keys[2],
                  access_token_secret=keys[3])

statuses = api.GetUserTimeline(screen_name='TTCnotices')

most_recent_status = statuses[0]

print("Most recent tweet ID: " + str(most_recent_status.id))

for s in statuses :
    tweet = ''.join(s.text.lower().split())

    if shouldPrintTweet(s) :
        printTweet(s)

