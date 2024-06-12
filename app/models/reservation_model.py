from app.database import db

class Reservation(db.Model):
    __tablename__ = "reservations"
 
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    restaurant_id = db.Column(db.Integer, nullable=False)
    reservation_date = db.Column(db.DateTime, nullable=False)
    num_guests = db.Column(db.Integer, nullable=False)
    special_requests = db.Column(db.String(128), nullable=False)
    status = db.Column(db.String(50), nullable=False)



    def __init__(self, user_id, restaurant_id, reservation_date, num_guess, special_requests, status):
        self.user_id = user_id
        self.restaurant_id = restaurant_id
        self.reservation_date = reservation_date
        self.num_guess = num_guess
        self.special_requests = special_requests
        self.status = status

    def save(self):
        db.session.add(self)
        db.session.commit()
        
    @staticmethod
    def get_all():
        return Reservation.query.all()

 
    @staticmethod
    def get_by_id(id):
        return Reservation.query.get(id)


    def update(self, name=None, adress=None,city= None, phone=None, description= None, rating= None):
        if name is not None:
            self.name = name
        if adress is not None:
            self.adress = adress
        if city is not None:
            self.city = city
        if phone is not None:
            self.phone = phone
        if description is not None:
            self.description = description
        if rating is not None:
            self.rating = rating
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()