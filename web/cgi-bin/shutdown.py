#!/usr/bin/python

# import cgi
# import cgitb
# import subprocess 
import os

print "Content-Type: text/html\n\n";

print("Shutting down now...\n");

os.system("sudo shutdown now");
