from peewee import SqliteDatabase, Model, IntegerField, CharField, BooleanField, DateTimeField
from sending_messages.admin_msg import send_ntf_admins
from data import DB_TITLE


db = SqliteDatabase(DB_TITLE+'.db')

class User(Model):
    user_id = IntegerField(unique=True, primary_key=True)
    username = CharField(null=True)
    prime_status = IntegerField(null=False, default=0)


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
    invited_by = IntegerField()
    registration_date = DateTimeField()

    class Meta:
        database = db

class Secret_keys(Model):
    from data import LENG_KEY
    data = CharField(max_length=LENG_KEY, unique=True, primary_key=True, null=False)
    privilege_level = IntegerField(null=False)
    created_by = IntegerField(null=False)
    registration_date = DateTimeField(null=False)
    is_issued = BooleanField(default=False, null=False)
    issued_by = IntegerField(null=True)
    issued_date = DateTimeField(null=True)
    is_activeted = BooleanField(default=False, null=False)
    by_activeted = IntegerField(null=True, unique=True)
    activeted_date = DateTimeField(null=True)

    class Meta:
        database = db

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

def get_amount_free_key(privilegies_lvl=0):
    if not privilegies_lvl:
        return Secret_keys.select().where(Secret_keys.is_issued == False).count()
    return Secret_keys.select().where(
        Secret_keys.is_issued == False,
        Secret_keys.privilege_level==privilegies_lvl
    ).count()

def generate_new_key(
        amount_key: int,
        author_id: int,
        privilege_level: int
    ):
    from datetime import datetime
    from data import LENG_KEY
    from random import choice
    from string import ascii_lowercase as letters
    successful_keys = 0
    generate_date = datetime.now()
    while successful_keys < amount_key:
        probably_key = ''.join(choice(letters) for _ in range(LENG_KEY))
        if not Secret_keys.get_or_none(data=probably_key):
            successful_keys += 1
            Secret_keys.create(
                data=probably_key,
                created_by=author_id,
                registration_date=generate_date,
                privilege_level=privilege_level
            )

def issue_prime(author_id, privilege_level: int):
    from datetime import datetime
    key = Secret_keys.select().where(
        Secret_keys.privilege_level == privilege_level,
        Secret_keys.is_issued == False
    ).first()
    if key:
        key.issued_date = datetime.now()
        key.is_issued = True
        key.issued_by = author_id
        key.save()
        return key.data
    return ''
    
def get_user_info(id: int):
    if user:=User.get_by_id(id):
        return user

async def initialize_db():
    db.connect()
    db.create_tables([User, Message, Admin, Secret_keys], safe=True)
    await send_ntf_admins("Базы данных загруженны.")

def db_close():
    db.close()