#!/usr/bin/perl

use strict;
use CGI;

my $cgi = new CGI;

my %in = (
	"email" => $cgi->param("email"),
	"fname" => $cgi->param("fname"),
	"lname" => $cgi->param("lname")
);

my $data = $ENV{DOCUMENT_ROOT}."/regdata/regdata.tsv";

open(FH, ">>" . $data);

#print FH "hiihihi\n";

print FH $in{"email"} . ", ".
         $in{"fname"} . ", ".
         $in{"lname"};

close(FH);


print "Content-type: text/html;\n\n";

print "env document_root = ".$ENV{DOCUMENT_ROOT}."<br>\n";

print "File written!<br>\n";

print "Thank you, ".$in{"fname"}." ".$in{"lname"}."!!\n\n";
