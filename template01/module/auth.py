from View.Singleton import MonoLogin

class Authentication:
    
    @classmethod
    def IsAccountValid(cls, id: str, password: str) -> bool:
        return True # It's NOT implemented yet! DIY. 
    
    @classmethod
    def Login(cls, id: str, password: str) -> tuple[bool, str, str]:
        is_valid = cls.IsAccountValid(id=id, password=password)
        if is_valid:
            result, token = MonoLogin.Login(id=id)
            return result, token, id
        else:
            return False, "", ""
    
    @classmethod
    def Logout(cls, token: str, id: str) -> bool:
        return MonoLogin.Logout(token=token, id=id)
    @classmethod
    def LogoutAll(cls, id: str) -> bool:
        return MonoLogin.LogoutAll(id=id)
    
    @classmethod
    def RefreshToken(cls, token: str, id: str) -> tuple[str, str]:
        return MonoLogin.RefreshToken(token=token, id=id)
    