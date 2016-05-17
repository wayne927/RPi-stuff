<?php 

require "../cgi-bin/db_connect.php";

$id = $_GET['id'];

if($id == "")
    header('Location: index.php');

$query = "UPDATE StickyNotes set active=0 where id=".$id.";";

if( !($result = $mysqli->query($query)) )
{
    echo "Querry error\n<br>";
    echo $query;
    exit();
}

header('Location: index.php');

?>
