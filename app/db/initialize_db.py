# Initialize dummy database for experiments


def seed_data():
    from app import db
    from models.user import User
    agelina = User(email='agelina-d@hotmail.com',
                   password='eimaithearakanoteleiesanaforesrobo')
    fotini = User(email='fotinipan97@gmail.com',
                  password='ankanokiallianaforamethnagelinathakanoxarakiri')
    db.session.add(agelina)
    db.session.add(fotini)
    db.session.commit()


def main():
    from app import db
    db.create_all()
    seed_data()


if __name__ == '__main__':
    main()
