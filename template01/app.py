#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    entry of this web application
"""

import os
import tornado.ioloop
import tornado.web
from webapi import basic_web_api

class MainHandler(tornado.web.RequestHandler):
    _web_root = os.path.abspath('./web')

    def get(self):
        #self.write('Hello, Tornado framework.')
        fpath = os.path.join(self._web_root, self.request.uri[1:])
        with open(fpath, "r") as html:
            lines = html.readlines()
            s = ""
            for line in lines:
                s += line
            print(s)
            b = bytes(s, 'utf-8')
            self.write(b)

def make_app():
    static_path_dir = './web/static/'
    return tornado.web.Application([
        (r'^/static/.+$', tornado.web.StaticFileHandler, {'path': static_path_dir}),
        (r'^/webapi/.+$', basic_web_api.BasicWebAPIHandler),
        (r'^/.*$', MainHandler),
    ])

if __name__ == "__main__":
    port = 80
    app = make_app()
    app.listen(port)
    print('Tornado is running at port {} ...'.format(port))
    tornado.ioloop.IOLoop.current().start()
