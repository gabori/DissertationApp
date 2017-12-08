from app import db
from models import User, Address
import datetime
import jwt


def query_user_by_name(newUser):
    user = User.query.filter(User.user_name == newUser['user_name']).first()
    return user


def query_user_by_username(username):
    user = User.query.filter(User.user_name == username).first()
    return user


def user_registration(newUser):
    new_user = User(first_name=newUser['first_name'], last_name=newUser['last_name'],
                    user_name=newUser['user_name'],
                    password=newUser['password'], phone_number=newUser['phone_number'], email=newUser['email'],
                    user_role="user", point=0)

    db.session.add(new_user)
    db.session.commit()
    user = User.query.filter(User.user_name == newUser['user_name']).first()
    address = Address(address_type="Lakcím", address_city=newUser['city'], address_street=newUser['street'],
                      address_number=newUser['number'], user_id=user.user_id)
    db.session.add(address)
    db.session.commit()


def query_users():
    user_result = User.query.all()
    users = []
    for i in user_result:
        addresses = []
        for j in i.addresses:
            addresses.append(j.to_dict())
        users.append({'user_name': i.user_name, 'user_addresses': addresses})
    return users


def edit_user(params):
    user = User.query.filter(User.user_name == params['username']).first()
    modified_user = params['modified_user']
    if user.password == modified_user['current_password']:
        if modified_user['new_password'] != modified_user['confirm_new_password']:
            status = 409
            return status
        user.password = modified_user['new_password']
        db.session.commit()
        status = 200
        return status
    else:
        status = 401
        return status


def query_user_data(username):
    user = User.query.filter(User.user_name == username).first()
    addresses = Address.query.filter(Address.user_id == user.user_id).all()
    address = []
    for i in addresses:
        address.append({'address_id': i.address_id, 'address_type': i.address_type,
                        'address_city': i.address_city, 'address_street': i.address_street,
                        'address_number': i.address_number})
    response_user = {'first_name': user.first_name, 'last_name': user.last_name, 'user_name': user.user_name,
                     'password': user.password, 'email': user.email, 'point': user.point,
                     'phone_number': user.phone_number, 'addresses': address}
    return response_user


def user_login(current_user):
    user = 0;
    user_result = User.query.all()
    for i in user_result:
        if current_user['username'] == i.user_name and current_user['password'] == i.password:
            payload = {
                "uid": i.user_id,
                "name": i.user_name,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=2)
            }

            token = jwt.encode(payload=payload, key="SECRET_KEY")
            login_user = {'username': i.user_name, 'password': i.password, 'user_role': i.user_role,
                          'token': token.decode("utf-8")}

            user = 1
            break;
    if user != 1:
        status = 202
        return status
    else:
        return login_user
