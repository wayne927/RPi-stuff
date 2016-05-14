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
    echo "<div class='col-sm-4'><div class='square ";
    if($row['color']=='red')
        echo "square-red";
    else if($row['color']=='blue')
        echo "square-blue";
    else
        echo "square-yellow";
    echo "'>\n";
    echo "<h2>".$row['title']."</h2>\n";
    echo "<p>\n";
    echo $row['content'];
    echo "</p>\n";
    echo "</div></div>\n";
}

?>

</div>

<br/>
<a class="btn btn-default" href="javascript:add_new_note('on');">Add new note</a>

</div>


<div id="newform-bg"></div>
<div id="newform">
    <form action="" method="post">
    <div class="form-row">
       <label for="note-title">Title</label>
       <input type="text" name="note-title" id="note-title" size="28">
    </div>
    <div class="form-row">
       <label for="note-content">Content</label>
       <textarea name="note-content" id="note-content" rows="8" cols="25"></textarea>
    </div>
    <div class="form-row">
        <label for="note-color">Color</label>
        <select name="note-color">
            <option value="red">Red</option>
            <option value="blue">Blue</option>
            <option value="yellow">Yellow</option>
        </select>
    </div>
    <button type="submit" class="btn btn-primary">Add note</button>
    <a class="btn btn-default pull-right" href="javascript:add_new_note('off');">Cancel</a>
    </form>
</div>


</body>

</html>
