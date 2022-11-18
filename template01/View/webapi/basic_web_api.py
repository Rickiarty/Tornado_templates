import json
from urllib.parse import parse_qs
import View.BaseHandler
from module.auth import Authentication

class BasicWebAPIHandler(View.BaseHandler.BaseHandler):
    
    #_webapi_mapping = dict() # Substitute 'dict()' for '{}' to initialize a dictionary/mapping for preventing from mixing dictionaries up with sets. 
    _webapi_mapping = {
        "login": Authentication.Login,
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
        print(self.request.method) # DEBUG
        print(self.request.headers) # DEBUG
        print(self.request.remote_ip) # DEBUG
        print(str(self.request.body)) # DEBUG
        print(str(self.request.body_arguments)) # DEBUG
        #web_args = { key: value for key, value in self.request.arguments.items() } # 'dictionary comprehension' in Python 
        args_t = parse_qs(self.request.body)
        web_args = {'id': str(args_t[b'id'])[3:-2], 'password': str(args_t[b'password'])[3:-2]}
        url_segs = self.request.full_url().split('/')
        if url_segs[-2] != "webapi":
            self.set_status(404)
            self.finish("Woops! page not found!")
            return
        webapi_name = url_segs[-1]
        #print("\n\nwebapi_name:\n ", webapi_name, "\ntype of a specific mapped inner function/method:\n ", type(self._webapi_mapping[webapi_name]), "\nname of a specific mapped inner function/method:\n ", str(self._webapi_mapping[webapi_name]), '\n') # DEBUG 
        is_valid, token, id = self._webapi_mapping[webapi_name](**web_args) # try to login 
        if not is_valid:
            http_response_data['msg'] = "login failed"
            self.write(json.dumps(http_response_data))
            return        
        http_response_data["token"] = token
        http_response_data["id"] = id
        self.write(json.dumps(http_response_data))

    # HTTP method 'OPTIONS'
    def options(super):
        super.options()