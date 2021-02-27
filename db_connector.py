import pymysql
from datetime import date
import configparser

# Connection to props.ini file
config = configparser.ConfigParser()
config.read('props.ini')

def db_conn():
    conn = pymysql.connect(
        host=config.get('CREDS', 'HOST'),
        port=3306,
        user=config.get('CREDS', 'USERNAME'),
        password=config.get('CREDS', 'PASSWORD'),
        db=config.get('CREDS', 'DB'),
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )
    conn.autocommit(True)

    return conn


def get_table():
    try:
        conn = db_conn()
        try:
            conn.connect()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM project_table")
            for row in cursor:
                print(row)
        except Exception as e:
            print('Query failed')
            print(e)
        finally:
            conn.close()
    except Exception as e:
        print('MySQL connection failed')
        print(e)

def get_data(id):

    try:
        conn = db_conn()

        try:
            conn.connect()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM project_table WHERE id = %s", id)
            for row in cursor:
                name = row['name']
            return name
        except Exception as e:
            print('Query failed')
            print(e)
        finally:
            conn.close()
    except Exception as e:
        print('MySQL connection failed')
        print(e)

def set_data(id, name):

    try:
        conn = db_conn()

        try:
            today = date.today()
            conn.connect()
            cursor = conn.cursor()
            cursor.execute("INSERT into project_table VALUES (%s, %s, %s)", (id, name, today))
        except Exception as e:
            print('Query failed')
            print(e)
        finally:
            conn.close()

    except Exception as e:
        print('MySQL connection failed')
        print(e)

def update(id, name):

    try:
        conn = db_conn()

        try:
            conn.connect()
            cursor = conn.cursor()

            cursor.execute("UPDATE project_table SET name = %s WHERE id = %s", (name, id))
        except Exception as e:
            print('Query failed')
            print(e)
        finally:
            conn.close()
    except Exception as e:
        print('MySQL connection failed')
        print(e)

def remove(id):

    try:
        conn = db_conn()

        try:
            conn.connect()
            cursor = conn.cursor()

            cursor.execute("DELETE FROM project_table WHERE id = %s", id)
        except Exception as e:
            print('Query failed')
            print(e)
        finally:
            conn.close()
    except Exception as e:
        print('MySQL connection failed')
        print(e)
