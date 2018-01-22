#!/usr/bin/python

import cgi
import cgitb
import os
import sys

cgitb.enable()
form = cgi.FieldStorage(keep_blank_values=0)

print "Content-type: text/html\n\n"


picfile = form['picfile']

#sys.exit()

outfile = open(picfile.filename, 'wb')
while 1:
    chunk = picfile.file.read(1000)
    if not chunk:
        break;
    outfile.write(chunk)
outfile.close()


print "Done!"


