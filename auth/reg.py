from users import User
import sys

def reg():
	user = User()
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    role = input("Enter your role")

    user.add['username'] = username
    user.add['password'] = password
    user.add['role'] = role

    return "User details added"
    
reg()