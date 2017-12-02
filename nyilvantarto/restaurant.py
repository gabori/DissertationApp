from app import db
from models import Restaurant, User, Address


def query_restaurants():
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
    return restaurants


def query_my_restaurants(current_username):
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

    return restaurants


def query_restaurant_by_name(newRestaurant):
    restaurant = Restaurant.query.filter(
        Restaurant.restaurant_name == newRestaurant["restaurant"]['restaurant_name']).first()
    return restaurant


def add_new_restaurant(newRestaurant):
    user = User.query.filter(User.user_name == newRestaurant["username"]).first()
    new_restaurant = Restaurant(restaurant_name=newRestaurant["restaurant"]['restaurant_name'],
                                restaurant_description=newRestaurant["restaurant"]['restaurant_description'],
                                delivery_price=newRestaurant["restaurant"]['delivery_price'],
                                delivery_min_time=newRestaurant["restaurant"]['delivery_min_time'],
                                delivery_max_time=newRestaurant["restaurant"]['delivery_max_time'],
                                min_order=newRestaurant["restaurant"]['min_order'], user_id=user.user_id
                                )
    db.session.add(new_restaurant)
    db.session.commit()
    new_address = Address(address_city=newRestaurant["restaurant"]['address']['address_city'],
                          address_street=newRestaurant["restaurant"]['address']['address_street'],
                          address_number=newRestaurant["restaurant"]['address']['address_number'],
                          restaurant_id=new_restaurant.restaurant_id)
    db.session.add(new_address)
    db.session.commit()


def query_restaurant_by_id(params):
    restaurant = Restaurant.query.filter(Restaurant.restaurant_id == params['restaurant_id']).first()
    return restaurant


def edit_restaurant(params, restaurant):
    user = User.query.filter(User.user_id == restaurant.user_id).first()
    modified_restaurant = params['modified_restaurant']
    if user.password == modified_restaurant['current_password']:
        restaurant.restaurant_name = modified_restaurant['restaurant_name']
        restaurant.restaurant_description = modified_restaurant['restaurant_description']
        restaurant.delivery_min_time = modified_restaurant['delivery_min_time']
        restaurant.delivery_max_time = modified_restaurant['delivery_max_time']
        restaurant.min_order = modified_restaurant['min_order']
        restaurant.address.address_city = modified_restaurant['address_city']
        restaurant.address.address_street = modified_restaurant['address_street']
        restaurant.address.address_number = modified_restaurant['address_number']
        db.session.commit()
        status = 200
        return status
    else:
        status = 401
        return status


def query_my_restaurant_data(restaurant_id):
    restaurant = Restaurant.query.filter(Restaurant.restaurant_id == restaurant_id).first()
    address = Address.query.filter(Address.restaurant_id == restaurant_id).first()
    new_restaurant = {'restaurant_id': restaurant.restaurant_id,
                      'restaurant_name': restaurant.restaurant_name,
                      'restaurant_description': restaurant.restaurant_description,
                      'address_city': restaurant.address.address_city,
                      'address_street': restaurant.address.address_street,
                      'address_number': restaurant.address.address_number,
                      'banner': restaurant.banner,
                      'delivery_price': restaurant.delivery_price,
                      'delivery_min_time': restaurant.delivery_min_time,
                      'delivery_max_time': restaurant.delivery_max_time,
                      'min_order': restaurant.min_order}
    return new_restaurant
