// Notice: 'document.cookie' is not equal to 'document.cookie'. 
function checkLoginStatusAjaxPost(webhost = 'http://localhost') {
    let record = document.cookie.split('|');
    var weburl = webhost + "/webapi/doeslogin";
    if( !(record[1].includes("token") && record[1].includes("id")) ) {
        return ;
    }
    var cookieData = JSON.parse(record[1]);
    $.ajax({
        type: "POST", 
        url: weburl,
        contentType: "application/json;charset=utf-8", 
        dataType: "json", 
        crossDomain: true, 
        data: JSON.stringify(cookieData), 
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
                document.getElementById("textarea1").value += '\ncookie in local data storage:\n' + document.cookie + '\n';
                alert(jsonStr);
            }
            else {
            }
        }
    });
}