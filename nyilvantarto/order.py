from app import db
from models import Restaurant, User, Meal, Order, Order_meals
import datetime
from time import gmtime, strftime


def checkout_order(newOrder):
    order_price = 0
    for i in newOrder['cart']:
        order_price += i['meal_price']
        meal_id = i['meal_id']
    payment = newOrder['payment']
    param_point = newOrder['point']
    # print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    point = (order_price // 1000) * 3
    meal = Meal.query.filter(Meal.meal_id == meal_id).first()
    user = User.query.filter(User.user_name == newOrder['username']).first()
    new_Order = Order(order_date=strftime("%Y-%m-%d %H:%M:%S", gmtime()), user_id=user.user_id, order_price=order_price,
                      restaurant_id=meal.restaurant_id, payment_type=payment['payment'])
    if param_point == 0:
        user.point = user.point + point
    elif param_point == -1:
        user.point = point
    else:
        user.point = param_point + point
    db.session.add(new_Order)
    db.session.commit()
    for i in newOrder['cart']:
        new_order_meals = Order_meals(order_meals_quantity=1, order_meals_price=i['meal_price'], meal_id=i['meal_id'],
                                      order_id=new_Order.order_id)
        db.session.add(new_order_meals)
        db.session.commit()
    status = 200
    return status


def query_orders():
    orders_result = Order.query.all()
    orders = []
    for i in orders_result:
        meals = []
        for j in i.order_meals:
            for z in j.meals:
                meals.append({'meal_name': z.meal_name})
        orders.append({'order_id': i.order_id, 'order_meals': meals, 'order_price': i.order_price})
    return orders


def query_my_orders(username, restaurant_id):
    user = User.query.filter(User.user_name == username).first()
    restaurant = Restaurant.query.filter(Restaurant.restaurant_id == restaurant_id).first()
    rest = []
    rest.append({'restaurant_id': restaurant.restaurant_id, 'restaurant_name': restaurant.restaurant_name})
    orders = []
    orders_result = Order.query.filter(Order.restaurant_id == restaurant.restaurant_id).all()
    for i in orders_result:
        meals = []
        for j in i.order_meals:
            if j.order_id == i.order_id:
                for k in j.meals:
                    meals.append({'meal_name': k.meal_name})
        customer = User.query.filter(User.user_id == i.user_id).first()
        orders.append({'order_id': i.order_id, 'order_date': str(i.order_date), 'order_meals': meals,
                       'order_price': i.order_price, 'payment_type': i.payment_type, 'restaurant_id': i.restaurant_id,
                       'restaurant': rest, 'user_id': customer.user_name})
    return orders
