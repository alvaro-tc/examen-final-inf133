from flask import Blueprint, request, jsonify
from app.models.restaurant_model import Restaurant
from app.views.restaurant_view import render_restaurant_list, render_restaurant_detail
from app.utils.decorators import jwt_required, roles_required

restaurant_bp = Blueprint("restaurant", __name__)


@restaurant_bp.route("/restaurants", methods=["GET"])
@jwt_required
@roles_required(roles="admin")
def get_restaurants():
    restaurants = Restaurant.get_all()
    return jsonify(render_restaurant_list(restaurants))



@restaurant_bp.route("/restaurants/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles="admin")
def get_restaurant(id):
    restaurant = Restaurant.get_by_id(id)
    if restaurant:
        return jsonify(render_restaurant_detail(restaurant))
    return jsonify({"error": "Restaurante no encontrado"}), 404

@restaurant_bp.route("/restaurants", methods=["POST"])
@jwt_required
@roles_required(roles="admin")
def create_restaurant():
    data = request.json
    name = data.get("name")
    address = data.get("address")
    city = data.get("city")
    phone = data.get("phone")
    description = data.get("description")
    rating = data.get("rating")
    
    if not name or not address or not city or not phone or not description:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    restaurant = Restaurant(name=name, address=address, city=city, phone=phone, description=description, rating=rating)
    restaurant.save()
    return jsonify(render_restaurant_detail(restaurant)), 201


@restaurant_bp.route("/restaurants/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles="admin")
def update_restaurant(id):
    restaurant = Restaurant.get_by_id(id)
    if not restaurant:
        return jsonify({"error": "Restaurante no encontrado"}), 404
    data = request.json
    name = data.get("name")
    address = data.get("address")
    city = data.get("city")
    phone = data.get("phone")
    description = data.get("description")
    rating = data.get("rating")
    restaurant.update(name,address,city,phone,description,rating)
    return jsonify(render_restaurant_detail(restaurant))



@restaurant_bp.route("/restaurants/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles="admin")
def delete_restaurant(id):
    restaurant = Restaurant.get_by_id(id)
    if not restaurant:
        return jsonify({"error": "Restaurante no encontrado"}), 404
    restaurant.delete()
    return "", 204
