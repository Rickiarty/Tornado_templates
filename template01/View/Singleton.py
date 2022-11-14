from datetime import datetime
from module.logger import Logger

class MonoLogin:

    __login_status = dict()
    
    @classmethod
    def Login(cls, token: str, id: str) -> bool:
        try:
            timestamp = datetime.now()
            cls.__login_status[token] = (id, timestamp)
            return True
        except Exception as ex:
            print(str(ex)) # DEBUG 
            #Logger.log(Logger.category_tuple[0], str(ex))
            return False
