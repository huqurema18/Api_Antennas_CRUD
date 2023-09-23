from flask import Flask, request, jsonify
from pymongo import MongoClient
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
    return jsonify({"message": "Item added successfully", "_id": str(result.inserted_id)}), 201

@app.route('/items', methods=['GET'])
def get_items():
    items = list(collection.find())
    for item in items:
        item['_id'] = str(item['_id'])  # Convertir ObjectId a str para la serialización JSON
    return jsonify({"items": items}), 200

@app.route('/items/<item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    collection.update_one({"_id": ObjectId(item_id)}, {"$set": data})
    return jsonify({"message": "Item updated successfully"}), 200

@app.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    collection.delete_one({"_id": ObjectId(item_id)})
    return jsonify({"message": "Item deleted successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
