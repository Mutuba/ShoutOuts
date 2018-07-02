import datetime
form db import connect

class User:
    def __init__(self, username, role, last_login, password):
        self.username = username
        self.role = role
        self.last_login = last_login
        self.password = password
    
    def username(self):
        return self.username

    def create_comment(self, message, author, created_at, updated_at, updated_by=None, parent=None):
