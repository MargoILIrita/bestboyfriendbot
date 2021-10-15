import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

CREATE_SHEME = '''CREATE ROLE admin;
ALTER ROLE admin WITH LOGIN PASSWORD 'password' NOSUPERUSER NOCREATEDB NOCREATEROLE;
CREATE DATABASE database_name OWNER user_name;
REVOKE ALL ON DATABASE database_name FROM PUBLIC;
GRANT CONNECT ON DATABASE database_name TO user_name;
GRANT ALL ON DATABASE database_name TO user_name;'''

# позже разберусь
try:
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()
except Exception as e:
    print(e)
finally:
    conn.close()



users = {}
users_modes = {}

def is_user_exist(chat_id):
    if chat_id in users.keys():
        return True
    return False

def add_user(chat_id, create_date):
    users[chat_id] = create_date

def get_boy_type(chat_id):
    return users_modes[chat_id]

def add_boyfriend_type(chat_id, mode):
    users_modes[chat_id] = mode
