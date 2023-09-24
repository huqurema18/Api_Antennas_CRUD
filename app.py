from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import json_util
import os

app = Flask(__name__)

# Conectar a MongoDB
client = MongoClient('mongodb+srv://RealityApp23:RealityApp@appantennas.ii8faau.mongodb.net/?retryWrites=true&w=majority')
db = client['Antennas']  # Reemplazar con el nombre de tu base de datos
collection = db['StudentsAntenas']  # Reemplazar con el nombre de tu colección

@app.route('/addStudent', methods=['POST'])
def add_item():
    data = request.get_json()
    result = collection.insert_one(data)
    return jsonify({"message": "Student added successfully", "_id": str(result.inserted_id)}), 201


@app.route('/students', methods=['GET'])
def get_items():
    items = list(collection.find())
    for item in items:
        item['_id'] = str(item['_id'])  # Convertir ObjectId a str para la serialización JSON
    return jsonify({"items": items}), 200

@app.route('/getStudents/<int:codigo_clase>', methods=['GET'])
def get_students(codigo_clase):
    students = collection.find({'codigo_clase': codigo_clase})
    students_list = [student for student in students]
    return json_util.dumps(students_list), 200


@app.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    collection.delete_one({"_id": ObjectId(item_id)})
    return jsonify({"message": "Item deleted successfully"}), 200

@app.route('/deleteStudents/<int:codigo_clase>', methods=['DELETE'])
def delete_students(codigo_clase):
    result = collection.delete_many({'codigo_clase': codigo_clase})
    return jsonify({'message': f'{result.deleted_count} students deleted'}), 200


if __name__ == "__main__":
    app.run(debug=True)
