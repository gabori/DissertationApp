from tests.base import BaseTestCase
from nyilvantarto.user import *


class UserEmptyTestCase(BaseTestCase):
    def test_no_users(self):
        person_results = query_users()
        self.assertEqual(person_results, [])

    def test_add_user(self):
        user_registration(newUser=
                          {'user_name': 'user_name', 'password': 'name', 'first_name': 'first', 'last_name': 'last',
                           'phone_number': '06202587854', 'email': 'email', 'city': 'miskolc', 'street': 'fő',
                           'number': '1'})

        person_results = query_users()
        self.assertEquals(len(person_results), 1)
        result = person_results[0]
        self.assertEquals(result['user_name'], 'user_name')
