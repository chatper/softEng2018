# Αυτά είναι μια αρχική ιδέα, αλλά βασικά πρέπει να δω να χρησιμοποιήσω το flask_security

from flask import Flask, request, make_response, jsonify
from app import app, db
from models.user import User
#from AggelikisFile import AggelikisClass


@app.route('/api/v1.0/users', methods=['GET'])
def home():
    q = User.query.all()
    users = [u.serialize for u in q]
    ret = [{key: u[key] for key in ['email', 'password']} for u in users]
    return make_response(jsonify(ret), 200)


@app.route('/api/v1.0/users', methods=['POST'])
def register():
    existing_user = User.query.filter_by(email=request.json['email']).first()
    if existing_user is not None:
        return make_response(jsonify({'error': 'Email already exists'}), 400)
    new_user = User(**request.json)
    db.session.add(new_user)
    db.session.commit()
    return make_response(jsonify({}), 201)


@app.route('/api/v1.0/users/<user_id>', methods=['GET'])
def profile(user_id):
    q = User.query.filter_by(id=user_id).first()
    if q is None:
        return make_response(jsonify({'error': 'Not found'}), 404)
    existing_user = q.serialize
    ret = {key: existing_user[key] for key in ['email', 'password']}
    return make_response(jsonify(ret), 200)


@app.route('/api/v1.0/users/<user_id>', methods=['DELETE'])
def delete(user_id):
    existing_user = User.query.filter_by(id=user_id).first()
    if existing_user is None:
        return make_response(jsonify({'error': 'Not found'}), 404)
    db.session.delete(existing_user)
    db.session.commit()
    return make_response(jsonify({}), 200)


@app.route('/api/v1.0/users/<user_id>', methods=['PUT'])
def updateProfile(user_id):
    existing_user = User.query.filter_by(id=user_id).first()
    if existing_user is None:
        return make_response(jsonify({'error': 'Not found'}), 404)
    existing_user.password = request.json['password']
    db.session.commit()
    return make_response(jsonify({}), 200)


@app.route('/api/v1.0/users/login', methods=['POST'])
def login():
    q = User.query.filter_by(
        email=request.json['email'], password=request.json['password']).first()
    if q is None:
        return make_response(jsonify({'error': 'Not found'}), 404)
    existing_user = q.serialize
    ret = {existing_user['id']}
    return make_response(jsonify(ret), 200)
