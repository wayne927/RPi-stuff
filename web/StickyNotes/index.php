<!DOCTYPE HTML>

<html>
<head>
<title>Sticky Notes</title>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" />
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap-theme.min.css" />
<link rel="stylesheet" type="text/css" href="http://fonts.googleapis.com/css?family=Open+Sans|Oswald|Roboto+Condensed" />
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>

<!-- my own styles -->
<link rel="stylesheet" type="text/css" href="style.css"/>
<script src="script.js"></script>

</head>

<body>

<?php 

require "../cgi-bin/db_connect.php";

if( !($result = $mysqli->query("SELECT * FROM StickyNotes;")) )
{
    echo "Query error\n";
    exit();
}
?>

<div class="container"><div class="row">

<?php

while($row = $result->fetch_assoc())
{
    if($row['active'] != 1)
        continue;

// color
    echo "<div class='col-sm-4'><div class='square ";
    if($row['color']=='red')
        echo "square-red";
    else if($row['color']=='blue')
        echo "square-blue";
    else
        echo "square-yellow";
    echo "'>\n";

// title
    echo "<h2>".$row['title']."</h2>\n";

// body content
    echo "<p>\n";
    echo $row['content'];
    echo "</p>\n";

// edit, delete buttons
    echo "<div class='delete-button'>\n";
    
    echo "<a href='newnote.php?id=".$row['id']."'>";
    echo "<span class='glyphicon glyphicon-pencil'></span></a>\n";
    echo "&nbsp;\n";

    echo "<a href='deletenote.php?id=".$row['id']."'><span class='glyphicon glyphicon-remove'></span></a>";
    echo "</div>\n";


    echo "</div></div>\n";

}

?>

</div>

<a class="btn btn-default" href="newnote.php">Add new note</a>

</div>



</body>

</html>
