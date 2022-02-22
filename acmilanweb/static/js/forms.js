function checkForm()
{
    var error=false; //to znaczy, że danych nie brakuje
    var contactName = document.getElementById("contactName");
    var contactEmail = document.getElementById("contactEmail");
    var contactInfo = document.getElementById("contactInfo");


    if (contactName.value == "")
    {
        document.getElementById("errorName").className="alert alert-danger";
        error=true;
    }
    
    if(contactEmail.value == "")
    {
        document.getElementById("errorEmail").className="alert alert-danger"; 
        error=true;
    } 
    else
    {
        var email = contactEmail.value;
        var regex = /^[a-zA-Z0-9._-]+@([a-zA-Z0-9.-]+\.)+[a-zA-Z0-9.-]{2,4}$/;
        if(regex.test(email)==false)
        {
            document.getElementById("mail").className="form-group has-error";
            document.getElementById("errorEmail").innerHTML="Niepoprawny adres e-mail";
            document.getElementById("errorEmail").className="alert alert-danger"; 
            error=true;
        }
    }

    if (contactInfo.value == "")
    {
        document.getElementById("errorInfo").className="alert alert-danger"; 
        error=true;
    }

    //zapobiega wyslaniu po wykryci bledow
    if (!error) return true; 
    else return false;
}

