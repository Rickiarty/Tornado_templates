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
            expDate.setTime(expDate.getTime() + (15*60*1000));
            document.cookie = "token=" + responseData["token"] + ";id=" + responseData["id"] + ";expires=" + expDate.toUTCString() + ";path=/;";
            document.getElementById("textarea1").innerHTML = JSON.stringify(responseData);
        },
        error: function (thrownError) {
            console.log(thrownError);
        }
    });
}

function checkLoginStatusAjaxPost() {
    let attr = document.cookie.split(';');
    var formData = {
        token: attr[0].substring(6),
        id: attr[0].substring(3),
    };
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
            alert(JSON.stringify(responseData));
        },
        error: function (thrownError) {
            console.log(thrownError);
        }
    });
}