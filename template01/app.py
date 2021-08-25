#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    entry of this web application
"""

import tornado.ioloop
import tornado.web
from webapi import basic_web_api

class MainHandler(tornado.web.RequestHandler):
    web_root = './web'

    def get(self):
        self.write('Hello, Tornado framework.')

def make_app():
    static_path_dir = './web/static/'
    return tornado.web.Application([
        (r'^/static/.+$', tornado.web.StaticFileHandler, {'path': static_path_dir}),
        (r'^/webapi/.+$', basic_web_api.BasicWebAPIHandler),
        (r'^/.*$', MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()