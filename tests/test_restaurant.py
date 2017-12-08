from tests.base import BaseTestCase
from nyilvantarto.restaurant import *
from nyilvantarto.user import *
import index


class RestaurantEmptyTestCase(BaseTestCase):
    def test_no_restaurants(self):
        restaurant_results = query_restaurants()
        self.assertEqual(restaurant_results, [])

    def test_add_restaurant(self):
        user_registration(newUser=
                          {'user_name': 'admin', 'password': 'name', 'first_name': 'first', 'last_name': 'last',
                           'phone_number': '06202587854', 'email': 'email', 'city': 'miskolc', 'street': 'fő',
                           'number': '1'})
        add_new_restaurant(newRestaurant=
                           {'restaurant': {'restaurant_name': 'név', 'restaurant_description': 'desc',
                                           'address': {'address_city': 'Miskolc', 'address_street': 'fő',
                                                       'address_number': '2'}, 'delivery_price': '230',
                                           'min_order': '230', 'delivery_min_time': '230', 'delivery_max_time': '230'},
                            'username': 'admin'})

        restaurant_results = query_restaurants()
        self.assertEquals(len(restaurant_results), 1)
        result = restaurant_results[0]
        self.assertEquals(result['restaurant_name'], 'név')
