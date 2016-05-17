<?php 

require "../cgi-bin/db_connect.php";

$title = $_POST['note-title'];
$content = $_POST['note-content'];
$color = $_POST['note-color'];

if($title=="" || $content=="")
    echo "WTF empty";

$insert_query = "INSERT INTO StickyNotes (title,content,color) VALUES ('".$title."','".$content."','".$color."');";

if( !($result = $mysqli->query($insert_query)) )
{
    echo "Querry error\n<br>";
    echo $insert_query;
    exit();
}

header('Location: index.php');

?>
