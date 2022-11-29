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
            //console.log(responseData); // DEBUG 
            document.getElementsByName("textarea1").value = responseData;
        },
        error: function (thrownError) {
            console.log(thrownError);
        }
    });
}