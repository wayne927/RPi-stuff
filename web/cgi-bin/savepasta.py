#!/usr/bin/python

import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()

if ('pasta' in form) :
    str = form['pasta'].value;
else :
    str = ""
    
outfile = open('../copypasta/pasta.txt', 'w');
outfile.write(str);
outfile.close();


print "Content-type: text/html\n"
print "<html><head><style> body {font-family: sans-serif; font-size:70px}"
print "#time-box { display: inline-block; font-size: 80px; padding: 20px; background-color: #AAFFAA; }"
print "</style>"
print "<script>function gohome() { window.location = '/copypasta/index.html' }</script>"
print "</head><body onload='gohome()'>\n"

print "</body></html>"
