/*function add_new_note(status)
{
    var newform_bg = document.getElementById('newform-bg');
    var newform = document.getElementById('newform');

    if(status == 'on')
    {
        newform_bg.style.visibility = 'visible';
        newform_bg.style.opacity = 0.7;

        newform.style.visibility = 'visible';
        newform.style.opacity = 1.0;
    }
    else
    {
        newform_bg.style.visibility = 'hidden';
        newform_bg.style.opacity = 0;

        newform.style.visibility = 'hidden';
        newform.style.opacity = 0;
    }
}*/

function check_fields()
{
    var title = document.getElementsByName('note-title')[0].value;
    var content = document.getElementsByName('note-content')[0].value;

    if( title == "")
    {
        alert("Please fill in the title.");
        return false;
    }
    
    if( content == "")
    {
        alert("Please fill in the content.");
        return false;
    }
    
    return true;
}
