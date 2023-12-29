from peewee import Model, IntegerField, CharField, BooleanField


class Message(Model):
    msg_id = IntegerField(null=False, primary_key=True)
    user_id = IntegerField(null=False)
    text = CharField(null=True)
    is_deleted = BooleanField(default=False, null=False)

    class Meta:
        from database.initial import db
        database = db


def create_new_msg(
    chat_id: int,
    msg_id: int,
    text_msg: str,
    username: str
):
    from database.user import User
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