from user import User
from models.comment import Comment
import sys
import datetime

def login():
	users = User()
	 
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    for user in users:
        if user == username:
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

login()