"""
    entry point of this web application
"""

import tornado.ioloop
import tornado.web
from View.webapi import basic_web_api
from View.web import basic_web

def make_app():
    static_path_dir = './websrc/'
    return tornado.web.Application([
        (r'^/webapi/.+$', basic_web_api.BasicWebAPIHandler), 
        (r'.*', basic_web.BasicWebHandler), # To resolve issues 'HTTP 405 - method not allow', it's one of keys to implement this instead of simply using Tornado's mapping mechanism from web URLs to static files' file paths. 
        (r'^/(.*)$', tornado.web.StaticFileHandler, {'path': static_path_dir}),
    ])

if __name__ == "__main__":
    port = 80
    app = make_app()
    app.listen(port)
    print('Tornado is running at port {} ...\n'.format(port))
    tornado.ioloop.IOLoop.current().start()
