
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
            var jsonStr = JSON.stringify(responseData);
            console.log('response data:\n' + jsonStr + "\n"); // DEBUG 
            document.getElementById("textarea1").innerHTML  = 'content of response from server:\n' + jsonStr + '\n';
            document.getElementById("textarea1").innerHTML += '\ncookie in local data storage:\n' + document.cookie + '\n';
            alert(jsonStr);
        },
        error: function (thrownError) {
            console.log(thrownError);
        }
    });
}