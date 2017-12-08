from models import Restaurant, User, Order, PaymentTable, Payment


def query_payments(restaurant_id):
    payments_result = PaymentTable.query.filter(PaymentTable.restaurant_id == restaurant_id).all()
    payments = []
    for i in payments_result:
        if (i.cash == True):
            payments.append({'payment': Payment.CASH.value})
        if (i.creditcard == True):
            payments.append({'payment': Payment.CREDITCARD.value})
        if (i.szep_card == True):
            payments.append({'payment': Payment.SZEPCARD.value})
        if (i.erzsebet_voucher == True):
            payments.append({'payment': Payment.ERZSEBETVOUCHER.value})
    return payments


def query_payment_type_stat(username, restaurant_id):
    user = User.query.filter(User.user_name == username).first()
    payment = PaymentTable.query.filter(PaymentTable.restaurant_id == restaurant_id).first()
    payments = []
    for key, value in payment.to_dict().items():
        if value == 1:
            payments.append(key)
    payments_dictionary = {}
    for i in payments:
        if i == "cash":
            payments_dictionary[i] = Order.query.filter(Order.restaurant_id == restaurant_id).filter(
                Order.payment_type == "Készpénz").count()
        if i == "creditcard":
            payments_dictionary[i] = Order.query.filter(Order.restaurant_id == restaurant_id).filter(
                Order.payment_type == "Bankkártya").count()
        if i == "szep_card":
            payments_dictionary[i] = Order.query.filter(Order.restaurant_id == restaurant_id).filter(
                Order.payment_type == "SZÉP kártya").count()
        if i == "erzsebet_voucher":
            payments_dictionary[i] = Order.query.filter(Order.restaurant_id == restaurant_id).filter(
                Order.payment_type == "Erzsébet utalvány").count()
    orders = []
    for key, value in payments_dictionary.items():
        orders.append({"y": value, "label": key})
    return orders
