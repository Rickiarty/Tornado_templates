function loginAjaxPost(webhost = 'http://localhost') {
    var weburl = webhost + "/webapi/login";
    var webpageData = {
        id: $("#textbox1").val(),
        password: $("#textbox2").val(),
    };
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
            console.log('response data:\n' + JSON.stringify(responseData) + "\n"); // DEBUG 
            const expDate = new Date();
            expDate.setTime(expDate.getTime() + (15*60*1000)); // now + 15 minutes in milli-second 
            var cookie = "record=|" + JSON.stringify(responseData) + "|;expires=" + expDate.toUTCString() + ";path=/;";
            //alert(cookie); // DEBUG 
            document.cookie = cookie;
            document.getElementById("textarea1").innerHTML = cookie;
        },
        error: function (thrownError) {
            console.log(thrownError);
        }
    });
}

function checkLoginStatusAjaxPost(webhost = 'http://localhost') {
    let record = document.cookie.split('|');
    var weburl = webhost + "/webapi/doeslogin";
    var webpageData = JSON.parse(record[1]);
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
            var readyState = $.post(weburl, {"token": webpageData["token"], "id": webpageData["id"]});
            console.log('response data:\n' + JSON.stringify(responseData) + "\n"); // DEBUG 
            document.getElementById("textarea1").innerHTML = JSON.stringify(webpageData);
            alert(JSON.stringify(responseData));
        },
        error: function (thrownError) {
            console.log(thrownError);
        }
    });
}