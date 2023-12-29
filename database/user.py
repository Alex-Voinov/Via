from peewee import Model, IntegerField, CharField

class User(Model):
    user_id = IntegerField(unique=True, primary_key=True)
    username = CharField(null=True)
    prime_status = IntegerField(null=False, default=0)


    class Meta:
        from database.initial import db
        database = db

def get_user_info(id: int):
    if user:=User.get_by_id(id):
        return user