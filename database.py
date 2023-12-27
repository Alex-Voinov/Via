from peewee import SqliteDatabase, Model, IntegerField, CharField, BooleanField
from sending_messages.admin_msg import send_ntf_admins

db = SqliteDatabase('main_db.db')

class User(Model):
    user_id = IntegerField(unique=True, primary_key=True)
    username = CharField(null=True)
    is_prime = BooleanField(null=False, default=False)


    class Meta:
        database = db

class Message(Model):
    msg_id = IntegerField(null=False, primary_key=True)
    user_id = IntegerField(null=False)
    text = CharField(null=True)
    is_deleted = BooleanField(default=False, null=False)

    class Meta:
        database = db


class Admin(Model):
    user_id = IntegerField(unique=True, primary_key=True)
    full_name = CharField(null=False)
    email = CharField(null=False)

def create_new_msg(
    chat_id: int,
    msg_id: int,
    text_msg: str,
    username: str
):
    Message.create(
        user_id=chat_id,
        msg_id=msg_id,
        text=text_msg
    )
    if not User.get_or_none(user_id=chat_id):
        User.create(
            user_id=chat_id,
            username=username
        )

async def messages_to_update(user_id):
    from main import bot
    data = Message.select().where((Message.user_id == user_id) & (Message.is_deleted == False))
    for message in data:
        try: await bot.delete_message(user_id, message.msg_id)
        except: 1
        message.is_deleted = True
        message.save()

async def initialize_db():
    db.connect()
    db.create_tables([User, Message, Admin], safe=True)
    await send_ntf_admins("Базы данных загруженны.")

def db_close():
    db.close()