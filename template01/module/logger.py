import json
from datetime import datetime

class Logger:
    category_tuple = ('login') # implement this yourself 

    @classmethod
    def log(cls, category: str, msg: str):
        now = datetime.now()
        with open("./log/{}.log".format(now.date()), "a") as log_f:
            record = {
                str(now): { 'category': category, 'msg': msg }
            }
            log_f.write(json.dumps(record) + "\n")
