from flask import request, jsonify
from main import app, db
from models.user import User, user_schema, users_schema, user_password_schema
from marshmallow import ValidationError, validate
from werkzeug.exceptions import HTTPException

def fail(msg, status_code):
    return (jsonify({'status': 'fail', 'errors': msg}), status_code)


def success(msg, status_code):
    return (jsonify({'status': 'success', 'data': msg}), status_code)


@app.errorhandler(Exception)
def handle_error(e):
    print("Server error:", e)
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code


@app.route('/api/v1.0/users', methods=['GET'])
def home():
    q = User.query.all()
    users = users_schema.dump(q)
    return success(users.data, 200)


@app.route('/api/v1.0/users', methods=['POST'])
def register():
    try:
        user_schema.validate(request.json)
    except ValidationError as err:
        return fail(err.messages, 422)

    existing_user = User.query.filter_by(email=request.json['email']).first()
    if existing_user is not None:
        return fail('Email address already in database', 409)

    user = User(**request.json)
    db.session.add(user)
    db.session.commit()

    return success(None, 201)


@app.route('/api/v1.0/users/<user_id>', methods=['GET'])
def profile(user_id):
    q = User.query.filter_by(id=user_id).first()
    if q is None:
        return fail('User not found', 404)

    user = user_schema.dump(q)
    return success(user.data, 200)


@app.route('/api/v1.0/users/<user_id>', methods=['DELETE'])
def delete(user_id):
    existing_user = User.query.filter_by(id=user_id).first()
    if existing_user is None:
        return fail('User not found', 404)

    deleted_user = user_schema.dump(existing_user)
    db.session.delete(existing_user)
    db.session.commit()

    return success(deleted_user.data, 200)


@app.route('/api/v1.0/users/<user_id>', methods=['PUT'])
def updateProfile(user_id):
    try:
        user_password_schema.validate(request.json)
    except ValidationError as err:
        return fail(err.messages, 422)

    existing_user = User.query.filter_by(id=user_id).first()
    if existing_user is None:
        return fail('User not found', 404)
    if existing_user.password != request.json['password']:
        return fail('Password did not match', 400)

    existing_user.password = request.json['newPassword']
    db.session.commit()

    user = user_schema.dump(existing_user)
    return success(user.data, 200)


@app.route('/api/v1.0/users/login', methods=['POST'])
def login():
    try:
        user_schema.validate(request.json)
    except ValidationError as err:
        return fail(err.messages, 422)

    q = User.query.filter_by(
        email=request.json['email'],
        password=request.json['password']).first()

    if q is None:
        return fail('User not found', 404)

    return success({"id": q.id}, 200)
