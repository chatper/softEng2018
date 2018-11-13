#Αυτά είναι μια αρχική ιδέα, αλλά βασικά πρέπει να δω να χρησιμοποιήσω το flask_security

from flask import Flask, request, make_response, jsonify
from app import app, db
from models.user import User
#from AggelikisFile import AggelikisClass
#Beware of circular dependencies duuuudes!

@app.route('/api/v1.0/users', methods=['GET'])
def home():
    q = User.query.all()
    users = [{'email': u.email, 'password': u.password} for u in q]
    return make_response(jsonify(users), 200)


@app.route('/api/v1.0/users', methods=['POST'])
def register():
    existing_user = User.query.filter_by(email=request.json['email']).first()
    if existing_user is not None:
        return make_response(jsonify({'error': 'Email already exists'}), 400)
    new_user = User(**request.json)
    db.session.add(new_user)
    db.session.commit()
    return make_response(jsonify({}), 201)


@app.route('/api/v1.0/users/<user_email>', methods=['GET'])
def profile(user_email):
    q = User.query.filter_by(email=user_email).first()
    if q is None:
        return make_response(jsonify({'error': 'Not found'}), 404)
    existing_user = {'email': q.email, 'password': q.password}
    return make_response(jsonify(existing_user), 200)


@app.route('/api/v1.0/users/<user_email>', methods=['DELETE'])
def delete(user_email):
    existing_user = User.query.filter_by(email=user_email).first()
    if existing_user is None:
        return make_response(jsonify({'error': 'Not found'}), 404)
    db.session.delete(existing_user)
    db.session.commit()
    return make_response(jsonify({}), 200)


@app.route('/api/v1.0/users/<user_email>', methods=['PUT'])
def updatePassword(user_email):
    existing_user = User.query.filter_by(email=user_email).first()
    if existing_user is None:
        return make_response(jsonify({'error': 'Not found'}), 404)
    existing_user.password = request.json['password']
    db.session.commit()
    return make_response(jsonify({}), 200)


@app.route('/api/v1.0/users/login', methods=['POST'])
def login():
    existing_user = User.query.filter_by(email=request.json['email'], password=request.json['password']).first()
    if existing_user is None:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return make_response(jsonify({}), 200)
