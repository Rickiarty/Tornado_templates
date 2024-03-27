
function refreshTokenAjaxPost(webhost = 'http://localhost') {
    var weburl = webhost + "/webapi/refreshtoken";
    let record = document.cookie.split('|');
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
                document.getElementById("textarea1").value  = 'cookie in local data storage - before:\n' + document.cookie + '\n';
                var jsonStr = xhr.responseText;
                console.log('response data:\n' + jsonStr + "\n"); // DEBUG 
                const expDate = new Date();
                expDate.setTime(expDate.getTime() + 15*(60*1000)); // now + 15 minutes in milli-second 
                var cookie = "record=|" + jsonStr + "|;expires=" + expDate.toUTCString() + ";path=/;SameSite=Strict";
                document.cookie = cookie;
                document.getElementById("textarea1").value += '\ncontent of response from server:\n' + jsonStr + '\n';
                document.getElementById("textarea1").value += '\ncookie in local data storage - after:\n' + document.cookie + '\n';
            }
            else {
            }
        }
    });
}
