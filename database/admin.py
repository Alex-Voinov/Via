from peewee import Model, IntegerField, CharField, DateTimeField

class Admin(Model):
    user_id = IntegerField(unique=True, primary_key=True)
    full_name = CharField(null=False)
    email = CharField(null=False)
    invited_by = IntegerField()
    registration_date = DateTimeField()

    class Meta:
        from database.initial import db
        database = db
