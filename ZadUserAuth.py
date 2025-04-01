'''
Zaprojektuj klase Userauth, która będzie symulować system logowania użytkownika w aplikacji mobilnej.
'''
class UserNotFoundError(Exception):
     pass

class WrongPasswordError(Exception):
     pass

class UserAuth:
    def __init__(self, users):
        self.users = users #słownik

    def login(self, username, password):
        self.username = username
        self.password = password
        if username not in self.users.keys():
            raise UserNotFoundError("Nie ma podanego użytkownika w systemie")
        if self.users[self.username] != self.password:
            raise WrongPasswordError("Podane hasło jest błędne")
        return "Zalogowano poprawnie"
        
auth = UserAuth({"admin": "1234", "user": "abcd"}) 

test = [("admin", "1234"), ("unknown", "pass"), ("user", "wrongpass")]

for username, password in test:
    try:
        print(auth.login(username, password))  
    except Exception as e:
        print(f"Błąd: {e}")
