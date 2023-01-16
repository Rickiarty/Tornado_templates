function loginAjaxPost(webhost = 'http://localhost') {
    var weburl = webhost + "/webapi/login";
    var webpageData = {
        id: $("#textbox1").val(),
        password: $("#textbox2").val(),
    };
    if (webpageData['id'].replace(" ", "")=="" || webpageData['password'].replace(" ", "")=="") {
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
        success: function (responseData) {
            console.log('web-URL:\n' + weburl + "\n"); // DEBUG 
            var readyState = $.post(weburl, {"id": webpageData["id"], "password": webpageData["password"]});
            var jsonStr = JSON.stringify(responseData);
            console.log('response data:\n' + jsonStr + "\n"); // DEBUG 
            const expDate = new Date();
            expDate.setTime(expDate.getTime() + 15*(60*1000)); // now + 15 minutes in milli-second 
            var cookies = "record=|" + jsonStr + "|;expires=" + expDate.toUTCString() + ";path=/;";
            //alert(cookies); // DEBUG 
            document.cookies = cookies;
            document.getElementById("textarea1").value  = 'content of response from server:\n' + jsonStr + '\n';
            document.getElementById("textarea1").value += '\ncookies in local data storage:\n' + document.cookies + '\n';
        },
        error: function (thrownError) {
            console.log(thrownError);
        }
    });
}