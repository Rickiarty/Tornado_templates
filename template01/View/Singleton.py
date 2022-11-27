from datetime import datetime
from random import randint
from module.logger import Logger

# a static class(靜態類別) for universal unique log-in management 
class MonoLogin:
    # You should NEVER instantiate(實例化) this class(類別) to an instance(實例). 

    # private member(s) 
    __login_status = dict() # unique dictionary recording current log-in status of accounts 
    # protected member(s)
    _character_list = [
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", 
        "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", 
        "U", "V", "W", "X", "Y", "Z", 
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 
        "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", 
        "u", "v", "w", "x", "y", "z", 
        "#", "=", "&", "^", 
    ] # a list from which this program unit can choose randomly 
    _token_length = 128
    
    @classmethod #(類別方法/函式) 
    def Login(cls, id: str) -> tuple[bool, str]: # public method/function 
        try:
            token = "" # generate a temporary series randomly 
            token = token.join( cls._character_list[randint(0, len(cls._character_list)-1)] for i in range(cls._token_length) ) # one of Pythonic ways to generate a string with a random series of characters 
            print('token=', token) # DEBUG
            if not token in cls.__login_status:
                timestamp = datetime.now()
                cls.__login_status[token] = (id, timestamp)
                return True, token # 登入成功, 暫時通行證證號 
            else:
                return cls.Login(id=id)
        except Exception as ex:
            print(str(ex)) # DEBUG 
            #Logger.log(Logger.category_tuple[0], str(ex)) # RELEASE or DEBUG 
            return False, "" # 登入失敗, (無暫時通行證，故無證號) 
