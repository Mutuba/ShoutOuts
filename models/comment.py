from datetime import datetime

import psycopg2
import psycopg2.extras

from db import connectDB


class Comment:
    def __init__(self):
        self.current_date = str(datetime.now())
        self.connection = connectDB()
        self.cursor = self.connection.cursor(
            cursor_factory=psycopg2.extras.DictCursor)

        self.current_date = str(datetime.now())

    def browse(self):
        try:
            self.cursor.execute('SELECT * FROM comment;')
        except (Exception, psycopg2.DatabaseError) as error:
            self.connection.rollback()
            return {'status': 'failed', 'data': error}
        comment_list = self.cursor.fetchall()
        if len(comment_list) == 0:
            return {'status': 'success', 'message': 'There are no comments yet'}
        else:
            return {'status': 'success', 'message': 'Comment sent', 'data': comment_list}

    def read(self, id):
        try:
            self.cursor.execute('SELECT * FROM comment WHERE id = %s ;',
                                ([id]))
        except (Exception, psycopg2.DatabaseError) as error:
            self.connection.rollback()
            return {'status': 'failed', 'data': error}
        results = self.cursor.fetchone()
        if results is None:
            return {'status': 'success', 'message': 'The comment does not exist'}
        return results

    def edit(self, id, message, updated_by):
        try:
            self.cursor.execute(
                """
                UPDATE comment SET 
                    message = %s,
                    updated_by = %s,
                    updated_at = %s
                WHERE id = %s;
                """,
                (
                    id,
                    message,
                    updated_by,
                    updated_at
                )
            )
            self.connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            self.connection.rollback()
            return {'status': 'failed', 'data': error}
        return {'status': 'success', 'data': 'Comment updated'}
        
    def add(self, message, author, created_at, updated_at, updated_by=None, parent=None):
        try:
            self.cursor.execute(
                """INSERT INTO comment (message, author, created_at, updated_at, updated_by, parent) 
                VALUES (%s, %s, %s, %s, %s, %s);""",
                (message, author, self.current_date, self.current_date, updated_by, parent))
            self.connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            self.connection.rollback()
            return {'status': 'failed', 'data': error}
        return {'status': 'success', 'message': 'Comment added'}
        
    def delete(self, id):
        try:
            self.cursor.execute('DELETE FROM comment WHERE id = %s ;',
                                ([id]))
            self.connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            self.connection.rollback()
            return {'status': 'failed', 'data': error}
        return {'status': 'success', 'data': 'Comment deleted'}