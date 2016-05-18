<?php 

require "../cgi-bin/db_connect.php";

$title = $_POST['note-title'];
$content = $_POST['note-content'];
$color = $_POST['note-color'];
$id = $_POST['id'];

if($title=="" || $content=="")
{
    echo "Empty title or content!";
    exit();
}

if($id == "") // new note
{
    echo "title = $title";
    echo "content = $content";

    //$insert_query = "INSERT INTO StickyNotes (title,content,color) VALUES ('".$title."','".$content."','".$color."');";
    $query = $mysqli->prepare("INSERT INTO StickyNotes (title, content, color) VALUES (?, ?, ?);");
    $query->bind_param("sss", $title, $content, $color);
}
else
{
    //$insert_query = "UPDATE StickyNotes SET title='".$title."', content='".$content."', color='".$color."' WHERE id=".$id.";";
    $query = $mysqli->prepare("UPDATE StickyNotes SET title=?, content=?, color=? WHERE id=?;");
    $query->bind_param("sssi", $title, $content, $color, intval($id));
}

//if( !($result = $mysqli->query($insert_query)) )
if( !($query->execute()) || $query->affected_rows == 0)
{
    echo "Querry error\n<br>";
    exit();
}

$mysqli->close();

header('Location: index.php');

?>
