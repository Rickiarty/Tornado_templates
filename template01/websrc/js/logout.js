function generalLogout(weburl) {
    let record = document.cookies.split('|');
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
                document.getElementById("textarea1").value  = 'cookies in local data storage - before:\n' + document.cookies + '\n';
                var _ = $.post(weburl, {"token": cookiesData["token"], "id": cookiesData["id"]});
                var jsonStr = xhr.responseText;
                var responseData = JSON.parse(jsonStr);
                console.log('response data:\n' + jsonStr + "\n"); //DEBUG 
                const expDate = new Date();
                expDate.setTime(expDate.getTime() - 730*(24*60*60*1000)); // now - 730 days in milli-second 
                var cookies = "record=|" + jsonStr + "|;expires=" + expDate.toUTCString() + ";path=/;";
                document.cookies = cookies;
                document.getElementById("textarea1").value += '\ncontent of response from server:\n' + jsonStr + '\n';
                document.getElementById("textarea1").value += '\ncookies in local data storage - after:\n' + document.cookies + '\n';
                if ( (responseData != null) && (responseData["result"] != null) ) {
                    if (responseData['result'] == "True") { 
                        alert('logout successfully');
                    }
                    else {
                        alert('failed to logout');
                    } 
                }
            }
            else {
                console.log("readyState = " + xhr.readyState);
                console.log("HTTP status code = " + xhr.status);
            }
        }
    });
}

function logoutAjaxPost(webhost = 'http://localhost') {
    var weburl = webhost + "/webapi/logout"; 
    generalLogout(weburl);
}

function logoutAllAjaxPost(webhost = 'http://localhost') { 
    var weburl = webhost + "/webapi/logoutall";
    generalLogout(weburl);
}
