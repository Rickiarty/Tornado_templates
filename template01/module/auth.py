from View.Singleton import MonoLogin

class Authentication:
    @classmethod
    def Login(cls, id: list, password: list) -> tuple[bool, str, str]:
        token = "01234567879012346578901234567879013245678901234567879" # generate a temporary series randomly by yourself 
        
        identity = id
        pwd = password
        print(type(identity), type(pwd)) # DEBUG 
        result = MonoLogin.Login(token=token, id=identity)
        return result, token, identity
