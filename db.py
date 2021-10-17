import psycopg2
from config import DATABASE_CONFIG

conn = None
cur = None

IS_USER_EXIST = '''select count(*) from users_data where chat_id = %s'''
ADD_USER = '''insert into users_data values (%s, %s, 0)'''
UPDATE_BOY_TYPE = '''UPDATE users_data SET boy_type = %s WHERE chat_id = %s;'''
FIND_BOY_TYPE = '''select boy_type from users_data where chat_id = %s'''

 

try:
    conn = psycopg2.connect(DATABASE_CONFIG)
    cur = conn.cursor()
except Exception as e:
    print(e)
    conn.close()
    

users = {}
users_modes = {}

def is_user_exist(chat_id):
    try:
        cur.execute(IS_USER_EXIST,(chat_id,))
        cnt = cur.fetchone()
        if cnt[0] == 0:
            return False
        return True
    except Exception as e:
        print(e)

def add_user(chat_id, create_date):
    try:
        cur.execute(ADD_USER,(chat_id, create_date))
        conn.commit()
    except Exception as e:
        print(e)

def get_boy_type(chat_id):
    try:
        cur.execute(FIND_BOY_TYPE,(chat_id,))
        boy_type = cur.fetchone()
        return boy_type[0]
    except Exception as e:
        print(e)
    return users_modes[chat_id]

def add_boyfriend_type(chat_id, mode):
    try:
        cur.execute(UPDATE_BOY_TYPE, (mode, chat_id))
        conn.commit()
    except Exception as e:
        print(e)
