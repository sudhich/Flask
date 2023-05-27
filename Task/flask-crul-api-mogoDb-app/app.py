from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# MongoDB configuration
app.config['MONGO_URI'] = 'mongodb://localhost:27017/crud'
mongo = PyMongo(app)

@app.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.table.find()
    output = []
    for user in users:
        output.append({'name': user['name'], 'email': user['email']})
    return jsonify({'result': output})

@app.route('/users', methods=['POST'])
def add_user():
    user = {'name': request.json['name'], 'email': request.json['email']}
    result = mongo.db.table.insert_one(user)
    return jsonify({'message': 'User added successfully', 'id': str(result.inserted_id)})
@app.route('/many_users', methods=['POST'])
def add_users():
    users = request.json  # Assuming the request contains a JSON array of user objects
    result = mongo.db.table.insert_many(users)
    if result.inserted_ids:
        output = {'message': 'Users added successfully', 'ids': [str(id) for id in result.inserted_ids]}
    else:
        output = 'No users added'
    return jsonify({'result': output})
from flask import make_response

@app.route('/users/download', methods=['GET'])
def download_users():
    users = mongo.db.table.find()
    output = []
    for user in users:
        output.append({'name': user['name'], 'email': user['email']})

    # Create a CSV file containing the user data
    csv_data = 'name,email\n'
    for user in output:
        csv_data += f"{user['name']},{user['email']}\n"

    # Create a response with the CSV file as an attachment
    response = make_response(csv_data)
    response.headers['Content-Disposition'] = 'attachment; filename=users.csv'
    response.mimetype = 'text/csv'
    return response


@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = mongo.db.table.find_one({'_id': ObjectId(id)})
    if user:
        output = {'name': user['name'], 'email': user['email']}
    else:
        output = 'No user found'
    return jsonify({'result': output})

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    user = {'name': request.json['name'], 'email': request.json['email']}
    result = mongo.db.table.update_one({'_id': ObjectId(id)}, {'$set': user})
    if result.modified_count > 0:
        output = {'message': 'User updated successfully'}
    else:
        output = 'No user found'
    return jsonify({'result': output})

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    result = mongo.db.table.delete_one({'_id': ObjectId(id)})
    if result.deleted_count > 0:
        output = {'message': 'User deleted successfully'}
    else:
        output = 'No user found'
    return jsonify({'result': output})

if __name__ == '__main__':
    app.run(debug=True)