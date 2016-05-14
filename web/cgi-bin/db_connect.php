<?php

$hostname = "localhost";
$username = "root";
$password = "ukekeu";

$mysqli = new mysqli($hostname, $username, $password, "wayneDB");

if($mysqli->connect_errno)
{
    echo "Can't connect to MySQL server.\n";
    exit();
}


?>
