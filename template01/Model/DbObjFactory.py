#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from module.db.manipulate_db import ManipulateDb as mdb
from module.encryption import encrypt
from module.hash.salted_hash import SaltingHashFactory
from Model.Database import DbName

class StoreFactory:
    # table `Order`
    class Order:
        pass

if __name__ == "__main__":
    # for unit test
    from Database import DbName
    order1 = DbName.Order()
    order2 = DbName.Order()
    print(str(order1 == order2))
