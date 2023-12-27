from peewee import SqliteDatabase, Model, IntegerField, CharField
from sending_messages.admin_msg import send_ntf_admins

db = SqliteDatabase('main_db.db')

class User(Model):
    user_id = IntegerField(unique=True, primary_key=True)
    username = CharField(null=True)


    class Meta:
        database = db

class Message(Model):
    msg_id = IntegerField(null=True, primary_key=True)
    user_id = IntegerField(null=True)
    text = CharField(null=True)


    class Meta:
        database = db

def create_new_msg(
    chat_id: int,
    msg_id: int,
    text_msg: str
):
    Message.create(
        user_id=chat_id,
        msg_id=msg_id,
        text=text_msg
    )

async def initialize_db():
    db.connect()
    db.create_tables([User, Message], safe=True)
    await send_ntf_admins("Базы данных загруженны.")

def db_close():
    db.close()