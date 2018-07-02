from users import User
import sys

def reg():
	user = User()
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    role = input(":Enter the role for the user")

    user.create_user(username, password, role)

    return "User details added"
    
reg()