#!/usr/bin/python

import cgi
import cgitb
import os
import sys

cgitb.enable()
form = cgi.FieldStorage(keep_blank_values=0)

print "Content-type: text/html\n\n"

def missing_music(div):
    return (div not in form or form[div].filename == "")

required_fields = ['email', 'fname', 'lname', 'street', 'city', 'province', 'country',
       'postal'];

def check_fields():
    required_field_names = ['Email', 'First name', 'Last name', 'Street', 'City', 'Province', 
       'Country', 'Postal code']

    missing_fields = []

    for i in range(0,len(required_fields)):
        if(required_fields[i] not in form or form[required_fields[i]].value == ""):
            missing_fields.append(required_field_names[i])

    if(len(missing_fields) > 0):
        print "The following fields are missing:<br/>"
        print ", ".join(missing_fields), "<br/>"
        print "<p>Please go back and fill them, and then submit again</p>"
        sys.exit(0)

    divs = form.getlist('division')
    if(len(divs) == 0):
        print "<p>Please choose at least one divison to compete in </p>"
        sys.exit(0)

    if('1A' in divs or 'Open' in divs):
        if(missing_music('musicfile1aprelim') and missing_music('musicfile1afinal')
           and missing_music('musicfileopen')):
            print "<p>You did not upload any music. Please go back and select a music file, and then submit again</p>"
            sys.exit(0)
       

check_fields()

doc_root = os.environ['DOCUMENT_ROOT']


# -------- music upload ----------
def upload_music(div):
    first_name = form['fname'].value
    last_name = form['lname'].value
    
    if(div == 'musicfile1aprelim'):
        suffix = '1Aprelim'
    elif(div == 'musicfile1afinal'):
        suffix = '1Afinal'
    else:
        suffix = 'Open'

    music_dir = os.path.join(doc_root, 'regdata', first_name+'-'+last_name+'_'+suffix)
    
    if(not os.path.exists(music_dir)):
        os.mkdir(music_dir)
    
    
    music_item = form[div]
    
    filename = os.path.join(music_dir, music_item.filename)
    
    outfile = open(filename, 'wb')
    while 1:
        chunk = music_item.file.read(1000)
        if not chunk:
            break;
        outfile.write(chunk)
    outfile.close()

    return filename

# -------

music_divs = ['musicfile1aprelim', 'musicfile1afinal', 'musicfileopen']

music_filenames = []

for d in music_divs:
    if(not missing_music(d)):
        filename = upload_music(d)
    else:
        filename = '-'
    music_filenames.append(filename)



filename = os.path.join(doc_root, 'regdata/regdata.csv')

outfile = open(filename, 'a')

write_line = []
for f in required_fields:
    write_line.append(form[f].value)

divs = ['1A', 'Open', 'kenbeg', 'Ladder', 'kengames']
divs_checked = form.getlist('division')
div_str = []

for d in divs:
    if(d in divs_checked):
        div_str.append(d)
    else:
        div_str.append("-")

    

write_line = ",".join(write_line)+","+",".join(div_str)+","+",".join(music_filenames)+"\n"

outfile.write(write_line)

outfile.close()

print 'Thank you for registering!!<br>'
print write_line





