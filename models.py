import json

from app import db
from sqlalchemy import Table, Column, Integer, ForeignKey, String, Float, Date, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum

Base = declarative_base()


class User(db.Model):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    user_name = Column(String)
    user_role = Column(String)
    password = Column(String)
    phone_number = Column(String)
    email = Column(String)

    orders = relationship(
        'Order',
        primaryjoin='Order.user_id==User.user_id',
        foreign_keys='(User.user_id)',
        uselist=True, viewonly=True)

    restaurants = relationship(
        'Restaurant',
        primaryjoin='Restaurant.user_id==User.user_id',
        foreign_keys='(User.user_id)',
        uselist=True, viewonly=True)

    addresses = relationship(
        'Address',
        primaryjoin='User.user_id==Address.user_id',
        foreign_keys='(User.user_id)',
        uselist=True, viewonly=True)

    # restaurantID = Column(Integer, ForeignKey('restaurants.restaurant_id'))

    # addresses = relationship("Address", back_populates="user")

    def to_dict(self):
        fields = {
            'user_id': self.user_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'user_name': self.user_name,
            'user_role' : self.user_role,
            'password': self.password,
            'phone_number': self.phone_number,
            'email': self.email
        }
        return fields

    def to_json(self):
        return json.dumps(self.to_dict())


class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    restaurant_id = Column(Integer, primary_key=True)
    restaurant_name = Column(String)
    restaurant_description = Column(String)
    banner = Column(String)
    min_order = Column(Integer)
    delivery_price = Column(Integer)
    delivery_min_time = Column(Integer)
    delivery_max_time = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    # user = relationship("User")
    # payment_id = Column(Integer, ForeignKey('payments.payment_id'))

    orders = relationship(
        'Order',
        primaryjoin='Restaurant.restaurant_id==Order.restaurant_id',
        foreign_keys='(Restaurant.restaurant_id)',
        uselist=True, viewonly=True
    )

    user = relationship(
        'User',
        primaryjoin='Restaurant.user_id==User.user_id',
        foreign_keys='(Restaurant.user_id)',
        uselist=False, viewonly=True
    )

    payment = relationship(
        'PaymentTable',
        primaryjoin='Restaurant.restaurant_id==PaymentTable.restaurant_id',
        foreign_keys='(Restaurant.restaurant_id)',
        uselist=False, viewonly=True)

    meals = relationship(
        'Meal',
        primaryjoin='Restaurant.restaurant_id==Meal.restaurant_id',
        foreign_keys='(Restaurant.restaurant_id)',
        uselist=True, viewonly=True)
    address = relationship(
        'Address',
        primaryjoin='Restaurant.restaurant_id==Address.restaurant_id',
        foreign_keys='(Restaurant.restaurant_id)',
        uselist=False, viewonly=True)

    # meals = relationship("Meal", backref ="restaurant")
    # address = relationship("Address", back_populates="restaurant")

    def to_dict(self):
        fields = {
            'restaurant_id': self.restaurant_id,
            'restaurant_name': self.restaurant_name,
            'restaurant_description': self.restaurant_description,
            'banner': self.banner,
            'min_order': self.min_order,
            'delivery_price': self.delivery_price,
            'delivery_min_time': self.delivery_min_time,
            'delivery_max_time': self.delivery_max_time
        }
        return fields

    def to_json(self):
        return json.dumps(self.to_dict())


class Meal(db.Model):
    __tablename__ = 'meals'
    meal_id = Column(Integer, primary_key=True)
    meal_name = Column(String)
    meal_description = Column(String)
    image_source = Column(String)
    meal_price = Column(Float)
    # order_meals_id = Column(Integer, ForeignKey('order_meals.order_meals_id'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.restaurant_id'))

    restaurant = relationship(
        'Restaurant',
        primaryjoin='Meal.restaurant_id==Restaurant.restaurant_id',
        foreign_keys='(Meal.restaurant_id)',
        uselist=False, viewonly=True)

    """order_meals = relationship(
        'Order_meals',
        primaryjoin='Meal.meals_id==Order_meals.order_meals_id',
        foreign_keys='(Meal.order_meals_id)',
        uselist=False, viewonly=True)"""

    order_meals = relationship(
        'Order_meals',
        primaryjoin='Meal.meal_id==Order_meals.meal_id',
        foreign_keys='(Meal.meal_id)',
        uselist=False, viewonly=True)

    # restaurant = relationhip("Restaurant", back_populates="meals")

    def to_dict(self):
        fields = {
            'meal_id': self.meal_id,
            'meal_name': self.meal_name,
            'meal_description': self.meal_description,
            'image_source': self.image_source,
            'meal_price': self.meal_price,

        }
        return fields

    def to_json(self):
        return json.dumps(self.to_dict())


class Address(db.Model):
    __tablename__ = 'addresses'
    address_id = Column(Integer, primary_key=True)
    address_type = Column(String)
    address_city = Column(String)
    address_street = Column(String)
    address_number = Column(String)
    restaurant_id = Column(Integer, ForeignKey('restaurants.restaurant_id'))
    user_id = Column(Integer, ForeignKey('users.user_id'))

    user = relationship(
        'User',
        primaryjoin='Address.user_id==User.user_id',
        foreign_keys='(Address.user_id)',
        uselist=False, viewonly=True)

    restaurant = relationship(
        'Restaurant',
        primaryjoin='Address.restaurant_id==Restaurant.restaurant_id',
        foreign_keys='(Address.restaurant_id)',
        uselist=False, viewonly=True)

    # user = relationship("User", back_populates="addresses")
    # restaurant = relationship("Restaurant", uselist=False, back_populates = "restaurant")

    def to_dict(self):
        fields = {
            'address_id': self.address_id,
            'address_type': self.address_type,
            'address_city': self.address_city,
            'address_street': self.address_street,
            'address_number': self.address_number,

        }
        return fields

    def to_json(self):
        return json.dumps(self.to_dict())


class Order(db.Model):
    __tablename__ = 'orders'
    order_id = Column(Integer, primary_key=True)
    oder_date = Column(Date)
    order_price = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.restaurant_id'))
    # order_meals_id = Column(Integer, ForeignKey('order_meals.order_meals_id'))

    restaurant = relationship(
        'Restaurant',
        primaryjoin='Restaurant.restaurant_id==Order.restaurant_id',
        foreign_keys='(Order.restaurant_id)',
        uselist=False, viewonly=True)

    user = relationship(
        'User',
        primaryjoin='User.user_id==Order.user_id',
        foreign_keys='(Order.user_id)',
        uselist=False, viewonly=True)

    order_meals = relationship(
        'Order_meals',
        primaryjoin='Order.order_id==Order_meals.order_id',
        foreign_keys='(Order.order_id)',
        uselist=True, viewonly=True)

    def to_dict(self):
        fields = {
            'order_id': self.order_id,
            'order_date': str(self.order_date),
            'order_price': self.order_price,
        }
        return fields

    def to_json(self):
        return json.dumps(self.to_dict())


class Order_meals(db.Model):
    __tablename__ = 'order_meals'
    order_meals_id = Column(Integer, primary_key=True)
    order_meals_quantity = Column(Integer)
    order_meals_price = Column(Integer)
    order_id = Column(Integer, ForeignKey('orders.order_id'))
    meal_id = Column(Integer, ForeignKey('meals.meal_id'))

    order = relationship(
        'Order',
        primaryjoin='Order_meals.order_id==Order.order_id',
        foreign_keys='(Order_meals.order_id)',
        uselist=False, viewonly=True)

    """meals = relationship(
        'Meal',
        primaryjoin='Order_meals.order_meals_id==Meal.order_meals_id',
        foreign_keys='(Order_meals.order_meals_id)',
        uselist=True, viewonly=True)"""
    meals = relationship(
        'Meal',
        primaryjoin='Order_meals.meal_id==Meal.meal_id',
        foreign_keys='(Order_meals.meal_id)',
        uselist=True, viewonly=True)

    def to_dict(self):
        fields = {
            'order_meals_id': self.order_meals_id,
            'order_meals_quantity': self.order_meals_quantity,
            'order_meals_price': self.order_meals_price,
        }
        return fields

    def to_json(self):
        return json.dumps(self.to_dict())


class Payment(Enum):
    CASH = 'Készpénz'
    CREDITCARD = 'Bankkártya'
    SZEPCARD = 'SZÉP kártya'
    ERZSEBETVOUCHER = 'Erzsébet utalvány'


class PaymentTable(db.Model):
    __tablename__ = 'payments'
    payment_id = Column(Integer, primary_key=True)
    cash = Column(Boolean)
    creditcard = Column(Boolean)
    szep_card = Column(Boolean)
    erzsebet_voucher = Column(Boolean)
    restaurant_id = Column(Integer, ForeignKey('restaurants.restaurant_id'))

    restaurant = relationship(
        'Restaurant',
        primaryjoin='PaymentTable.restaurant_id==Restaurant.restaurant_id',
        foreign_keys='(PaymentTable.restaurant_id)',
        uselist=False, viewonly=True)

    def to_dict(self):
        fields = {
            'payment_id': self.payment_id,
            'cash': self.cash,
            'creditcard': self.creditcard,
            'szep_card': self.szep_card,
            'erzsebet_voucher': self.erzsebet_voucher
        }
        return fields

    def to_json(self):
        return json.dumps(self.to_dict())
