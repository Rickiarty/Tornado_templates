#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import View.BaseHandler

class BasicWebAPIHandler(View.BaseHandler.BaseHandler):
    _json_response_content = '{ "success": "%s", "error_code": "%s", "msg": "%s" }'
    _msg = ''

    def get(self):
        self.write(self._json_response_content % ("1", "0", self._msg) )

    def post(self):
        self.write(self._json_response_content % ("1", "0", self._msg) )
    