
function checkAccountValidityAjaxPost(webhost = 'http://localhost') {
    var weburl = webhost + "/webapi/isaccountvalid";
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
        complete: function (xhr) {
            console.log("readyState = " + xhr.readyState);
            console.log("HTTP status code = " + xhr.status);
            if(xhr.readyState == 4 && xhr.status == 200) {
                var jsonStr = xhr.responseText;
                console.log('response data:\n' + jsonStr + "\n"); // DEBUG 
                document.getElementById("textarea1").value  = 'content of response from server:\n' + jsonStr + '\n';
                alert(jsonStr);
            }
            else {
            }
        }
    });
}
