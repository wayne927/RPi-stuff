#!/usr/bin/python
import cgi
import cgitb
import os
import sys

cgitb.enable()

print "Content-type: text/html\n"

form = cgi.FieldStorage()

def has_var(var):
    return (var in form and form[var].value != "")

def write_file(text):
    outfile = open('../include/next-meeting.txt', 'w');
    outfile.write(text)
    outfile.close()

def done_writing(text):
    print "<h1>Updated!</h1>", text
    print "<br/><br/>"
    print "Go back to <a href='http://www.yoyotoronto.com'>yoyotoronto.com</a>"

if(has_var('custom-text')) :
    str = form['custom-text'].value
    write_file(str)
    done_writing(str)
    exit()

TBD = 0
    
uoft_map_url = "https://www.google.ca/maps?q=Bahen+Centre+for+Information+Technology,+Saint+George+Street,+Toronto,+ON&hl=en&sll=43.659994,-79.396246&sspn=0.003446,0.008256&oq=bahen&t=m&z=17&iwloc=A"

york_map_url = "https://www.google.ca/maps/place/Vari+Hall/@43.773042,-79.503556,17z/data=!4m2!3m1!1s0x0000000000000000:0x0244f1cd950ff986"

meet_date = "";
meet_time = "";
meet_locatoin = "";
meet_map_url = "";

if((not has_var('meet-date')) or (not has_var('meet-time'))) :
    TBD = 1;
else:
    meet_date = form['meet-date'].value
    meet_time = form['meet-time'].value
    
if(has_var('meet-location') and form['meet-location'].value == 'other'):
    if((not has_var('meet-location-other')) or (not has_var('meet-location-other-url'))):
        TBD = 1;
    else :
        meet_location = form['meet-location-other'].value;
        meet_location_url = form['meet-location-other-url'].value;
else :
    meet_location = form['meet-location'].value
    if(meet_location == "UofT"):
        meet_location_url = uoft_map_url
    else:
        meet_location_url = york_map_url
    

if(TBD == 1):
    str = "Next club meeting: TBD"
else:
    str = 'Next club meeting:&nbsp;&nbsp;&nbsp;' + meet_date + '<br/>' + meet_time + ' at ' + meet_location + " (<a href='" + meet_location_url + "' target='_blank'>Map</a>)"

write_file(str)
done_writing(str)

#print "<h1>Updated!</h1>", str
    
#if(has_var("place")):
#    print "meeting place is "+form["place"].value
    
    
