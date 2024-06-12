from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

from app.models.user_model import User
user_bp = Blueprint("user", __name__)
 

@user_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    phone = data.get("phone")
    role = data.get("role")


    if not email or not password or not name or not phone or not role:
        return jsonify({"error": "Solicitud incorrecta"}), 400

    existing_user = User.find_by_email(email)
    if existing_user:
        return jsonify({"error": "El correo electrónico ya está en uso"}), 400

    new_user = User(name, email, password, phone, role)
    new_user.save()

    return jsonify({"message": "Usuario creado exitosamente"}), 201


@user_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")
    user = User.find_by_email(email)
    if user and check_password_hash(user.password_hash, password):
        access_token = create_access_token(
            identity={"email": email, "role": user.role}
        )
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401