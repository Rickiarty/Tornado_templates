#import json
#from urllib.parse import parse_qs
import View.BaseHandler

class BasicWebHandler(View.BaseHandler.BaseHandler):
    # HTTP method 'GET'
    def get(self):
        self.set_default_headers()
        #print(self.request.full_url()) # DEBUG 
        web_url = self.request.full_url()
        web_url = web_url.replace('http://', '')
        web_url = web_url.replace('https://', '')
        hostname_portnumber = web_url.split('/')[0] # 0th element 
        #print(hostname_portnumber) # DEBUG 
        web_url = web_url.replace(hostname_portnumber, '')
        #print(web_url) # DEBUG 
        file_path = './websrc/' + web_url[1:]
        #print(file_path) # DEBUG 
        try:
            with open(file_path, "rb") as web_source_file: # "rb": read-only and read in binary 
                http_response_bytes = web_source_file.read() # -> bytes 
            self.write(http_response_bytes) # write a series of data to network stream in byte - executed only once 
        except Exception as ex:
            print(str(ex))
            self.set_status(404)
            self.finish("Woops! page not found!")

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
        self.write(http_response_str) # write a string to network stream - executed only once 
