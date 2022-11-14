from View.Singleton import MonoLogin

class Authentication:
    @classmethod
    def Login(cls, id: list[str], password: list[str]) -> tuple[bool, str, str]:
        token = "01234567879012346578901234567879013245678901234567879" # generate a temporary series randomly by yourself 
        
        identity = id[0]
        pwd = password[0]
        print(identity, pwd) # DEBUG 
        result = MonoLogin.Login(token=token, id=identity)
        return result, token, identity
