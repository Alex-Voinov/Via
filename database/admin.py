from peewee import Model, IntegerField, CharField, DateTimeField

class Admin(Model):
    user_id = IntegerField(unique=True, primary_key=True)
    full_name = CharField(null=False)
    email = CharField(null=False)
    invited_by = IntegerField(null=False)
    registration_date = DateTimeField(null=False)

    class Meta:
        from database.initial import db
        database = db

def get_id_admins():
    return tuple(map(lambda admin: admin.user_id , Admin.select()))

async def create_superuser():
    from main import bot
    from database.admin import Admin
    from datetime import datetime
    second_name=''
    first_name=''
    email=''
    id = input('Введи свой телеграм-id: ')
    while not id.isdigit():
        id = input('Введи корректный телеграм-id: ') 
    while not second_name:
        second_name = input('Введи вашу фамилию: ').strip()
    while not first_name:    
        first_name = input('Введи ваше имя: ').strip()
    full_name = f'{second_name} {first_name}'.title()
    while not email:
        email = input('Введи ваш email: ')
    date = datetime.now()
    try:
        await bot.send_message(
            id,
            f'Привет, {first_name}! Теперь мы с тобой лучшие друзья)'
        )
        Admin.create(
            user_id=id,
            full_name=full_name,
            email=email,
            invited_by=0,
            registration_date=date
        )
    except Exception as e:
        print(
            f'Произошла ошибка: {e}',
            'Пожалуйста проверьте корректность данных и повторите попытку позже.'
        )
        exit()


