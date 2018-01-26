<!DOCTYPE HTML>
<html>
<head>
<title>PicTransfer</title>

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
    max-width: 500px;
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
$dir = $_SERVER['DOCUMENT_ROOT'].'/PicTransfer/files';
$files = array_diff(scandir($dir), array('..', '.'));

foreach ($files as $thisfile)
{
    $filename = "files/".$thisfile;

    print("<div class='displayfile'>\n");
    print("<a href='".$filename."'>".$thisfile);

    $extension = end(explode(".", $thisfile));
    if (!strcasecmp($extension, "jpg") ||
        !strcasecmp($extension, "png") ||
        !strcasecmp($extension, "gif")) 
    {
        print("<br/><img src='".$filename."' width='400' />");
    }

    print("</a></div>");
}

?>


</body>



</html>
