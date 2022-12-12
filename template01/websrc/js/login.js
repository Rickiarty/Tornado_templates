function loginAjaxPost() {
    var formData = {
        id: $("#textbox1").val(),
        password: $("#textbox2").val(),
    };
    $.ajax({
        type: "POST", 
        url: "/webapi/login",
        contentType: "application/json;charset=utf-8", 
        dataType: "json", 
        crossDomain: true, 
        data: JSON.stringify(formData), 
        beforeSend: function(request) {
        	request.setRequestHeader("Access-Control-Allow-Origin", "*");
        },
        success: function (url, formData) {
            var responseData = $.post(url, {"id": formData["id"], "password": formData["password"]});
            const expDate = new Date();
            expDate.setTime(expDate.getTime() + (15*60*1000)); // now + 15 minutes in milli-second 
            var cookie = "record=|" + JSON.stringify(responseData) + "|;expires=" + expDate.toUTCString() + ";path=/;";
            alert(cookie); // DEBUG 
            document.cookie = cookie;
            document.getElementById("textarea1").innerHTML = cookie;
        },
        error: function (thrownError) {
            console.log(thrownError);
        }
    });
}

function checkLoginStatusAjaxPost() {
    let record = document.cookie.split('|');
    var formData = JSON.parse(record[1]);
    $.ajax({
        type: "POST", 
        url: "/webapi/doeslogin",
        contentType: "application/json;charset=utf-8", 
        dataType: "json", 
        crossDomain: true, 
        data: JSON.stringify(formData), 
        beforeSend: function(request) {
        	request.setRequestHeader("Access-Control-Allow-Origin", "*");
        },
        success: function (url, formData) {
            var responseData = $.post(url, {"token": formData["token"], "id": formData["id"]});
            document.getElementById("textarea1").innerHTML = JSON.stringify(formData);
            alert(JSON.stringify(responseData));
        },
        error: function (thrownError) {
            console.log(thrownError);
        }
    });
}