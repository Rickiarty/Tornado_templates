#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql

class Order:
    # private members
    __id = -1 # id auto-generated by database server
    __order_code = "" # id of order customized by developer
    __amount = 0 # total amount (of money)
    __customer_id = "" # (It's actually customer's e-mail in this web application.)
    __detail = "" # detail of order
    __note = "" # (optional)
    __progress = "" # progress in which order is dealt with by worker
    __time_stamp = "" # auto-generated by database server
    __deleted = 0 # False

    def __init__(self, id, order_code, amount, customer_id, detail, note, progress, time_stamp, deleted):
        self.__id = id
        self.__order_code = order_code
        self.__amount = amount
        self.__customer_id = customer_id
        self.__detail = detail
        self.__note = note
        self.__progress = progress
        self.__time_stamp = time_stamp
        self.__deleted = deleted

    @property
    def id(self):
        return self.__id
    
    @property
    def order_code(self):
        return self.__order_code
    
    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, val):
        self.__amount = val
    
    @property
    def customer_id(self):
        return self.__customer_id
    @customer_id.setter
    def customer_id(self, val):
        self.__customer_id = val
    
    @property
    def detail(self):
        return self.__detail
    @detail.setter
    def detail(self, val):
        self.__detail = val

    @property
    def note(self):
        return self.__note
    @note.setter
    def note(self, val):
        self.__note = val

    @property
    def progress(self):
        return self.__progress
    @progress.setter
    def progress(self, val):
        self.__progress = val

    @property
    def time_stamp(self):
        return self.__time_stamp
    
    @property
    def deleted(self):
        return self.__deleted
    @deleted.setter
    def deleted(self, val):
        self.__deleted = val
