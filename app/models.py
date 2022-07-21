import datetime
from .app import db


class Pizza(db.Model):
    __tablename__ = 'pizza'
    id = db.Column(db.Integer, primary_key=True)
    pizza_name = db.Column(db.String(50), nullable=False)
    is_sauce = db.Column(db.Boolean())
    is_cheese = db.Column(db.Boolean())
    is_ham = db.Column(db.Boolean())
    is_champignons = db.Column(db.Boolean())
    is_pepper = db.Column(db.Boolean())
    is_olives = db.Column(db.Boolean())
    is_bacon = db.Column(db.Boolean())
    is_corn = db.Column(db.Boolean())
    is_tuna = db.Column(db.Boolean())
    is_pineapple = db.Column(db.Boolean())
    price_30 = db.Column(db.Float())
    price_40 = db.Column(db.Float())
    price_50 = db.Column(db.Float())

class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    street_and_house_number  = db.Column(db.String(50), nullable=False)
    ordered_pizzas = db.Column(db.String(100))
    order_value = db.Column(db.Float())
    is_paid = db.Column(db.Boolean())

class Pizza_customize(db.Model):
    __tablename__ = 'pizza_customize'
    id = db.Column(db.Integer, primary_key=True)
    pizza_name = db.Column(db.String(50), nullable=False)
    is_sauce = db.Column(db.Boolean())
    is_cheese = db.Column(db.Boolean())
    is_ham = db.Column(db.Boolean())
    is_champignons = db.Column(db.Boolean())
    is_pepper = db.Column(db.Boolean())
    is_olives = db.Column(db.Boolean())
    is_bacon = db.Column(db.Boolean())
    is_corn = db.Column(db.Boolean())
    is_tuna = db.Column(db.Boolean())
    is_pineapple = db.Column(db.Boolean())
    size = db.Column(db.Float())
    price = db.Column(db.Float())

class Opinion(db.Model):
    __tablename__ = 'opinion'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.Text(), nullable=False)
    message = db.Column(db.Text(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False, default=datetime.datetime.utcnow)
