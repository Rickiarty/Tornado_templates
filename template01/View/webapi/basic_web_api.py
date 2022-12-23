import json
import View.BaseHandler
from module.auth import Authentication
#from urllib.parse import parse_qs

class BasicWebAPIHandler(View.BaseHandler.BaseHandler):
    
    #_webapi_mapping = dict() # Substitute 'dict()' for '{}' to initialize a dictionary/mapping for preventing from mixing dictionaries up with sets. 
    _webapi_mapping = {
        "isaccountvalid": Authentication.IsAccountValid, 
        "doeslogin": Authentication.DoesLogin, 
        "login": Authentication.Login, 
        "logout": Authentication.Logout, 
        "logoutall": Authentication.LogoutAll, 
        "refreshtoken": Authentication.RefreshToken, 
    }
    
    # HTTP method 'GET'
    def get(self):
        self.set_default_headers()
        http_response_str = ""
        http_response_str += 'HTTP method/verb:\n' + str(self.request.method)
        http_response_str += "\n\nHTTP request's header:\n" + str(self.request.headers)
        http_response_str += '\n\nremote IP:\n' + str(self.request.remote_ip)
        http_response_str += "\n\nHTTP request's body:\n" + str(self.request.body)
        http_response_str += "\n\narguments of HTTP request's body:\n" + str(self.request.body_arguments)
        self.write(http_response_str)

    # HTTP method 'POST'
    def post(self):
        http_response_data = dict() # Substitute 'dict()' for '{}' to initialize a dictionary/mapping for preventing from mixing dictionaries up with sets. 
        self.set_default_headers()
        #print(self.request.method) # DEBUG
        #print(self.request.headers) # DEBUG
        #print(self.request.remote_ip) # DEBUG
        #print(str(self.request.body)) # DEBUG
        #print(str(self.request.body_arguments)) # DEBUG
        #req_args = { key: value for key, value in self.request.arguments.items() } # 'dictionary comprehension' in Python 
        req_args = json.loads(str(self.request.body)[2:-1])
        #print(json.dumps(req_args)) # DEBUG 
        #print('id=', json.dumps(req_args['id'])) # DEBUG 
        #print('password=', json.dumps(req_args['password'])) # DEBUG 
        url_segs = self.request.full_url().split('/')
        if url_segs[-2] != "webapi":
            self._pageNotFound()
            return
        webapi_name = url_segs[-1]
        #print("\n\nwebapi_name:\n ", webapi_name, "\ntype of a specific mapped inner function/method:\n ", type(self._webapi_mapping[webapi_name]), "\nname of a specific mapped inner function/method:\n ", str(self._webapi_mapping[webapi_name]), '\n') # DEBUG 
        if webapi_name == 'login':
            succeeded, token, id = self._webapi_mapping[webapi_name](id=req_args['id'], password=req_args['password']) # try to login 
            if not succeeded:
                http_response_data['msg'] = "login failed"
                self.write(json.dumps(http_response_data))
                return        
            else: # succeeded 
                http_response_data["token"] = token
                http_response_data["id"] = id
                #print('log-in =', str(Authentication.DoesLogin(token=token, id=id))) # DEBUG 
                #print('id =', id) # DEBUG 
                #print('token =', token) # DEBUG 
                self.write(json.dumps(http_response_data))
                return
        elif webapi_name == 'logout':
            # It's NOT implemented yet.
            return
        elif webapi_name == 'logoutall':
            # It's NOT implemented yet.
            return
        elif webapi_name == 'refreshtoken':
            # It's NOT implemented yet.
            return
        elif webapi_name == 'doeslogin':
            does_login = self._webapi_mapping[webapi_name](token=req_args['token'], id=req_args['id'])
            http_response_data['doesLogin'] = str(does_login)
            self.write(json.dumps(http_response_data))
            return
        elif webapi_name == 'isaccountvalid':
            # It's NOT implemented yet.
            return
        else:
            # Do nothing. 
            return
