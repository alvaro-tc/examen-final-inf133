def render_restaurant_list(restaurants):
    return [
        {
            "id": restaurant.id,
            "name": restaurant.name,
            "adress": restaurant.adress,
            "city": restaurant.city,
            "phone": restaurant.phone,
            "description": restaurant.description,
            "rating": restaurant.rating
        }
        for restaurant in restaurants
    ]


def render_restaurant_detail(restaurant):
    return {
        "id": restaurant.id,
        "name": restaurant.name,
        "adress": restaurant.adress,
        "city": restaurant.city,
        "phone": restaurant.phone,
        "description": restaurant.description,
        "rating": restaurant.rating
    }