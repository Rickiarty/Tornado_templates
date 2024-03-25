function loginAjaxPost(webhost = 'http://localhost') {
    var weburl = webhost + "/webapi/login";
    var webpageData = {
        id: $("#textbox1").val(),
        password: $("#textbox2").val(),
    };
    if (webpageData['id'].replaceAll(" ", "")=="" || webpageData['password'].replaceAll(" ", "")=="") {
        return ;
    }
    $.ajax({
        type: "POST", 
        url: weburl,
        contentType: "application/json;charset=utf-8", 
        dataType: "json", 
        crossDomain: true, 
        data: JSON.stringify(webpageData), 
        beforeSend: function(request) {
        	request.setRequestHeader("Access-Control-Allow-Origin", "*");
        },
        error: function (thrownError) {
            console.log(thrownError);
        },
        complete: function (xhr) {
            if(xhr.readyState == 4 && xhr.status == 200) {
                console.log('web-URL:\n' + weburl + "\n"); // DEBUG 
                var jsonStr = xhr.responseText;
                console.log('response data:\n' + jsonStr + "\n"); // DEBUG 
                const expDate = new Date();
                expDate.setTime(expDate.getTime() + 15*(60*1000)); // now + 15 minutes in milli-second 
                var cookies = "record=|" + jsonStr + "|;expires=" + expDate.toUTCString() + ";path=/;";
                //alert(cookies); // DEBUG 
                document.cookies = cookies;
                document.getElementById("textarea1").value  = 'content of response from server:\n' + jsonStr + '\n';
                document.getElementById("textarea1").value += '\ncookies in local data storage:\n' + document.cookies + '\n';
            }
            else {
                console.log("readyState = " + xhr.readyState);
                console.log("HTTP status code = " + xhr.status);
            }
        }
    });
}