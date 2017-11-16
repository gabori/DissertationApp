from flask import Flask, send_file, request, redirect, render_template, make_response, Response, session, url_for
from app import app, db
from models import User, Restaurant, Meal, Order, Order_meals, Address, PaymentTable, Payment
import json
import logging
import datetime

user = ""
log = logging.getLogger(__name__)


@app.route('/')
def index():
    return send_file('templates/index.html')


@app.route('/registration', methods=['POST'])
def registration():
    newUser = request.json
    user = User.query.filter(User.user_name == newUser['user_name']).first()
    print(newUser['user_name'])
    if user is not None:
        response = Response(status=409)
        return response
    else:
        new_user = User(first_name=newUser['first_name'], last_name=newUser['last_name'],
                        user_name=newUser['user_name'],
                        password=newUser['password'], phone_number=newUser['phone_number'], email=newUser['email'])
        db.session.add(new_user)
        db.session.commit()
        response = Response(status=200)
        return response


@app.route('/checkout', methods=['POST'])
def checkout():
    newOrder = request.json

    order_price = 0
    print("king")
    for i in newOrder['cart']:
        order_price += i['meal_price']
        meal_id = i['meal_id']
    meal = Meal.query.filter(Meal.meal_id == meal_id).first()
    user = User.query.filter(User.user_name == newOrder['username']).first()
    new_Order = Order(oder_date=datetime.datetime.now(), user_id=user.user_id, order_price=order_price,
                      restaurant_id=meal.restaurant_id)
    db.session.add(new_Order)
    db.session.commit()

    for i in newOrder['cart']:
        new_order_meals = Order_meals(order_meals_quantity=1, order_meals_price=i['meal_price'], meal_id=i['meal_id'],
                                      order_id=new_Order.order_id)
        db.session.add(new_order_meals)
        db.session.commit()
    response = Response(status=200)
    return response


@app.route('/users', methods=['GET'])
def get_users():
    user_result = User.query.all()
    users = []
    for i in user_result:
        addresses = []
        for j in i.addresses:
            addresses.append(j.to_dict())
        users.append({'user_name': i.user_name, 'user_addresses': addresses})
    response = Response(response=json.dumps(users), status=200, mimetype='application/json')
    return response


@app.route('/login', methods=['GET', 'POST'])
def login():
    user_result = User.query.all()
    current_user = request.json

    for i in user_result:
        if current_user['username'] == i.user_name and current_user['password'] == i.password:
            login_user = {'username': i.user_name, 'password': i.password, 'user_role': i.user_role}
            global user;
            user = 1
            break;
    if user != 1:
        response = Response(status=401)
        return response
    else:
        response = Response(response=json.dumps(login_user), status=200, mimetype='application/json')
        return response


@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    # print(session['username'])
    restaurant_result = Restaurant.query.all()
    restaurants = [{'restaurant_id': restaurant.restaurant_id,
                    'restaurant_name': restaurant.restaurant_name,
                    'restaurant_description': restaurant.restaurant_description,
                    'restaurant_city': restaurant.address.address_city,
                    'restaurant_street': restaurant.address.address_street,
                    'restaurant_number': restaurant.address.address_number,
                    'banner': restaurant.banner,
                    'delivery_price': restaurant.delivery_price,
                    'delivery_min_time': restaurant.delivery_min_time,
                    'delivery_max_time': restaurant.delivery_max_time,
                    'min_order': restaurant.min_order} for restaurant in restaurant_result]
    response = Response(response=json.dumps(restaurants), status=200, mimetype='application/json')
    return response


@app.route('/myRestaurant', methods=['GET'])
def get_my_restaurant():
    current_username = request.args.get('username')
    print(current_username)
    user = User.query.filter(User.user_name == current_username).first()
    restaurant_result = Restaurant.query.filter(Restaurant.user_id == user.user_id).all()
    restaurants = [{'restaurant_id': restaurant.restaurant_id,
                    'restaurant_name': restaurant.restaurant_name,
                    'restaurant_description': restaurant.restaurant_description,
                    'restaurant_city': restaurant.address.address_city,
                    'restaurant_street': restaurant.address.address_street,
                    'restaurant_number': restaurant.address.address_number,
                    'banner': restaurant.banner,
                    'delivery_price': restaurant.delivery_price,
                    'delivery_min_time': restaurant.delivery_min_time,
                    'delivery_max_time': restaurant.delivery_max_time,
                    'min_order': restaurant.min_order} for restaurant in restaurant_result]
    response = Response(response=json.dumps(restaurants), status=200, mimetype='application/json')
    return response


@app.route('/meals', methods=['GET'])
def get_meals():
    restaurant_id = request.args.get('restaurant_id')
    print(int(restaurant_id))
    meals_result = Meal.query.join(Meal.restaurant).filter(Restaurant.restaurant_id == int(restaurant_id)).all()
    meals = [meal.to_dict() for meal in meals_result]
    response = Response(response=json.dumps(meals), status=200, mimetype='application/json')

    return response


@app.route('/orders', methods=['GET'])
def get_orders():
    orders_result = Order.query.all()
    orders = []
    for i in orders_result:
        meals = []
        for j in i.order_meals:
            for z in j.meals:
                meals.append({'meal_name': z.meal_name})
        orders.append({'order_id': i.order_id, 'order_meals': meals, 'oder_price': i.order_price})
    response = Response(response=json.dumps(orders), status=200, mimetype='application/json')
    # print(orders)
    return response


@app.route('/cities', methods=['GET'])
def get_cities():
    cities_result = Address.query.with_entities(Address.address_city).filter(Address.restaurant_id >= 1).distinct()
    cities = []
    for i in cities_result:
        cities.append({'city_name': i.address_city})
        # cities.append(i.address_city)
    response = Response(response=json.dumps(cities), status=200, mimetype='application/json')
    # print(cities)
    return response


@app.route('/payments', methods=['GET'])
def get_payments():
    payments_result = PaymentTable.query.filter(PaymentTable.restaurant_id == 1).all()
    payments = []
    for i in payments_result:
        if (i.cash == True):
            payments.append({'cash': Payment.CASH.value})
        if (i.creditcard == True):
            payments.append({'creditcard': Payment.CREDITCARD.value})
        if (i.szep_card == True):
            payments.append({'szep_card': Payment.SZEPCARD.value})
        if (i.erzsebet_voucher == True):
            payments.append({'erzsebet_voucher': Payment.ERZSEBETVOUCHER.value})
    response = Response(response=json.dumps(payments), status=200, mimetype='application/json')
    print(payments)
    return response


@app.route('/addRestaurant', methods=['POST'])
def addRestaurant():
    newRestaurant = request.json
    restaurant = Restaurant.query.filter(Restaurant.restaurant_name == newRestaurant['restaurant_name']).first()
    print(newRestaurant)
    if restaurant is not None:
        response = Response(status=409)
        return response
    else:
        new_restaurant = Restaurant(restaurant_name=newRestaurant['restaurant_name'],
                                    restaurant_description=newRestaurant['restaurant_description'])
        db.session.add(new_restaurant)
        db.session.commit()
        new_address = Address(address_city=newRestaurant['address']['address_city'],
                              address_street=newRestaurant['address']['address_street'],
                              address_number=newRestaurant['address']['address_number'],
                              restaurant_id=new_restaurant.restaurant_id)
        db.session.add(new_address)
        db.session.commit()
    response = Response(status=200)
    return response


@app.route('/addMeal', methods=['POST'])
def addMeal():
    newMeal = request.json

    print(newMeal)
    user = User.query.filter(User.user_name == newMeal['username']).first()

    restaurant = Restaurant.query.filter(user.user_id == Restaurant.user_id).first()
    new_meal = Meal(meal_name=newMeal['meal_name'],
                    meal_description=newMeal['meal_description'],
                    meal_price=newMeal['meal_price'],
                    restaurant_id=restaurant.restaurant_id)
    db.session.add(new_meal)
    db.session.commit()
    response = Response(status=200)
    return response


@app.route('/removeMeal', methods=['POST'])
def removeMeal():
    removable_meal = request.json
    Meal.query.filter(Meal.meal_id == removable_meal['meal_id']).delete()
    db.session.commit()
    response = Response(status=200)
    return response


@app.route('/myOrders', methods=['GET'])
def get_my_orders():
    username = request.args.get('username')
    restaurant_id = request.args.get('restaurant_id')
    user = User.query.filter(User.user_name == username).first()
    restaurant = Restaurant.query.filter(Restaurant.restaurant_id == restaurant_id).first()
    rest = []
    rest.append({'restaurant_id': restaurant.restaurant_id, 'restaurant_name': restaurant.restaurant_name})
    orders = []
    orders_result = Order.query.filter(Order.restaurant_id == restaurant.restaurant_id).all()
    print(orders_result)
    for i in orders_result:
        meals = []
        for j in i.order_meals:
            if j.order_id == i.order_id:
                for k in j.meals:
                    meals.append({'meal_name': k.meal_name})
        customer = User.query.filter(User.user_id == i.user_id).first()
        orders.append({'order_id': i.order_id, 'order_date': str(i.oder_date), 'order_meals': meals,
                       'order_price': i.order_price, 'restaurant_id': i.restaurant_id,
                       'restaurant': rest, 'user_id': customer.user_name})

    response = Response(response=json.dumps(orders), status=200, mimetype='application/json')
    print(orders)
    return response


@app.route('/userData', methods=['GET'])
def userData():
    username = request.args.get('username')
    user = User.query.filter(User.user_name == username).first()
    addresses = Address.query.filter(Address.user_id == user.user_id).all()
    address = []
    for i in addresses:
        address.append({'address_id': i.address_id, 'address_type': i.address_type,
                        'address_city': i.address_city, 'address_street': i.address_street,
                        'address_number': i.address_number})
    response_user = {'first_name': user.first_name, 'last_name': user.last_name, 'user_name': user.user_name,
                     'password': user.password, 'email': user.email,
                     'phone_number': user.phone_number, 'addresses': address}
    print(response_user)
    response = Response(response=json.dumps(response_user), status=200, mimetype='application/json')
    return response


@app.route('/editUser', methods=['POST'])
def editUser():
    params = request.json
    user = User.query.filter(User.user_name == params['username']).first()
    modified_user = params['modified_user']
    print(modified_user)
    if user.password == modified_user['current_password']:
        if modified_user['new_password'] != modified_user['confirm_new_password']:
            response = Response(status=409)
            return response
        user.password = modified_user['new_password']
        db.session.commit()
        response = Response(status=200)
        return response
    else:
        response = Response(status=401)
        return response


if __name__ == '__main__':
    app.run()
