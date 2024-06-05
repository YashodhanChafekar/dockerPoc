from flask import request, jsonify
from app import app, db, mongo
from app.models import User

@app.route('/')
def home():
    return "Welcome to the Flask Backend!"

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        username = request.json['username']
        user = User(username=username)
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "User added"}), 201

    users = User.query.all()
    users_list = [{"id": user.id, "username": user.username} for user in users]
    return jsonify({"users": users_list})

@app.route('/mongo', methods=['GET', 'POST'])
def add_mongo_user():
    if request.method == 'GET':
        users = mongo.db.users.find({})
        users_list = [user for user in users]
        return jsonify({"users": users_list})
    username = request.json['username']
    mongo.db.users.insert_one({'username': username})
    return jsonify({"message": "User added to MongoDB"}), 201
