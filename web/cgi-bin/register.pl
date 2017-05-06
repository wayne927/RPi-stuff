#!/usr/bin/perl

use strict;
use CGI;
#use Mail::Mailer;

my $cgi = new CGI;

my %in = (
	"email" => $cgi->param("email"),
    "paidemail" => $cgi->param("paidemail"),
	"fname" => $cgi->param("fname"),
	"lname" => $cgi->param("lname"),
	"musicfile1aprelim" => $cgi->param("musicfile1aprelim"),
	"musicfile1afinal" => $cgi->param("musicfile1afinal"),
	"musicfileopen" => $cgi->param("musicfileopen")
);

print "Content-type: text/html;\n\n";
print "<html><body>";

print $in{lname};
print $in{fname};
print $in{paidemail};
print $in{musicfile1aprelim};

print "</body></html>";


my $upload_dir = $ENV{DOCUMENT_ROOT} . "/regdata/files";
my $mytime = time;

my $data = $ENV{DOCUMENT_ROOT} . "/regdata/regdata.tsv";

my $req = 0;

for my $item ("email", "fname", "lname")
{
	$in{$item} = cleanout($in{$item});
	
	if ($in{$item} eq "")
	{
		$req++;
	}
}

# not required, but still need cleaning
$in{paidemail} = cleanout($in{paidemail});



if ($req > 0)
{
	print "Content-type: text/html;\n\n";
	print "<html>" .
		"<title>Music upload - Eastern Canadian Regionals 2017</title>\n" .
		"<link rel=\"stylesheet\" type=\"text/css\" href=\"/style.css\"/>\n" .
		"<link rel=\"stylesheet\" type=\"text/css\" href=\"/register.css\"/>\n" .
		"<link rel=\"stylesheet\" type=\"text/css\" href=\"http://fonts.googleapis.com/css?family=Open+Sans|Oswald\">\n" .
	"<body><div id=\"content\"><h1>Missing Data</h1><p>Please <a href=\"javascript: history.go(-1);\">go back</a> and fill out all the required fields</p></div></body></html>\n";
	#print $upload_dir;
}
else
{
	my @err = ();
    
    my $oneA_prelim_uploaded = 0;
    my $oneA_final_uploaded = 0;
    my $open_uploaded = 0;
    
    my $oneA_prelim_filename = "";
    my $oneA_final_filename = "";
    my $open_filename = "";

	# ----------- music for 1a prelim ------------------------------
	if ($in{musicfile1aprelim} ne "")
	{
		my $filename = cleanout($in{musicfile1aprelim});
        $oneA_prelim_filename = $filename;
		
		my $upload_filehandle = $cgi->upload("musicfile1aprelim") || push(@err, __LINE__ . ": " . $!);
		
		$mytime = $in{fname} . "-" . $in{lname} . "-1A_prelim";
		
		$upload_dir = $upload_dir . "/" . $mytime;
		
		if (not -e $upload_dir){
			mkdir $upload_dir, 0750;
		}
		
		open UPLOADFILE, ">$upload_dir/$filename" || push(@err, __LINE__ . ": " . $!);; 

		if (scalar(@err) == 0){
			binmode UPLOADFILE || push(@err, __LINE__ . ": " . $!);

	        my $buffer;
			my $bytesread;

			while ($bytesread = read($upload_filehandle, $buffer, 1024)) {
				print UPLOADFILE $buffer || push(@err, __LINE__ . ": " . $!);
			}
		}
		close UPLOADFILE || push(@err, __LINE__ . ": " . $!);
		
		$in{musicfile1aprelim} = "/files/" . $mytime . "/" . $filename;
        
        $oneA_prelim_uploaded = 1;
	}
	
	$upload_dir = $ENV{DOCUMENT_ROOT} . "/regdata/files";
	
	# ----------- music for 1a final ------------------------------
	if ($in{musicfile1afinal} ne "")
	{
		my $filename = cleanout($in{musicfile1afinal});
        $oneA_final_filename = $filename;
		
		my $upload_filehandle = $cgi->upload("musicfile1afinal") || push(@err, __LINE__ . ": " . $!);
		
		$mytime = $in{fname} . "-" . $in{lname} . "-1A_final";
		
		$upload_dir = $upload_dir . "/" . $mytime;
		
		if (not -e $upload_dir){
			mkdir $upload_dir, 0750;
		}
		
		open UPLOADFILE, ">$upload_dir/$filename" || push(@err, __LINE__ . ": " . $!);; 

		if (scalar(@err) == 0){
			binmode UPLOADFILE || push(@err, __LINE__ . ": " . $!);

	        my $buffer;
			my $bytesread;

			while ($bytesread = read($upload_filehandle, $buffer, 1024)) {
				print UPLOADFILE $buffer || push(@err, __LINE__ . ": " . $!);
			}
		}
		close UPLOADFILE || push(@err, __LINE__ . ": " . $!);
		
		$in{musicfile1afinal} = "/files/" . $mytime . "/" . $filename;
        
        $oneA_final_uploaded = 1;
	}
	
	$upload_dir = $ENV{DOCUMENT_ROOT} . "/regdata/files";
	
	# ----------- music for open ------------------------------
	if ($in{musicfileopen} ne "")
	{
		my $filename = cleanout($in{musicfileopen});
        $open_filename = $filename;
		
		my $upload_filehandle = $cgi->upload("musicfileopen") || push(@err, __LINE__ . ": " . $!);
		
		$mytime = $in{fname} . "-" . $in{lname} . "-open";
		
		$upload_dir = $upload_dir . "/" . $mytime;
		
		if (not -e $upload_dir){
			mkdir $upload_dir, 0750;
		}
		
		open UPLOADFILE, ">$upload_dir/$filename" || push(@err, __LINE__ . ": " . $!);; 

		if (scalar(@err) == 0){
			binmode UPLOADFILE || push(@err, __LINE__ . ": " . $!);

	        my $buffer;
			my $bytesread;

			while ($bytesread = read($upload_filehandle, $buffer, 1024)) {
				print UPLOADFILE $buffer || push(@err, __LINE__ . ": " . $!);
			}
		}
		close UPLOADFILE || push(@err, __LINE__ . ": " . $!);
		
		$in{musicfileopen} = "/files/" . $mytime . "/" . $filename;
        
        $open_uploaded = 1;
	}
	
    
    
	open(FH, ">>" . $data);
    
    my $print_email_str = $in{email};
    if($in{paidemail} ne "")
    {
        $print_email_str .= ",";
        $print_email_str .= $in{paidemail};
    }
	
	print FH
        $print_email_str . "\t" .
		$in{"fname"} . "\t" .
		$in{"lname"} . "\t" .
		$in{"musicfile1aprelim"} . "\t" .
		$in{"musicfile1afinal"} . "\t" .
		$in{"musicfileopen"} . "\n";

	close(FH);
    
	
	# Send Emails
	my $mailerr = "";
	
	my $emailsubject = "Eastern Canadian Regionals 2017 music upload confirmation";
	
	my $emailmsg = "Hello " . $in{"fname"} . " " . $in{"lname"} . ",<br><br>";
    
    $emailmsg .= "This is to confirm that you have successfully uploaded music files for the following divisions";
    if($oneA_prelim_uploaded == 1 && $oneA_prelim_filename ne "")
    {
        $emailmsg .= "<p>1A preliminary: " . $oneA_prelim_filename . "</p>";
    }
    if($oneA_final_uploaded == 1 && $oneA_final_filename ne "")
    {
        $emailmsg .= "<p>1A final: " . $oneA_final_filename . "</p>";
    }
	if($open_uploaded == 1 && $open_filename ne "")
    {
        $emailmsg .= "<p>Open final: " . $open_filename . "</p>";
    }
    
    $emailmsg .= "<p>We look forward to seeing you in Toronto on May 20.</p>";
    $emailmsg .= "<p>Good luck!</p>";
    
	
    print $emailmsg;
    
exit;
    
	
	# $mailerr .= SendMail(
		# $in{"email"},
		# $emailsubject,
		# $emailmsg);
	

	# $mailerr .= SendMail(
		# "wayne.ngan\@gmail.com",
		# "New Nats music upload",
		# $emailmsg
	# );

    #print "Location: http://" . $ENV{HTTP_HOST} . "/music-thanks.html\n\n";

}

sub cleanout ($)
{
	my $item = shift;
	
	$item =~ s/\s+/ /gi;
	$item =~ s/\t+/ /gi;
	$item =~ s/\r+//gi;
	$item =~ s/\n+/ /gi;
	$item =~ s/^\s+//gi;
	$item =~ s/\s+$//gi;
	
	return $item;
}


sub SendMail {
	# my $err = "";
	# my($to, $subject, $message) = @_;
	
	# my $mailer = Mail::Mailer->new();
	# $mailer->open({
			# 'Content-Type' => "text/html;",
			# From => "Eastern Canadian Regionals 2017 \<contact\@yoyotoronto.com\>",
			# To => $to,
			# Subject => $subject
			# }) || ($err .= "Can't send an e-mail. Registration failed.");
	# print $mailer $message;
	# $mailer->close();
	# return $err;
}


#print "Content-type: text/html;\n\n";
#foreach my $key (keys %in)
#{
#	print "<b>" . $key . "</b> " . $in{$key} . "<br>\n";
#}
