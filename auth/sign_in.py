from user import User
from models.comment import Comment
import sys
import datetime

def login():
    users = User.get_users()
    
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    user = User.get_user(username)

    if username:
        if user.password == password:
            return "Welcome, you are logged in"
        comments = Comment()
        parent = input("Enter parent comment")
        message = input("Enter comment message")
        created_at = str(datetime.now()) 
        updated_at = str(datetime.now())
        updated_by = user
        author = user
        else:
            return "wrong password"
    return "User not found"
login()