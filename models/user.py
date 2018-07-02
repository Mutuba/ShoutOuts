import datetime 

class User:
    def __init__(self, username, role, last_login, password):
        self.username = username
        self.role = role
        self.last_login = last_login
        self.password = password
    
    def username(self):
        return self.username
        