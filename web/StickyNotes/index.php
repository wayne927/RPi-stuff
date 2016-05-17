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
    
    echo "<a href='index.php?editid=".$row['id']."' ";
    echo "onclick='javascript:add_new_note(\"on\");'";
    echo "><span class='glyphicon glyphicon-pencil'></span></a>\n";
    echo "&nbsp;\n";

    echo "<a href='deletenote.php?id=".$row['id']."'><span class='glyphicon glyphicon-remove'></span></a>";
    echo "</div>\n";


    echo "</div></div>\n";

}

?>

</div>

<a class="btn btn-default" href="javascript:add_new_note('on');">Add new note</a>

</div>

<?php
$editid = $_GET['editid'];

if($editid > 0)
{
    $query = 'SELECT title, content, color FROM StickyNotes where id='.$editid.';';
    if( !($result = $mysqli->query($query)) )
    {
        echo "Error! ".$query;
        exit();
    }
    $row = $result->fetch_assoc();
    $edit_title = $row['title'];
    $edit_content = $row['content'];
    $edit_color = $row['color'];
}
?>

<div id="newform-bg"></div>

<div id="newform">
    <form action="addnote.php" method="post" onsubmit="return check_fields();">
    <div class="form-row">
       <label for="note-title">Title</label>
<?php
if($editid > 0)
{
    echo '<input type="text" name="note-title" id="note-title" size="28" ';
    echo 'value="';
    echo $edit_title;
    echo '">';
}
else
    echo '<input type="text" name="note-title" id="note-title" size="28">';
?>
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
