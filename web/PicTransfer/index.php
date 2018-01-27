<!DOCTYPE HTML>
<html>
<head>
<title>PicTransfer</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<script type="text/javascript">
function displayFileName()
{
    var input = document.getElementById("choosefile");
    var str = "";
    
    if('files' in input)
    {
        if(input.files.length == 0)
            str = "Please select a file.";
        else
            for (var i=0; i<input.files.length; i++)
            {
                str = str + input.files[i].name;
                str = str + "<br>";
            }
    }
    
    document.getElementById("chosenfilelist").innerHTML = str;
}
</script>

<style>
body {
    font-family: sans-serif;
}

#chosenfilelist {
    border: 1px solid #BBBBBB;
    padding: 10px 10px;
    /*max-width: 500px;*/
    width: 500px;
    min-height: 100px;
    margin-bottom: 20px;
}

.inputfile {
    width: 0.1px;
    height: 0.1px;
}

.inputfile + label {
    padding: 9px 20px;
    margin-left: -5px;
    height: 50px;
    font-size: 30px;
    background-color: #5555CC;
    border-radius: 5px;
    color: white;
    cursor: pointer;
}
.inputfile + label:hover {
    background-color: #2222FF;
}

input[type=submit] {
    padding: 0 20px 0 20px;
    padding-right: 20px;
    height: 50px;
    font-size: 30px;
    background-color: #11AA11;
    border-radius: 5px;
    color: white;
    cursor: pointer;
    border: none;
}
input[type=submit]:hover {
    background-color: #22BB22;
}

.displayfile { 
    margin: 20px 0 20px 0;
    padding: 10px;
    width: 500px;
    background-color: #DDD;
}
.displayfile:hover {
    background-color: #CCC;
}

.displayfile img {
    padding-top: 5px;
}

.filesize {
    color: #888;
}

@media only screen and (max-width: 700px) {
#chosenfilelist {
    width: 95%;
}
.displayfile {
    width: 95%;
}
.displayfile img {
    width: 100%;
}

}
</style>

</head>

<body>

<form id="fileform"  action="/cgi-bin/process_PicTransfer.py" method="POST" enctype="multipart/form-data">
    <h3>Upload file:</h3>
    <div id="chosenfilelist">No file chosen</div>
    <input type="file" id="choosefile" class="inputfile" name="picfile" onchange="displayFileName();" multiple>
    <label for="choosefile">Browse</label>

    <p><input type="submit" value="Upload"></p>
</form>

<?php
function isImageFile($filename)
{
    $extension = end(explode(".", $filename));
    return (!strcasecmp($extension, "jpg") ||
            !strcasecmp($extension, "png") ||
            !strcasecmp($extension, "gif")); 
}

$dir = $_SERVER['DOCUMENT_ROOT'].'/PicTransfer/files';
$files_unordered = array_diff(scandir($dir), array('..', '.'));
$files = array();

foreach ($files_unordered as $thisfile)
{
    if (isImageFile($thisfile))
        array_push($files, $thisfile);
    else
        array_unshift($files, $thisfile);
}

foreach ($files as $thisfile)
{
    $filename = "files/".$thisfile;
    $filesize_kB = round(filesize($dir."/".$thisfile) / 1000);
    $filesize_MB = $filesize_kB / 1000;

    print("<div class='displayfile'>");
    print("<span class='filesize'>");
    if ($filesize_MB > 1)
        print("(".$filesize_MB." M) ");
    else
        print("(".$filesize_kB." k) ");
    print("</span>");
    print("<a href='".$filename."'>".$thisfile);

    if (isImageFile($thisfile))
    {
        print("<br/><img src='".$filename."' width='400' />");
    }

    print("</a></div>\n\n");
}

?>


</body>



</html>
