def render_reservation_list(reservations):
    return [
        {
            "user_id": reservation.user_id,
            "reservation_id": reservation.reservation_id,
            "reservation_date": reservation.reservation_date,
            "num_guests": reservation.num_guests,
            "special_requests": reservation.special_requests,
            "status": reservation.status
        }
        for reservation in reservations
    ]


def render_reservation_detail(reservation):
    return {
        "user_id": reservation.user_id,
        "reservation_id": reservation.reservation_id,
        "reservation_date": reservation.reservation_date,
        "num_guests": reservation.num_guests,
        "special_requests": reservation.special_requests,
        "status": reservation.status
    }