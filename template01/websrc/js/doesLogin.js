// Notice: 'document.cookies' is not equal to 'document.cookie'. 
function checkLoginStatusAjaxPost(webhost = 'http://localhost') {
    let record = document.cookies.split('|');
    var weburl = webhost + "/webapi/doeslogin";
    if( !(record[1].includes("token") && record[1].includes("id")) ) {
        return ;
    }
    var cookiesData = JSON.parse(record[1]);
    $.ajax({
        type: "POST", 
        url: weburl,
        contentType: "application/json;charset=utf-8", 
        dataType: "json", 
        crossDomain: true, 
        data: JSON.stringify(cookiesData), 
        beforeSend: function(request) {
        	request.setRequestHeader("Access-Control-Allow-Origin", "*");
        },
        error: function (thrownError) {
            console.log(thrownError);
        },
        complete: function (xhr) {
            if(xhr.readyState == 4 && xhr.status == 200) {
                var _ = $.post(weburl, {"token": cookiesData["token"], "id": cookiesData["id"]});
                var jsonStr = xhr.responseText;
                console.log('response data:\n' + jsonStr + "\n"); // DEBUG 
                document.getElementById("textarea1").value  = 'content of response from server:\n' + jsonStr + '\n';
                document.getElementById("textarea1").value += '\ncookies in local data storage:\n' + document.cookies + '\n';
                alert(jsonStr);
            }
            else {
                console.log("readyState = " + xhr.readyState);
                console.log("HTTP status code = " + xhr.status);
            }
        }
    });
}