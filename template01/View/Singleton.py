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
    
    @classmethod # a protected class method 
    def _generateToken(cls) -> str:
        token = "" # initialize a string 
        # generate a temporary series randomly 
        while token == "" or (token in cls.__login_status):
            token = "" # set it to an empty string 
            token = token.join( cls._character_list[randint(0, len(cls._character_list)-1)] for i in range(cls._token_length) ) # one of Pythonic ways to generate a string with a random series of characters 
        return token

    @classmethod #(類別方法/函式) 
    def Login(cls, id: str) -> tuple[bool, str]: # public method/function 
        try:
            token = cls._generateToken()
            #print('token=', token) # DEBUG 
            timestamp = datetime.now()
            cls.__login_status[token] = (id, timestamp) # set the value of key-value pair to a tuple: (使用者帳號的ID, 時間戳記) 
            return True, token # 登入成功, 暫時通行證證號 
        except Exception as ex:
            print(str(ex)) # DEBUG 
            #Logger.log(Logger.category_tuple[0], str(ex)) # RELEASE or DEBUG 
            return False, "" # 登入失敗, (無暫時通行證，故無證號) 

    @classmethod
    def Logout(cls, token: str, id: str) -> bool:
        if (token in cls.__login_status) and (cls.__login_status[token][0] == id):
            cls.__login_status.pop(token, None)
            return True
        else:
            return False
    @classmethod
    def LogoutAll(cls, id: str) -> bool:
        tokens_to_be_deleted = [key for key in cls.__login_status if cls.__login_status[key][0] == id] # 'dictionary comprehension' in Python 
        for token in tokens_to_be_deleted:
            cls.__login_status.pop(token, None)
        return True
    
    @classmethod
    def RefreshToken(cls, token: str, id: str) -> tuple[str, str]:
        if not token in cls.__login_status:
            return "", id
        try:
            new_token = cls._generateToken()
            #print('token=', token) # DEBUG 
            timestamp = datetime.now()
            cls.__login_status[new_token] = (id, timestamp) # set the value of key-value pair to a tuple: (使用者帳號的ID, 時間戳記) 
            cls.__login_status.pop(token, None)
            return new_token, id
        except Exception as ex:
            cls.__login_status[token] = (id, datetime.now())
            print(str(ex)) # DEBUG 
            #Logger.log(Logger.category_tuple[0], str(ex)) # RELEASE or DEBUG 
            return token, id
    