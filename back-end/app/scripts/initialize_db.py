from main import db
from models.user import User
from sqlalchemy.exc import IntegrityError


def create_users():
    agelina = User(
        email='agelina-d@hotmail.com',
        password='eimaithearakanoteleiesanaforesrobo')
    fotini = User(
        email='fotinipan97@gmail.com',
        password='ankanokiallianaforamethnagelinathakanoxarakiri')

    db.session.add(agelina)
    db.session.add(fotini)
    db.session.commit()


print('Creating tables..')
db.create_all()

try:
    print('Trying to create users..')
    create_users()
except IntegrityError as e:
    print('Users could not be created! {}'.format(e))
