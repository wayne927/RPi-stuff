#!/usr/bin/python

import cgi
import cgitb
import os
import sys

print "Content-type: text/html\n"

cgitb.enable()
form = cgi.FieldStorage(keep_blank_values=0)
doc_root = os.environ['DOCUMENT_ROOT']

outpath = doc_root+"/PicTransfer/files/"

if not os.path.exists(outpath):
    os.makedirs(outpath)

picfiles = form['picfile']

if not isinstance(picfiles, list):
    templist = list()
    templist.append(picfiles)
    picfiles = templist

for thisfile in picfiles:
    if not thisfile.filename:
        break
    fout = open(outpath+thisfile.filename, 'wb')
    while 1:
        chunk = thisfile.file.read(1000)
        if not chunk:
            break;
        fout.write(chunk)
    fout.close()

print "<html><head>"
print "<script>function gohome() { window.location = '/PicTransfer' }</script>"
print "</head><body onload='gohome()'>\n"

print "</body></html>"

