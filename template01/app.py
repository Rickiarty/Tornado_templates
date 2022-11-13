"""
    entry of this web application
"""

import tornado.ioloop
import tornado.web
from View.webapi import basic_web_api

def make_app():
    static_path_dir = './websrc/'
    return tornado.web.Application([
        (r'^/webapi/.+$', basic_web_api.BasicWebAPIHandler),
        (r'^/(.*)$', tornado.web.StaticFileHandler, {'path': static_path_dir}),
    ])

if __name__ == "__main__":
    port = 80
    app = make_app()
    app.listen(port)
    print('Tornado is running at port {} ...\n'.format(port))
    tornado.ioloop.IOLoop.current().start()
