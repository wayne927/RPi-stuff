#!/usr/bin/python

import twitter
import datetime
from datetime import timedelta
import calendar
import os

def shouldPrintTweet(status) :
    # Don't care if it's weekend
#    utc = datetime.datetime.strptime(status.created_at, '%a %b %d %H:%M:%S +0000 %Y')
#    offset = -5
#    local_time = utc + timedelta(hours=offset)
#    if local_time.weekday() > 5 : 
#        return False

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
    utc = datetime.datetime.strptime(status.created_at, '%a %b %d %H:%M:%S +0000 %Y')
    offset = -5

    local_time = utc + timedelta(hours=offset)
    print(calendar.day_name[local_time.weekday()] + " " +str(local_time))
    print(status.text + "\n")


api = twitter.Api(consumer_key='whF9lsCVHnQ7xvPHR9EW884o9',
                  consumer_secret='6lVTtmwykmvL93YJcwlpJWeMpAbakk2Mx9uXoTNhxqjVIi7jgh',
                  access_token_key='31615381-wuNig1XOjAXSpobB4winQGuEEjNE6rGJlJsCRn5sx',
                  access_token_secret='PDYqavTudQqh43fU1nKbUaQ6skaAwCoIoQMmT7zI2gAQD')



#print api.VerifyCredentials()

#statuses = api.GetUserTimeline(screen_name='wayne927', since_id=693671776426070016)

statuses = api.GetUserTimeline(screen_name='TTCnotices')
#GetUserTimeline(user_id=None, screen_name=None, since_id=None, max_id=None, count=None, include_rts=True, trim_user=False, exclude_replies=False)

#print("s length = " + str(len(statuses)))

most_recent_status = statuses[0]

print("Most recent tweet ID: " + str(most_recent_status.id))

for s in statuses :
#    print(s)
#    print("Date: " + s.created_at)
#    print("ID: " + str(s.id))
    tweet = ''.join(s.text.lower().split())

#    if ( 'line1' in tweet or 'line2' in tweet or 'line4' in tweet ) and ( 'elevator' not in tweet ) :
    if shouldPrintTweet(s) :
        printTweet(s)

        tweet_out = open('email.txt', 'w')
        tweet_out.write(s.created_at + "\n")
        tweet_out.write(s.text + "\n")
        tweet_out.close()



    


