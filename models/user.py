import datetime
from db import *

class User:
    # Create a user
    def create_user(self, username, password, role):
        create_db_tables()
        last_login = str(datetime.datetime.utcnow())
        conn = connectDB()
        cur = conn.cursor()
        cur.execute('INSERT INTO users (username, password, role, last_login) VALUES (%s, %s, %s, %s, %s)', (username, password, role, last_login))
        conn.commit
        cur.close()
        conn.close()

    # Fetch a list of users
    def get_users(self):
        conn = connectDB()
        cur = conn.cursor()
        cur.execute('SELECT * FROM users')
        conn.commit()
        users = cur.fetchall()
        cur.close()
        conn.close()
        return users

    # Fetch a user
    def get_user(self, username):
        conn = connectDB()
        cur = conn.cursor()
        cur.execute('SELECT * FROM users WHERE username = %s', (username,))
        conn.commit()
        user = cur.fetchone()
        cur.close()
        conn.close()
        return user

    # Delete a user
    def delete_user(self, username):
        conn = connectDB()
        cur = conn.cursor()
        cur.execute('DELETE FROM users WHERE username = %s', (username,))
        cur.close()
        conn.close()
        