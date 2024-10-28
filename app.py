from flask import Flask, request, jsonify
from datastructure import FamilyStructure
import random

app = Flask(__name__)
jackson_family = FamilyStructure('Jackson')

def _generateId():
    return random.randint(0, 99999999)

# Inicializa miembros
John = {
    "id": _generateId(),
    "first_name": "John",
    "last_name": jackson_family.last_name,
    "age": 32,
    "lucky_numbers": [2, 13, 136]
}

Marta = {
    "id": _generateId(),
    "first_name": "Marta",
    "last_name": jackson_family.last_name,
    "age": 22,
    "lucky_numbers": [12, 3, 66]
}

jackson_family.add_member(John)
jackson_family.add_member(Marta)

@app.route('/')
def hello():
    return '¡EL SERVIDOR API ESTÁ EN FUNCIONAMIENTO!'

@app.route('/members', methods=['GET'])
def get_all_members():
    return jsonify(jackson_family.get_all_members()), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    else:
        return jsonify({"error": "Miembro no encontrado."}), 404




@app.route('/post-member', methods=['POST'])
def add_member():
    try:
        member_data = request.get_json()
        member_data['id'] = _generateId()
        member_data['last_name'] = jackson_family.last_name
        jackson_family.add_member(member_data)
        return jsonify(member_data), 201  # Respuesta 201 al agregar con éxito
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Error del servidor

# Ejecutar la aplicación
app.run(host='localhost', port=5004, debug=True)
