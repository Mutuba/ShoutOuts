from user import User
import sys

def login():
	users = User()
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    for user in users:
        if user == username:
            return "Welcome, you are logged in"
        else:
            return "wrong password"

login()