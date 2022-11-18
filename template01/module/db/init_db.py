#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    from manipulate_db import ManipulateDb
else:
    from module.db.manipulate_db import ManipulateDb

class DatabaseInitializer:
    @classmethod
    def initialize_database(cls):
        #若尚未建立，就創建資料表。
        # table 'Order'
        table_order_sql  = "CREATE TABLE IF NOT EXISTS `Order` ("
        table_order_sql += "`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,"
        table_order_sql += "`order_code` VARCHAR(255) NOT NULL,"
        table_order_sql += "`amount` INT NOT NULL,"
        table_order_sql += "`customer_id` VARCHAR(255) NOT NULL,"
        table_order_sql += "`detail` VARCHAR(255) NOT NULL,"
        table_order_sql += "`note` VARCHAR(255),"
        table_order_sql += "`progress` VARCHAR(120) NOT NULL,"
        table_order_sql += "`time_stamp` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
        table_order_sql += "`deleted` TINYINT(1) NOT NULL"
        table_order_sql += ");"
        # write to database
        ex = ManipulateDb.query_write(table_order_sql)
        if ex != None:
            print(str(ex), "\n while writing 'Order' data table to database.\n")

if __name__ == '__main__':
    # to initialize database
    DatabaseInitializer.initialize_database()
