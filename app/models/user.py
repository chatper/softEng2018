from app import db


# Xρησιμοποίησα την class User για δοκιμές.
# Στο users_controller.py αντί για from models.user import User
# κάντε import την κλάση της Αγγελικής από το αρχείο της.

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    @property
    def __repr__(self):
        return '<User %r>' % self.user

    @property
    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password
        }
