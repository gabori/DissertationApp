from app import db
from models import Restaurant, User, Order, Meal
from datetime import datetime
from collections import Counter
import collections


def query_meals(restaurant_id):
    meals_result = Meal.query.join(Meal.restaurant).filter(Restaurant.restaurant_id == int(restaurant_id)).all()
    meals = [meal.to_dict() for meal in meals_result]
    return meals


def query_meal_types(restaurant_id):
    types_result = Meal.query.with_entities(Meal.meal_type).filter(Meal.restaurant_id == restaurant_id).distinct()
    types = []
    for i in types_result:
        types.append({'meal_type': i.meal_type})
    return types


def add_new_meal(newMeal):
    # restaurant = Restaurant.query.filter(newMeal['restaurant_id'] == Restaurant.restaurant_id).first()
    new_meal = Meal(meal_name=newMeal['meal']["meal_name"],
                    meal_description=newMeal['meal']['meal_description'],
                    meal_price=newMeal['meal']['meal_price'],
                    meal_type=newMeal['meal']['meal_type'],
                    restaurant_id=newMeal['restaurant_id'])
    db.session.add(new_meal)
    db.session.commit()


def remove_meal(removable_meal):
    Meal.query.filter(Meal.meal_id == removable_meal['meal_id']).delete()
    db.session.commit()


def query_meal_data_by_id(meal_id):
    meal = Meal.query.filter(Meal.meal_id == meal_id).first()
    response_meal = {'meal_id': meal.meal_id,
                     'meal_name': meal.meal_name,
                     'meal_description': meal.meal_description,
                     'meal_type': meal.meal_type,
                     'meal_price': meal.meal_price,
                     'restaurant_id': meal.restaurant_id}
    return response_meal


def edit_meal(params):
    meal = Meal.query.filter(Meal.meal_id == params['meal_id']).first()
    restaurant = Restaurant.query.filter(Restaurant.restaurant_id == params['restaurant_id']).first()
    user = User.query.filter(User.user_id == restaurant.user_id).first()
    modified_meal = params['modified_meal']
    if user.password == modified_meal['current_password']:
        meal.meal_name = modified_meal['meal_name']
        meal.meal_description = modified_meal['meal_description']
        meal.meal_type = modified_meal['meal_type']
        meal.meal_price = modified_meal['meal_price']
        meal.restaurant_id = params['restaurant_id']
        meal.image_source = meal.image_source
        db.session.commit()
        status = 200
        return status
    else:
        status = 401
        return status


def query_meal_type_stat(username, restaurant_id):
    user = User.query.filter(User.user_name == username).first()
    meal_types = Meal.query.filter(Meal.restaurant_id == restaurant_id).group_by(Meal.meal_type).all()
    orders_result = Order.query.filter(Order.restaurant_id == restaurant_id).all()
    meals = []
    for i in meal_types:
        tmp = 0
        for j in orders_result:
            for k in j.order_meals:
                if k.order_id == j.order_id:
                    for l in k.meals:
                        if i.meal_type == l.meal_type:
                            tmp += 1
        meals.append({"y": tmp, "label": i.meal_type})
    return meals


def query_order_datetime_stat(restaurant_id):
    orders_result = Order.query.filter(Order.restaurant_id == restaurant_id).all()
    dates = []
    for i in orders_result:
        dates.append(datetime.strptime(i.order_date, "%Y-%m-%d %H:%M:%S").hour)

    a = dict(Counter(dates))
    ordered_a = collections.OrderedDict(sorted(a.items()))
    values = []
    keys = []
    dates_result = []
    for i in ordered_a.values():
        values.append(i)
    for i in ordered_a:
        keys.append(i)
    for i in range(0, len(values)):
        dates_result.append({"y": values[i], "label": keys[i]})

    return dates_result
