from app import db


# Xρησιμοποίησα την class User για δοκιμές.
# Στο app.py αντί για from models.user import User
# κάντε import την κλάση της Αγγελικής από το αρχείο της.
# Θεώρησα ότι στη βάση δε γίνεται να υπάρχουν δύο rows με ίδια τιμή για το column email
# οπότε θα μπορούσε αυτό να είναι primary key και το id περιττο (;;;)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username