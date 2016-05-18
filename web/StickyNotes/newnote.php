<?php

require "../cgi-bin/db_connect.php";

$id = $_GET['id'];
if($id != "")
{
    //$query = 'SELECT title, content, color FROM StickyNotes where id='.$id.';';
    $query = $mysqli->prepare('SELECT title, content, color FROM StickyNotes where id=?');
    $query->bind_param('i', intval($id));
    $query->execute();
    $query->store_result();
 
 //   if( !($result = $mysqli->query($query)) )
    if( $query->num_rows == 0 )
    {
        echo "Invalid edit query!\n";
        exit();
    }

    $query->bind_result($edit_title, $edit_content, $edit_color);
    $query->fetch();

    //$row = $result->fetch_assoc();
    //$edit_title = $row['title'];
    //$edit_content = $row['content'];
    //$edit_color = $row['color'];
}
?>

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

<style>
.square-gray {
    width: 400px;
    height: 500px;
    margin: auto;
    padding: 20px;
    background-color: #CCC;
}
</style>

</head>


<body>

<div class="square square-gray">
<form action="addnote.php" method="post" onsubmit="return check_fields();">
    <div class="form-row">
       <label for="note-title">Title</label>
<?php
if($id == "")
    echo '<input type="text" name="note-title" id="note-title" size="28">';
else
{
    echo '<input name="id" type="hidden" value="'.$id.'">';

    echo '<input type="text" name="note-title" id="note-title" size="28" value="';
    echo $edit_title;
    echo '">';
}
?>
    </div>
    <div class="form-row">
       <label for="note-content">Content</label>
<?php
if($id == "")
    echo '<textarea name="note-content" id="note-content" rows="8" cols="25"></textarea>';
else
{
    echo '<textarea name="note-content" id="note-content" rows="8" cols="25">';
    echo $edit_content;
    echo '</textarea>';
}

?>
    </div>
    <div class="form-row">
        <label for="note-color">Color</label>
        <select name="note-color">
<?php
$colors = array('red', 'yellow', 'blue');
foreach ($colors as $c)
{
    echo "<option value='".$c."'";
    if($edit_color == $c)
        echo " selected>";
    else
        echo ">";
    echo ucfirst($c)."</option>";
}
?>
        </select>
    </div>
    <button type="submit" class="btn btn-primary">Add note</button>
    <a class="btn btn-default pull-right" href="index.php">Cancel</a>
</form>
</div>


</body>

</html>

<?php
$mysqli->close();
?>

