import psycopg2

def connect():
    conn = None
    try:
        conn = psycopg2.connect("host='localhost' dbname='shoutout' user='shoutout' password=''")
        print('Successfully connected to PostgreSQL!')
        return conn
    except psycopg2.DatabaseError as e:
        if conn:
            conn.rollback()
        print('Cannot connect to PostgreSQL. Error {}'.format(e))
        sys.exit(1)
        