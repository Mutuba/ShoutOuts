import psycopg2
import psycopg2.extras
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def connectDB():
    connection_string = 'dbname=shoutout user=shoutout password=shoutout host=localhost'
    try:
        return psycopg2.connect(connection_string)
    except:
        print('Can\'t connect to database')

def create_db_tables():
    queries = [
        'DROP TABLE IF EXISTS "users" CASCADE',
        'DROP TABLE IF EXISTS "comment" CASCADE',
        """
        CREATE TABLE users (
            id SERIAL PRIMARY KEY NOT NULL, 
            username VARCHAR(140) NOT NULL, 
            password VARCHAR(140) NOT NULL, 
            role VARCHAR(140) NOT NULL, 
            last_login VARCHAR(140)
            );
        """,
        """
        CREATE TABLE comment (
            id SERIAL PRIMARY KEY NOT NULL, 
            parent INT, 
            message TEXT NOT NULL, 
            author INT NOT NULL, 
            created_at VARCHAR(140) NOT NULL, 
            updated_at VARCHAR(140) NOT NULL, 
            updated_by VARCHAR(140)
            );
        """
    ]
    run_query_commands(queries)

def run_query_commands(queries):
    connection = None
    try:
       connection = connectDB()
       cursor = connection.cursor()
       for query in queries:
            cursor.execute(query)
       cursor.close()
       connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


if __name__ == '__main__':
    create_db_tables()
