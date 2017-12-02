from models import Address

def query_cities():
    cities_result = Address.query.with_entities(Address.address_city).filter(Address.restaurant_id >= 1).distinct()
    cities = []
    for i in cities_result:
        cities.append({'city_name': i.address_city})
    return cities