from peewee import SqliteDatabase
from data import DB_TITLE


db = SqliteDatabase(DB_TITLE+'.db')


async def initialize_db():
    from database.user import User
    from database.message import Message
    from database.admin import Admin
    from database.secret_key import Secret_keys
    from sending_messages.admin_msg import send_ntf_admins
    db.connect()
    db.create_tables([User, Message, Admin, Secret_keys], safe=True)
    await send_ntf_admins("Базы данных загруженны.")

def db_close():
    db.close()