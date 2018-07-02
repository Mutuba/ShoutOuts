from users import User
import sys
from db import *

def reg():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    role = input("Enter the role for the user: ")

    if not username:
        print('Username is required')
    if not password:
        print('Password is required')
        
    User.create_user(username, password, role)
