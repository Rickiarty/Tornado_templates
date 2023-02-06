import View.BaseHandler
import os

class BasicWebHandler(View.BaseHandler.BaseHandler):
    # HTTP method 'GET'
    def get(self):
        self.set_default_headers()
        web_url = self.request.full_url()
        web_url = web_url.split('://')[1]
        web_url = web_url.split('?')[0]
        web_url = web_url.split('#')[0]
        url_segs = web_url.split('/')
        hostname_portnumber = url_segs[0]
        file_path = ""
        web_url = web_url.replace(hostname_portnumber, '')
        if web_url[1:] == 'index.html' or web_url[1:] == 'index.htm' or web_url[1:] == 'index' or web_url[1:] == '' or len(url_segs) == 1:
            file_path = os.fspath('./websrc/index.html')
        else:
            file_path = os.path.join(os.fspath('./websrc/'), web_url[1:])
        http_response_bytes = None
        try:
            with open(file_path, "rb") as web_source_file: # "rb": read-only and read in binary 
                http_response_bytes = web_source_file.read() # -> bytes 
                #print(file_path, len(http_response_bytes), 'bytes') # DEBUG
            if http_response_bytes == None:
                self._httpResponseHandler(404)
            else:
                self.write(http_response_bytes) # write a series of data to network stream in byte - executed only once 
                self.flush()
        except Exception as ex:
            print(str(ex))
            self._httpResponseHandler(404)

    # HTTP method 'POST'
    def post(self):
        self._httpResponseHandler(204)
