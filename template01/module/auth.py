from View.Singleton import MonoLogin

class Authentication:
    @classmethod
    def Login(cls, id: str, password: str) -> tuple[bool, str, str]:
        is_valid = cls.IsAccountValid(id=id, password=password)
        if is_valid:
            result, token = MonoLogin.Login(id=id)
            return result, token, id
        else:
            return False, "", ""
    
    @classmethod
    def IsAccountValid(cls, id: str, password: str) -> bool:
        return True # It's NOT implemented yet! DIY. 
