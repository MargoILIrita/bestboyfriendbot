import os
import psycopg2

# DATABASE_URL = os.environ['DATABASE_URL']


cur = None

IS_USER_EXIST = '''select count(*) from users_data where chat_id = %s'''
ADD_USER = '''insert into users_data values (%s, %s, 0)'''
UPDATE_BOY_TYPE = '''UPDATE users_data SET boy_type = %s WHERE chat_id = %s;'''

 

try:
    # conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    conn = psycopg2.connect( host="localhost",
    port = 5432,
    database="postgres",
    user="postgres",
    password="")
    cur = conn.cursor()
except Exception as e:
    print(e)
    conn.close()
    

users = {}
users_modes = {}

def is_user_exist(chat_id):
    if chat_id in users.keys():
        return True
    return False

def add_user(chat_id, create_date):
    users[chat_id] = create_date
    cur.execute(ADD_USER,(chat_id, create_date))

def get_boy_type(chat_id):
    return users_modes[chat_id]

def add_boyfriend_type(chat_id, mode):
    users_modes[chat_id] = mode
    cur.execute(UPDATE_BOY_TYPE, (chat_id,mode))

