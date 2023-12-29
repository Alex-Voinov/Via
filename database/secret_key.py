from peewee import Model, IntegerField, CharField, BooleanField, DateTimeField



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
        from database.initial import db
        database = db



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

def try_activate_prime(
        probably_secret_key,
        activater_id
    ) -> tuple[bool, int]:
    '''
Осуществляем проверку секретного ключа в базе данных.

Результат проверки - bool-значение (успешно не успешно)
+ статус код:

    0 - ключа не существует в базе данных.

    1 - ключ существует, но ещё не был выдан.

    2 - ключ существует, был выдан, но уже активирован.

    3 - корректный ключ, выданный для активации.    
    '''
    from datetime import datetime
    from database.user import User
    secret_key= Secret_keys.select().where(
        Secret_keys.data==probably_secret_key
    ).first()
    if not secret_key:
        return False, 0
    if not secret_key.issued_by:
        return False, 1
    if secret_key.is_activeted:
        return False, 2
    secret_key.is_activeted = True
    secret_key.by_activeted = activater_id
    secret_key.activeted_date = datetime.now()
    privilege_level = secret_key.privilege_level
    user = User.get_by_id(activater_id)
    user.prime_status = privilege_level
    user.save()
    secret_key.save()
    return True, privilege_level