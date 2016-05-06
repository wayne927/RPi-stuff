#!/usr/bin/perl

use strict;


#my $data = $ENV{DOCUMENT_ROOT}."/regdata/regdata.tsv";

#my $data = "/regdata/regdata.tsv";

my $data = "outfile.txt";

open(FH, ">>", $data);

print FH "hiihihi\n";


close(FH);


print "Content-type: text/html;\n\n";

print "File written!<br>\n";
