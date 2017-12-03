from flask import send_file, request, Response
from app import app
import json
import logging

from nyilvantarto.restaurant import *
from nyilvantarto.meal import *
from nyilvantarto.user import *
from nyilvantarto.order import *
from nyilvantarto.address import *
from nyilvantarto.payment import *

user = ""
log = logging.getLogger(__name__)


@app.route('/')
def index():
    return send_file('templates/index.html')


@app.route('/registration', methods=['POST'])
def registration():
    newUser = request.json
    user = query_user_by_name(newUser)
    if user is not None:
        response = Response(status=409)
        return response
    else:
        user_registration(newUser)
        response = Response(status=200)
        return response


@app.route('/checkout', methods=['POST'])
def checkout():
    newOrder = request.json
    status = checkout_order(newOrder)
    response = Response(status=status)
    return response


@app.route('/users', methods=['GET'])
def get_users():
    users = query_users()
    response = Response(response=json.dumps(users), status=200, mimetype='application/json')
    return response


@app.route('/login', methods=['GET', 'POST'])
def login():
    current_user = request.json
    login_user = user_login(current_user)
    if login_user == 202:
        response = Response(status=202, mimetype='application/json')
        return response
    else:
        response = Response(response=json.dumps(login_user), status=200, mimetype='application/json')
        return response


@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = query_restaurants()
    response = Response(response=json.dumps(restaurants), status=200, mimetype='application/json')
    return response


@app.route('/myRestaurant', methods=['GET'])
def get_my_restaurant():
    current_username = request.args.get('username')
    restaurants = query_my_restaurants(current_username)
    response = Response(response=json.dumps(restaurants), status=200, mimetype='application/json')
    return response


@app.route('/meals', methods=['GET'])
def get_meals():
    restaurant_id = request.args.get('restaurant_id')
    meals = query_meals(restaurant_id)
    response = Response(response=json.dumps(meals), status=200, mimetype='application/json')

    return response


@app.route('/orders', methods=['GET'])
def get_orders():
    orders = query_orders()
    response = Response(response=json.dumps(orders), status=200, mimetype='application/json')
    return response


@app.route('/cities', methods=['GET'])
def get_cities():
    cities = query_cities()
    response = Response(response=json.dumps(cities), status=200, mimetype='application/json')
    return response


@app.route('/types', methods=['GET'])
def get_types():
    restaurant_id = request.args.get('restaurant_id')
    types = query_meal_types(restaurant_id)
    response = Response(response=json.dumps(types), status=200, mimetype='application/json')
    return response


@app.route('/payments', methods=['GET'])
def get_payments():
    restaurant_id = request.args.get('restaurant_id')
    payments = query_payments(restaurant_id)
    response = Response(response=json.dumps(payments), status=200, mimetype='application/json')
    return response


@app.route('/addRestaurant', methods=['POST'])
def addRestaurant():
    newRestaurant = request.json
    print(newRestaurant["restaurant"]['restaurant_name'])
    restaurant = query_restaurant_by_name(newRestaurant)
    if restaurant is not None:
        response = Response(status=409)
        return response
    else:
        add_new_restaurant(newRestaurant)
    response = Response(status=200)
    return response


@app.route('/addMeal', methods=['POST'])
def addMeal():
    newMeal = request.json
    add_new_meal(newMeal)
    response = Response(status=200)
    return response


@app.route('/removeMeal', methods=['POST'])
def removeMeal():
    removable_meal = request.json
    remove_meal(removable_meal)
    response = Response(status=200)
    return response


@app.route('/myOrders', methods=['GET'])
def get_my_orders():
    username = request.args.get('username')
    restaurant_id = request.args.get('restaurant_id')
    orders = query_my_orders(username, restaurant_id)
    response = Response(response=json.dumps(orders), status=200, mimetype='application/json')
    return response


@app.route('/paymentTypeStat', methods=['GET'])
def paymentTypeStat():
    username = request.args.get('username')
    restaurant_id = request.args.get('restaurant_id')
    orders = query_payment_type_stat(username, restaurant_id)
    response = Response(response=json.dumps(orders), status=200, mimetype='application/json')
    return response


@app.route('/mealTypeStat', methods=['GET'])
def mealTypeStat():
    username = request.args.get('username')
    restaurant_id = request.args.get('restaurant_id')
    meals = query_meal_type_stat(username, restaurant_id)
    response = Response(response=json.dumps(meals), status=200, mimetype='application/json')
    return response


@app.route('/userData', methods=['GET'])
def userData():
    username = request.args.get('username')
    response_user = query_user_data(username)
    response = Response(response=json.dumps(response_user), status=200, mimetype='application/json')
    return response


@app.route('/editUser', methods=['POST'])
def editUser():
    params = request.json
    status = edit_user(params)
    response = Response(status=status)
    return response


@app.route('/restaurantData', methods=['GET'])
def get_my_restaurant_data():
    restaurant_id = request.args.get('restaurant_id')
    new_restaurant = query_my_restaurant_data(restaurant_id)
    response = Response(response=json.dumps(new_restaurant), status=200, mimetype='application/json')
    return response


@app.route('/editRestaurant', methods=['POST'])
def editRestaurant():
    params = request.json
    restaurant = query_restaurant_by_id(params)
    status = edit_restaurant(params, restaurant)
    response = Response(status=status)
    return response


@app.route('/mealData', methods=['GET'])
def get_my_meal_data():
    meal_id = request.args.get('meal_id')
    response_meal = query_meal_data_by_id(meal_id)
    response = Response(response=json.dumps(response_meal), status=200, mimetype='application/json')
    return response


@app.route('/editMeal', methods=['POST'])
def editMeal():
    params = request.json
    status = edit_meal(params)
    response = Response(status=status)
    return response


if __name__ == '__main__':
    app.run()
