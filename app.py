from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import json_util
import os

app = Flask(__name__)

# Conección a MongoDB
client = MongoClient('mongodb+srv://RealityApp23:RealityApp@appantennas.ii8faau.mongodb.net/?retryWrites=true&w=majority')
db = client['Antennas']  #  el nombre de la base de datos
collection = db['StudentsAntenas']  #  el nombre de colección
comentarios= db['ComentariosAntenas'] #  el nombre de colección
codsala= db['CodeSalaAntenas'] #  el nombre de colección

@app.route('/addCodSal', methods=['POST'])
def add_code():
    data = request.get_json()
    print(data)
    # Verificar si el código de sala ya existe
    existing_code = codsala.find_one({'codigo_clase': data.get('codigo_clase')})
    
    if existing_code is None:
        # no existe, insertar el nuevo código de sala
        result = codsala.insert_one(data)
        return jsonify({"message": "Código de sala agregado satisfactoriamente", "_id": str(result.inserted_id)}), 201
    else:
        # ya existe, enviar un mensaje indicando que ya existe
        return jsonify({"message": "El código de sala ya existe"}), 400

@app.route('/addStudent', methods=['POST'])
def add_item():
    data = request.get_json()
    print(data.get('codigo_clase'))
    existing_code = codsala.find_one({'codigo_clase': data.get('codigo_clase')})
    
    if existing_code is None:
        return jsonify({"message": "The room code does not exist, I cannot add that student"}), 400
    else:
        result = collection.insert_one(data)
        return jsonify({"message": "student successfully added", "_id": str(result.inserted_id)}), 201

    

@app.route('/addComentario', methods=['POST'])
def add_comentario():
    data = request.get_json()
    result = comentarios.insert_one(data)
    return jsonify({"message": "Comentario agregado satisfactoriamente", "_id": str(result.inserted_id)}), 201

@app.route('/getCodes', methods=['GET'])
def get_Codes():
    items = list(codsala.find())
    for item in items:
        item['_id'] = str(item['_id'])  
    return jsonify({"items": items}), 200

@app.route('/students', methods=['GET'])
def get_items():
    items = list(collection.find())
    for item in items:
        item['_id'] = str(item['_id'])  
    return jsonify({"items": items}), 200

@app.route('/getStudents/<int:codigo_clase>', methods=['GET'])
def get_students(codigo_clase):
    students = collection.find({'codigo_clase': codigo_clase})
    students_list = [student for student in students]
    return json_util.dumps(students_list), 200

@app.route('/getComentary', methods=['GET'])
def get_Comentary():
    items = list(comentarios.find())
    for item in items:
        item['_id'] = str(item['_id'])  
    return jsonify({"items": items}), 200

@app.route('/deleteStudents/<int:codigo_clase>', methods=['DELETE'])# 6 caracteres
def delete_students(codigo_clase):
    result = collection.delete_many({'codigo_clase': codigo_clase})
    codigo=codsala.delete_many({'codigo_clase': codigo_clase})
    return jsonify({'message': f'{result.deleted_count} students deleted and {codigo.deleted_count} room code also'}), 200


@app.route('/deleteCode/<int:codigo_clase>', methods=['DELETE'])# 6 caracteres
def delete_codes(codigo_clase):
    result = codsala.delete_many({'codigo_clase': codigo_clase})
    codigo=collection.delete_many({'codigo_clase': codigo_clase})
    return jsonify({'message': f'{result.deleted_count} room code removed and {codigo.deleted_count} and stundents deleted vinculated with room code '}), 200


if __name__ == "__main__":
    app.run()
