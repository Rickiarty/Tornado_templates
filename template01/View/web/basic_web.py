import json
from urllib.parse import parse_qs
import View.BaseHandler

class BasicWebHandler(View.BaseHandler.BaseHandler):
    # HTTP method 'GET'
    def get(self):
        self.set_default_headers()
        http_response_str  = ''
        http_response_str += "\nrequest URL:\n" + str(self.request.full_url())
        http_response_str += '\n\nHTTP method/verb:\n' + str(self.request.method)
        http_response_str += "\n\nHTTP request's header:\n" + str(self.request.headers)
        http_response_str += '\n\nremote IP:\n' + str(self.request.remote_ip)
        http_response_str += "\n\nHTTP request's body:\n" + str(self.request.body)
        http_response_str += "\n\narguments of HTTP request's body:\n" + str(self.request.body_arguments)
        self.write(http_response_str)

    # HTTP method 'POST'
    def post(self):
        self.set_default_headers()
        http_response_str  = ''
        http_response_str += "\nrequest URL:\n" + str(self.request.full_url())
        http_response_str += '\n\nHTTP method/verb:\n' + str(self.request.method)
        http_response_str += "\n\nHTTP request's header:\n" + str(self.request.headers)
        http_response_str += '\n\nremote IP:\n' + str(self.request.remote_ip)
        http_response_str += "\n\nHTTP request's body:\n" + str(self.request.body)
        http_response_str += "\n\narguments of HTTP request's body:\n" + str(self.request.body_arguments)
        self.write(json.dumps(http_response_str))

    # HTTP method 'OPTIONS'
    def options(super):
        super.options()
