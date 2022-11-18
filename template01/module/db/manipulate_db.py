#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pymysql
if __name__ == "__main__":
    from db_settings import DbSettings
elif sys.argv[0].split("/")[-1] == "init_db.py":
    from db_settings import DbSettings
else:
    from module.db.db_settings import DbSettings

class ManipulateDb(DbSettings):

    @classmethod
    def query_read_only(cls, sql_command):
        try:
            # 建立Connection物件 (以'with'包裹，防止連線沒關掉)
            with pymysql.connect(**DbSettings.db_settings) as conn:
                #建立cursor物件
                cursor = conn.cursor()
                #執行語法
                cursor.execute(sql_command)
                #取得整個 data view
                result_view = cursor.fetchall() # to get a whole data view
        except Exception as ex:
            return None, ex
        return result_view, None

    @classmethod
    def query_write(cls, sql_command):
        try:
            # 建立Connection物件 (以'with'包裹，防止連線沒關掉)
            with pymysql.connect(**DbSettings.db_settings) as conn:
                # 建立cursor物件
                cursor = conn.cursor()
                # execute SQL command
                cursor.execute(sql_command)
                # save
                conn.commit()
        except Exception as ex:
            return ex
        return None

if __name__ == "__main__":
    # for unit test 
    sql_command = 'SELECT VERSION()'
    result, ex = ManipulateDb.query_read_only(sql_command)
    if ex == None:
        print(str(result))
    else:
        print("%s\n while executing query '%s' to database.\n" % (str(result), sql_command))
