"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
# from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

jackson_family.add_member({
    "first_name": "Oscar",
    "age": 36,
    "lucky_number": [23, 9, 89]
})

jackson_family.add_member({
    "first_name": "Karen",
    "age": 37,
    "lucky_number": [5, 9, 88]
})

jackson_family.add_member({
    "first_name": "Ian",
    "age": 37,
    "lucky_number": [17, 11, 17]
})

jackson_family.add_member({
    "first_name": "Lauren",
    "age": 37,
    "lucky_number": [6, 8, 19]
})

# Handle/serialize errors like a JSON object


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints


@app.route('/')
def sitemap():
    return generate_sitemap(app)
# ENDPOINT 1: Obtener todos los miembros


@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "family": members
    }
    return jsonify(response_body), 200

# ENDPOINT 2: Obtener un solo miembro
@app.route('/members/<int:member_id>', methods=['GET'])
def get_single_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    return jsonify({"msg": "Miembro no encontrado"}), 400


@app.route('/members', methods=['POST'])
def add_member():
    body = request.get_json()
    if body["age"] <= 0:
        return jsonify({
            "error": 'edad no puede ser igual o menor a 0'
        }), 400
    new_member = jackson_family.add_member(body)
    return jsonify(new_member)

# ENDPOINT 4: Eliminar un miembro

@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_family_member(member_id):
    deleted = jackson_family.delete_member(member_id)
    if deleted:
        return jsonify({"done": True}), 200
    return jsonify({"msg": "Member not found"}), 400


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
