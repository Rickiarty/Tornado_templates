"""
    entry point of this web application
"""

import tornado.ioloop
import tornado.web

def make_app():
    static_path_dir = './websrc/'
    return tornado.web.Application([
        (r'^/(.*)$', tornado.web.StaticFileHandler, {'path': static_path_dir}),
    ])

if __name__ == "__main__":
    port = 80
    app = make_app()
    app.listen(port)
    print('Tornado is running at port {} ...\n'.format(port))
    tornado.ioloop.IOLoop.current().start()
