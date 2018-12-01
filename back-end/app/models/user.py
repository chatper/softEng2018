from main import db
from marshmallow import Schema, fields, validate


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    @property
    def __repr__(self):
        return '<User %r>' % self.user


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Email(
        required=True,
        validate=validate.Email(error='Not a valid email address'))
    password = fields.Str(
        required=True,
        validate=[validate.Length(min=4, max=40)],
        load_only=True)


class UserPasswordSchema(Schema):
    password = fields.Str(
        required=True,
        validate=[validate.Length(min=4, max=40)],
        load_only=True)
    new_password = fields.Str(
        required=True,
        validate=[validate.Length(min=4, max=40)],
        load_only=True,
        load_from="newPassword")


user_schema = UserSchema(strict=True)
users_schema = UserSchema(strict=True, many=True)
user_password_schema = UserPasswordSchema(strict=True)
