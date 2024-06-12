from flask import Blueprint, request, jsonify
from app.models.reservation_model import Reservation
from app.views.reservation_view import render_reservation_list, render_reservation_detail
from app.utils.decorators import jwt_required, roles_required

reservation_bp = Blueprint("reservation", __name__)


@reservation_bp.route("/reservations", methods=["GET"])
@jwt_required
@roles_required(roles="admin")
def get_reservations():
    reservations = Reservation.get_all()
    return jsonify(render_reservation_list(reservations))



@reservation_bp.route("/reservations/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles="admin")
def get_reservation(id):
    reservation = Reservation.get_by_id(id)
    if reservation:
        return jsonify(render_reservation_detail(reservation))
    return jsonify({"error": "Reservacion no encontrado"}), 404

@reservation_bp.route("/reservations", methods=["POST"])
@jwt_required
@roles_required(roles="admin")
def create_reservation():
    data = request.json
    user_id = data.get("user_id")
    restaurant_id = data.get("restaurant_id")
    reservation_date = data.get("reservation_date")
    num_guests = data.get("num_guests")
    special_requests = data.get("special_requests")
    status = data.get("status")
    
    if not user_id or not restaurant_id or not reservation_date or not (num_guests>=0) or not special_requests or not status:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    reservation = Reservation(user_id=user_id, restaurant_id=restaurant_id, reservation_date=reservation_date, num_guests=num_guests)
    reservation.save()
    return jsonify(render_reservation_detail(reservation)), 201


@reservation_bp.route("/reservations/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles="admin")
def update_reservation(id):
    reservation = Reservation.get_by_id(id)
    if not reservation:
        return jsonify({"error": "Reservacion no encontrado"}), 404
    data = request.json
    user_id = data.get("user_id")
    restaurant_id = data.get("restaurant_id")
    reservation_date = data.get("reservation_date")
    num_guests = data.get("num_guests")
    special_requests = data.get("special_requests")
    status = data.get("status")
    reservation.update(user_id=user_id, restaurant_id=restaurant_id, reservation_date=reservation_date, num_guests=num_guests)
    return jsonify(render_reservation_detail(reservation))



@reservation_bp.route("/reservations/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles="admin")
def delete_reservation(id):
    reservation = Reservation.get_by_id(id)
    if not reservation:
        return jsonify({"error": "Reservacion no encontrado"}), 404
    reservation.delete()
    return "", 204
