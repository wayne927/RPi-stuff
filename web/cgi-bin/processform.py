#!/usr/bin/python

import cgi
import cgitb
import os

form = cgi.FieldStorage()
cgitb.enable()

print "Content-type: text/html\n\n"
print "Thank you for registering!!"
print "<br><br>"

fname = form['fname'].value
lname = form['lname'].value
email = form['email'].value

print fname + "<br>"
print lname + "<br>"
print email + "<br>"

doc_root = os.environ['DOCUMENT_ROOT']
filename = doc_root + '/regdata/output.txt'

write_line = fname+', '+lname+', '+email

outfile = open(filename, 'w')
outfile.write(write_line)
outfile.close()

musicfile = form['musicupload'];

#print "<br>", type(musicfile), "<br>"

filename = doc_root + '/regdata/' + musicfile.filename

outfile = open(filename, 'wb')
while 1:
	chunk = musicfile.file.read(1000)
	if not chunk:
		break
	outfile.write(chunk)
outfile.close()

print "File stored as " + filename


