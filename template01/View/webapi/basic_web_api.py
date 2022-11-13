import json
from urllib.parse import parse_qs
import View.BaseHandler
from module.auth import Authentication

class BasicWebAPIHandler(View.BaseHandler.BaseHandler):
    
    #webapi_mapping = dict() # Substitute 'dict()' for '{}' to initialize a dictionary/mapping for preventing from mixing dictionaries up with sets. 
    webapi_mapping = {
        "login": Authentication.Login,
    }
    
    def get(self):
        self.set_default_headers()
        http_response_str = ""
        http_response_str += 'HTTP method/verb:\n' + str(self.request.method)
        http_response_str += "\n\nHTTP request's header:\n" + str(self.request.headers)
        http_response_str += '\n\nremote IP:\n' + str(self.request.remote_ip)
        http_response_str += "\n\nHTTP request's body:\n" + str(self.request.body)
        http_response_str += "\n\narguments of HTTP request's body:\n" + str(self.request.body_arguments)
        self.write(http_response_str)

    def post(self):
        http_response_data = {
            "token": "01234567879012346578901234567879013245678901234567879", 
            "id": "Bubu", 
            "sex": 1
        }
        self.set_default_headers()
        print(self.request.method) # DEBUG
        print(self.request.headers) # DEBUG
        print(self.request.remote_ip) # DEBUG
        print(str(self.request.body)) # DEBUG
        print(str(self.request.body_arguments)) # DEBUG
        #web_args = { key: value for key, value in self.request.arguments.items() } # 'dictionary comprehension' in Python 
        web_args = parse_qs(self.request.body)
        print(web_args) # DEBUG 
        id = str(web_args[b'id'][0])
        passwd = str(web_args[b'password'][0])
        temp = self.request.full_url().split('/')
        if temp[-2] != "webapi":
            self.set_status(404)
            self.finish("Woops! page not found!")
            return
        webapi_name = temp[-1]
        is_valid, token = self.webapi_mapping[webapi_name](id, passwd)
        if not is_valid:
            self.write(json.dumps(http_response_data))
            return        
        http_response_data["token"] = token
        http_response_data["id"] = id
        self.write(json.dumps(http_response_data))
