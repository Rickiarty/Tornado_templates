
function checkAccountValidityAjaxPost(webhost = 'http://localhost') {
    var weburl = webhost + "/webapi/isaccountvalid";
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
            var readyState = $.post(weburl, {"id": webpageData["id"], "password": webpageData["password"]});
            var jsonStr = JSON.stringify(responseData);
            console.log('response data:\n' + jsonStr + "\n"); // DEBUG 
            document.getElementById("textarea1").value  = 'content of response from server:\n' + jsonStr + '\n';
            alert(jsonStr);
        },
        error: function (thrownError) {
            console.log(thrownError);
        }
    });
}
