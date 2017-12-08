from app import db
from models import *
from nyilvantarto import *

if __name__ == '__main__':
    print("Create population...")
    user1 = User(user_name='gabori95', password='gabori', first_name='Péter', last_name='Gábori',
                 phone_number='06202587854', email='gabori@gmail.com', user_role="admin", point=0)
    user2 = User(user_name='feher2', password='feher', first_name='Péter', last_name='Fehér',
                 phone_number='06302587854', email='feher@gmail.com', user_role="admin", point=0)
    user3 = User(user_name='arsenal86', password='arsenal', first_name='József', last_name='Nagy',
                 phone_number='06702587854', email='arsenal@gmail.com', user_role="user", point=34)
    user4 = User(user_name='kiss14', password='kiss', first_name='Edit', last_name='Kiss',
                 phone_number='06302837043', email='kiss@gmail.com', user_role="user", point=140)
    user5 = User(user_name='nagymiki', password='nagymiki', first_name='Miklós', last_name='Nagy',
                 phone_number='06302344212', email='nagymikil@gmail.com', user_role="user", point=450)
    user6 = User(user_name='holga', password='holga', first_name='Olga', last_name='Horváth',
                 phone_number='06201237898', email='holga@gmail.com', user_role="user", point=0)

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(user4)
    db.session.add(user5)
    db.session.add(user6)
    db.session.commit()

    restaurant1 = Restaurant(restaurant_name="Mckalmár", restaurant_description="Családiás vendéglő Miskolc szívében.",
                             banner="/static/images/restaurant_logo.jpg", min_order=1200, delivery_price=300,
                             delivery_min_time=40, delivery_max_time=50,
                             user_id=1)
    restaurant2 = Restaurant(restaurant_name="Csülök csárda",
                             restaurant_description="Itt sütik a város legjobb csülkét.",
                             banner="/static/images/restaurant_logo.jpg", min_order=1000, delivery_price=400,
                             delivery_min_time=40, delivery_max_time=50,
                             user_id=1)
    restaurant3 = Restaurant(restaurant_name="PizzaTime", restaurant_description="A város legjobb pizzázója.",
                             banner="/static/images/restaurant_logo.jpg", min_order=1000, delivery_price=0,
                             delivery_min_time=50, delivery_max_time=50,
                             user_id=2)
    restaurant4 = Restaurant(restaurant_name="Filó Pizzéria", restaurant_description="Pizzák akár 500ft-tól is.",
                             banner="/static/images/restaurant_logo.jpg", min_order=900, delivery_price=300,
                             delivery_min_time=40, delivery_max_time=60,
                             user_id=2)
    restaurant5 = Restaurant(restaurant_name="Rapid ételbár", restaurant_description="Olcsó és finom.",
                             banner="/static/images/restaurant_logo.jpg", min_order=1200, delivery_price=300,
                             delivery_min_time=40, delivery_max_time=50,
                             user_id=1)
    restaurant6 = Restaurant(restaurant_name="Feher Ökör", restaurant_description="Tradicionális kisvendéglő.",
                             banner="/static/images/restaurant_logo.jpg", min_order=1100, delivery_price=0,
                             delivery_min_time=40, delivery_max_time=60,
                             user_id=2)
    db.session.add(restaurant1)
    print(restaurant1.min_order)
    db.session.add(restaurant2)
    db.session.add(restaurant3)
    db.session.add(restaurant4)
    db.session.add(restaurant5)
    db.session.add(restaurant6)
    db.session.commit()

    address1 = Address(address_type="Lakcím", address_city="Miskolc", address_street="Csabavezér", address_number="22",
                       user_id="1")
    address2 = Address(address_type="Lakcím", address_city="Miskolc", address_street="Széchenyi", address_number="22",
                       user_id="2")
    address3 = Address(address_type="Lakcím", address_city="Miskolc", address_street="Csabavezér", address_number="20",
                       user_id="3")
    address4 = Address(address_type="Lakcím", address_city="Miskolc", address_street="Vörösmarty Mihály",
                       address_number="2",
                       user_id="4")
    address5 = Address(address_type="Lakcím", address_city="Ózd", address_street="Bolyki", address_number="93",
                       user_id="5")

    address6 = Address(address_type="Lakcím", address_city="Ózd", address_street="Árpád", address_number="6",
                       user_id="6")

    address7 = Address(address_type="Lakcím", address_city="Ózd", address_street="Bolyki", address_number="4",
                       restaurant_id="5")
    address8 = Address(address_type="Lakcím", address_city="Ózd", address_street="Vasvár", address_number="6",
                       restaurant_id="4")
    address9 = Address(address_type="Lakcím", address_city="Ózd", address_street="Géza", address_number="10",
                       restaurant_id="6")
    address10 = Address(address_type="Lakcím", address_city="Msikolc", address_street="Széchenyi", address_number="15",
                        restaurant_id="1")
    address11 = Address(address_type="Lakcím", address_city="Msikolc", address_street="Széchenyi", address_number="18",
                        restaurant_id="2")
    address12 = Address(address_type="Lakcím", address_city="Msikolc", address_street="Fő", address_number="15",
                        restaurant_id="3")
    db.session.add(address1)
    db.session.add(address2)
    db.session.add(address3)
    db.session.add(address4)
    db.session.add(address5)
    db.session.add(address6)
    db.session.add(address7)
    db.session.add(address8)
    db.session.add(address9)
    db.session.add(address10)
    db.session.add(address11)
    db.session.add(address12)
    db.session.commit()

    meal1 = Meal(meal_name="Son-go-ku pizza", meal_description="Paradicsom alap, sonka, gomba, kukorica, sajt",
                 image_source="/static/images/meal_logo.jpg", meal_price=1000, meal_type="Pizza", restaurant_id=1)
    meal2 = Meal(meal_name="Sonkás pizza", meal_description="Paradicsom alap, sonka, sajt",
                 image_source="/static/images/meal_logo.jpg", meal_price=900, meal_type="Pizza", restaurant_id=1)
    meal3 = Meal(meal_name="Négy sajtos pizza", meal_description="Paradicsom alap, 4 fajta sajt",
                 image_source="/static/images/meal_logo.jpg", meal_price=1100, meal_type="Pizza", restaurant_id=1)
    meal4 = Meal(meal_name="Hamburger", meal_description="12 dkg marhahúspogácsa, zöldségek, buci",
                 image_source="/static/images/meal_logo.jpg", meal_price=600, meal_type="Hamburger", restaurant_id=1)
    meal5 = Meal(meal_name="Sajtburger", meal_description="12 dkg marhahúspogácsa, zöldségek, buci, sajt",
                 image_source="/static/images/meal_logo.jpg", meal_price=800, meal_type="Hamburger", restaurant_id=1)
    meal6 = Meal(meal_name="Párolt rizs", meal_description="12 dkg",
                 image_source="/static/images/meal_logo.jpg", meal_price=350, meal_type="Köret", restaurant_id=1)
    meal7 = Meal(meal_name="Sültkrumpli", meal_description="12 dkg",
                 image_source="/static/images/meal_logo.jpg", meal_price=350, meal_type="Köret", restaurant_id=1)
    meal8 = Meal(meal_name="Coca-cola", meal_description="3,3 dl",
                 image_source="/static/images/meal_logo.jpg", meal_price=250, meal_type="Üdítő", restaurant_id=1)
    meal9 = Meal(meal_name="Sprite", meal_description="3,3 dl",
                 image_source="/static/images/meal_logo.jpg", meal_price=250, meal_type="Üdítő", restaurant_id=1)
    meal10 = Meal(meal_name="Rántott sajt", meal_description="Két 8 dkg-os sajt szelettből.",
                  image_source="/static/images/meal_logo.jpg", meal_price=600, meal_type="Frissensült", restaurant_id=1)
    meal11 = Meal(meal_name="Roston csirkemell", meal_description="16 dkg, diétás.",
                  image_source="/static/images/meal_logo.jpg", meal_price=600, meal_type="Frissensült", restaurant_id=1)

    meal12 = Meal(meal_name="Son-go-ku pizza", meal_description="Paradicsom alap, sonka, gomba, kukorica, sajt",
                  image_source="/static/images/meal_logo.jpg", meal_price=1200, meal_type="Pizza", restaurant_id=2)
    meal13 = Meal(meal_name="Sonkás pizza", meal_description="Paradicsom alap, sonka, sajt",
                  image_source="/static/images/meal_logo.jpg", meal_price=1100, meal_type="Pizza", restaurant_id=2)
    meal14 = Meal(meal_name="Sült csülök", meal_description="Pékné módra.",
                  image_source="/static/images/meal_logo.jpg", meal_price=1500, meal_type="Frissensült",
                  restaurant_id=2)
    meal15 = Meal(meal_name="Csülkös bableves", meal_description="Gazdagon.",
                  image_source="/static/images/meal_logo.jpg", meal_price=1200, meal_type="Leves", restaurant_id=2)
    meal16 = Meal(meal_name="Hús leves", meal_description="Marhahúsból, csiga tésztával.",
                  image_source="/static/images/meal_logo.jpg", meal_price=600, meal_type="Leves", restaurant_id=2)
    meal17 = Meal(meal_name="Párolt rizs", meal_description="12 dkg",
                  image_source="/static/images/meal_logo.jpg", meal_price=350, meal_type="Köret", restaurant_id=2)
    meal18 = Meal(meal_name="Sültkrumpli", meal_description="12 dkg",
                  image_source="/static/images/meal_logo.jpg", meal_price=350, meal_type="Köret", restaurant_id=2)
    meal19 = Meal(meal_name="Coca-cola", meal_description="3,3 dl",
                  image_source="/static/images/meal_logo.jpg", meal_price=250, meal_type="Üdítő", restaurant_id=2)
    meal20 = Meal(meal_name="Sprite", meal_description="3,3 dl",
                  image_source="/static/images/meal_logo.jpg", meal_price=200, meal_type="Üdítő", restaurant_id=2)
    meal21 = Meal(meal_name="Rántott sajt", meal_description="Két 8 dkg-os sajt szelettből.",
                  image_source="/static/images/meal_logo.jpg", meal_price=600, meal_type="Frissensült", restaurant_id=2)
    meal22 = Meal(meal_name="Roston csirkemell", meal_description="16 dkg, diétás.",
                  image_source="/static/images/meal_logo.jpg", meal_price=600, meal_type="Frissensült", restaurant_id=2)

    meal23 = Meal(meal_name="Son-go-ku pizza", meal_description="Paradicsom alap, sonka, gomba, kukorica, sajt",
                  image_source="/static/images/meal_logo.jpg", meal_price=1000, meal_type="Pizza", restaurant_id=3)
    meal24 = Meal(meal_name="Sonkás pizza", meal_description="Paradicsom alap, sonka, sajt",
                  image_source="/static/images/meal_logo.jpg", meal_price=900, meal_type="Pizza", restaurant_id=3)
    meal25 = Meal(meal_name="Négy sajtos pizza", meal_description="Paradicsom alap, 4 fajta sajt",
                  image_source="/static/images/meal_logo.jpg", meal_price=1100, meal_type="Pizza", restaurant_id=3)
    meal26 = Meal(meal_name="Hamburger", meal_description="12 dkg marhahúspogácsa, zöldségek, buci",
                  image_source="/static/images/meal_logo.jpg", meal_price=600, meal_type="Hamburger", restaurant_id=3)
    meal27 = Meal(meal_name="Gyros pizza", meal_description="Paradicsom alap, gyros hús, oliva bogyó, sajt",
                  image_source="/static/images/meal_logo.jpg", meal_price=1300, meal_type="Hamburger", restaurant_id=3)
    meal28 = Meal(meal_name="Csirkés pizza", meal_description="Tejfölös alap, csirkemell, sajt, paradicsom",
                  image_source="/static/images/meal_logo.jpg", meal_price=1350, meal_type="Köret", restaurant_id=3)
    meal29 = Meal(meal_name="Smoke pizza", meal_description="Paradicsomos alap, tarja, füstöltsajt",
                  image_source="/static/images/meal_logo.jpg", meal_price=1250, meal_type="Pizza", restaurant_id=3)
    meal30 = Meal(meal_name="Coca-cola", meal_description="3,3 dl",
                  image_source="/static/images/meal_logo.jpg", meal_price=250, meal_type="Üdítő", restaurant_id=3)
    meal31 = Meal(meal_name="Sprite", meal_description="3,3 dl",
                  image_source="/static/images/meal_logo.jpg", meal_price=250, meal_type="Üdítő", restaurant_id=3)

    meal32 = Meal(meal_name="Son-go-ku pizza", meal_description="Paradicsom alap, sonka, gomba, kukorica, sajt",
                  image_source="/static/images/meal_logo.jpg", meal_price=700, meal_type="Pizza", restaurant_id=4)
    meal33 = Meal(meal_name="Sonkás pizza", meal_description="Paradicsom alap, sonka, sajt",
                  image_source="/static/images/meal_logo.jpg", meal_price=500, meal_type="Pizza", restaurant_id=4)
    meal34 = Meal(meal_name="Négy sajtos pizza", meal_description="Paradicsom alap, 4 fajta sajt",
                  image_source="/static/images/meal_logo.jpg", meal_price=1100, meal_type="Pizza", restaurant_id=4)
    meal35 = Meal(meal_name="Hamburger", meal_description="12 dkg marhahúspogácsa, zöldségek, buci",
                  image_source="/static/images/meal_logo.jpg", meal_price=600, meal_type="Hamburger", restaurant_id=4)
    meal36 = Meal(meal_name="Gyros pizza", meal_description="Paradicsom alap, gyros hús, oliva bogyó, sajt",
                  image_source="/static/images/meal_logo.jpg", meal_price=1300, meal_type="Hamburger", restaurant_id=4)
    meal37 = Meal(meal_name="Csirkés pizza", meal_description="Tejfölös alap, csirkemell, sajt, paradicsom",
                  image_source="/static/images/meal_logo.jpg", meal_price=1350, meal_type="Köret", restaurant_id=4)
    meal38 = Meal(meal_name="Smoke pizza", meal_description="Paradicsomos alap, tarja, füstöltsajt",
                  image_source="/static/images/meal_logo.jpg", meal_price=1250, meal_type="Pizza", restaurant_id=4)
    meal39 = Meal(meal_name="Coca-cola", meal_description="3,3 dl",
                  image_source="/static/images/meal_logo.jpg", meal_price=250, meal_type="Üdítő", restaurant_id=4)
    meal40 = Meal(meal_name="Sprite", meal_description="3,3 dl",
                  image_source="/static/images/meal_logo.jpg", meal_price=250, meal_type="Üdítő", restaurant_id=4)

    meal41 = Meal(meal_name="Rántott hús", meal_description="Két nagy szelet.",
                  image_source="/static/images/meal_logo.jpg", meal_price=1200, meal_type="Frissensült",
                  restaurant_id=6)
    meal42 = Meal(meal_name="Sült oldalas", meal_description="20 dkg",
                  image_source="/static/images/meal_logo.jpg", meal_price=1100, meal_type="Frissensült",
                  restaurant_id=6)
    meal43 = Meal(meal_name="Sült csülök", meal_description="Pékné módra.",
                  image_source="/static/images/meal_logo.jpg", meal_price=1500, meal_type="Frissensült",
                  restaurant_id=6)
    meal44 = Meal(meal_name="Csülkös bableves", meal_description="Gazdagon.",
                  image_source="/static/images/meal_logo.jpg", meal_price=1200, meal_type="Leves", restaurant_id=6)
    meal45 = Meal(meal_name="Hús leves", meal_description="Marhahúsból, csiga tésztával.",
                  image_source="/static/images/meal_logo.jpg", meal_price=600, meal_type="Leves", restaurant_id=6)
    meal46 = Meal(meal_name="Párolt rizs", meal_description="12 dkg",
                  image_source="/static/images/meal_logo.jpg", meal_price=350, meal_type="Köret", restaurant_id=6)
    meal47 = Meal(meal_name="Sültkrumpli", meal_description="12 dkg",
                  image_source="/static/images/meal_logo.jpg", meal_price=350, meal_type="Köret", restaurant_id=6)
    meal48 = Meal(meal_name="Coca-cola", meal_description="3,3 dl",
                  image_source="/static/images/meal_logo.jpg", meal_price=250, meal_type="Üdítő", restaurant_id=6)
    meal49 = Meal(meal_name="Sprite", meal_description="3,3 dl",
                  image_source="/static/images/meal_logo.jpg", meal_price=200, meal_type="Üdítő", restaurant_id=6)
    meal50 = Meal(meal_name="Rántott sajt", meal_description="Két 8 dkg-os sajt szelettből.",
                  image_source="/static/images/meal_logo.jpg", meal_price=600, meal_type="Frissensült", restaurant_id=6)
    meal51 = Meal(meal_name="Roston csirkemell", meal_description="16 dkg, diétás.",
                  image_source="/static/images/meal_logo.jpg", meal_price=600, meal_type="Frissensült", restaurant_id=6)

    meal52 = Meal(meal_name="Son-go-ku pizza", meal_description="Paradicsom alap, sonka, gomba, kukorica, sajt",
                  image_source="/static/images/meal_logo.jpg", meal_price=1200, meal_type="Pizza", restaurant_id=5)
    meal53 = Meal(meal_name="Sonkás pizza", meal_description="Paradicsom alap, sonka, sajt",
                  image_source="/static/images/meal_logo.jpg", meal_price=1100, meal_type="Pizza", restaurant_id=5)
    meal54 = Meal(meal_name="Sült csülök", meal_description="Pékné módra.",
                  image_source="/static/images/meal_logo.jpg", meal_price=1500, meal_type="Frissensült",
                  restaurant_id=2)
    meal55 = Meal(meal_name="Csülkös bableves", meal_description="Gazdagon.",
                  image_source="/static/images/meal_logo.jpg", meal_price=1200, meal_type="Leves", restaurant_id=5)
    meal56 = Meal(meal_name="Hús leves", meal_description="Marhahúsból, csiga tésztával.",
                  image_source="/static/images/meal_logo.jpg", meal_price=600, meal_type="Leves", restaurant_id=5)
    meal57 = Meal(meal_name="Párolt rizs", meal_description="12 dkg",
                  image_source="/static/images/meal_logo.jpg", meal_price=350, meal_type="Köret", restaurant_id=5)
    meal58 = Meal(meal_name="Sültkrumpli", meal_description="12 dkg",
                  image_source="/static/images/meal_logo.jpg", meal_price=350, meal_type="Köret", restaurant_id=5)
    meal59 = Meal(meal_name="Coca-cola", meal_description="3,3 dl",
                  image_source="/static/images/meal_logo.jpg", meal_price=250, meal_type="Üdítő", restaurant_id=5)
    meal60 = Meal(meal_name="Sprite", meal_description="3,3 dl",
                  image_source="/static/images/meal_logo.jpg", meal_price=200, meal_type="Üdítő", restaurant_id=5)
    meal61 = Meal(meal_name="Rántott sajt", meal_description="Két 8 dkg-os sajt szelettből.",
                  image_source="/static/images/meal_logo.jpg", meal_price=600, meal_type="Frissensült", restaurant_id=5)
    meal62 = Meal(meal_name="Roston csirkemell", meal_description="16 dkg, diétás.",
                  image_source="/static/images/meal_logo.jpg", meal_price=600, meal_type="Frissensült", restaurant_id=5)

    db.session.add(meal1)
    db.session.add(meal2)
    db.session.add(meal3)
    db.session.add(meal4)
    db.session.add(meal5)
    db.session.add(meal6)
    db.session.add(meal7)
    db.session.add(meal8)
    db.session.add(meal9)
    db.session.add(meal10)
    db.session.add(meal11)
    db.session.add(meal12)
    db.session.add(meal13)
    db.session.add(meal14)
    db.session.add(meal15)
    db.session.add(meal16)
    db.session.add(meal17)
    db.session.add(meal18)
    db.session.add(meal19)
    db.session.add(meal20)
    db.session.add(meal21)
    db.session.add(meal22)
    db.session.add(meal23)
    db.session.add(meal24)
    db.session.add(meal25)
    db.session.add(meal26)
    db.session.add(meal27)
    db.session.add(meal28)
    db.session.add(meal29)
    db.session.add(meal30)
    db.session.add(meal31)
    db.session.add(meal32)
    db.session.add(meal33)
    db.session.add(meal34)
    db.session.add(meal35)
    db.session.add(meal36)
    db.session.add(meal37)
    db.session.add(meal38)
    db.session.add(meal39)
    db.session.add(meal40)
    db.session.add(meal41)
    db.session.add(meal42)
    db.session.add(meal43)
    db.session.add(meal44)
    db.session.add(meal45)
    db.session.add(meal46)
    db.session.add(meal47)
    db.session.add(meal48)
    db.session.add(meal49)
    db.session.add(meal50)
    db.session.add(meal51)
    db.session.add(meal52)
    db.session.add(meal53)
    db.session.add(meal54)
    db.session.add(meal55)
    db.session.add(meal56)
    db.session.add(meal57)
    db.session.add(meal58)
    db.session.add(meal59)
    db.session.add(meal60)
    db.session.add(meal61)
    db.session.add(meal62)

    db.session.commit()

    payment1 = PaymentTable(cash=1, creditcard=1, szep_card=1, erzsebet_voucher=1, restaurant_id=1)
    payment2 = PaymentTable(cash=1, creditcard=1, szep_card=1, erzsebet_voucher=1, restaurant_id=2)
    payment3 = PaymentTable(cash=1, creditcard=1, szep_card=1, erzsebet_voucher=1, restaurant_id=3)
    payment4 = PaymentTable(cash=1, creditcard=1, szep_card=1, erzsebet_voucher=0, restaurant_id=4)
    payment5 = PaymentTable(cash=1, creditcard=1, szep_card=1, erzsebet_voucher=0, restaurant_id=5)
    payment6 = PaymentTable(cash=1, creditcard=1, szep_card=1, erzsebet_voucher=0, restaurant_id=6)

    db.session.add(payment1)
    db.session.add(payment2)
    db.session.add(payment3)
    db.session.add(payment4)
    db.session.add(payment5)
    db.session.add(payment6)
    db.session.commit()

    order1 = Order(order_date="2017-12-08 07:28:24", order_price="1200", user_id=4, restaurant_id=1,
                   payment_type="Készpénz")
    order2 = Order(order_date="2017-12-08 08:28:24", order_price="1600", user_id=4, restaurant_id=1,
                   payment_type="Készpénz")
    order3 = Order(order_date="2017-12-08 08:28:24", order_price="2200", user_id=6, restaurant_id=1,
                   payment_type="Készpénz")
    order4 = Order(order_date="2017-12-08 09:28:24", order_price="1000", user_id=5, restaurant_id=1,
                   payment_type="Készpénz")
    order5 = Order(order_date="2017-12-08 10:28:24", order_price="1200", user_id=4, restaurant_id=1,
                   payment_type="Készpénz")
    order6 = Order(order_date="2017-12-08 10:28:24", order_price="3500", user_id=6, restaurant_id=1,
                   payment_type="Készpénz")
    order7 = Order(order_date="2017-12-08 11:28:24", order_price="4600", user_id=5, restaurant_id=1,
                   payment_type="Készpénz")
    order8 = Order(order_date="2017-12-08 11:28:24", order_price="1200", user_id=4, restaurant_id=1,
                   payment_type="Készpénz")
    order9 = Order(order_date="2017-12-08 11:28:24", order_price="1000", user_id=6, restaurant_id=1,
                   payment_type="Készpénz")
    order10 = Order(order_date="2017-12-08 12:28:24", order_price="1150", user_id=4, restaurant_id=1,
                    payment_type="Készpénz")
    order11 = Order(order_date="2017-12-08 12:28:24", order_price="1800", user_id=5, restaurant_id=1,
                    payment_type="Készpénz")
    order12 = Order(order_date="2017-12-08 12:28:24", order_price="2300", user_id=4, restaurant_id=1,
                    payment_type="Bankkártya")

    order13 = Order(order_date="2017-12-08 12:28:24", order_price="1200", user_id=4, restaurant_id=1,
                    payment_type="Készpénz")
    order14 = Order(order_date="2017-12-08 13:28:24", order_price="1600", user_id=4, restaurant_id=1,
                    payment_type="Készpénz")
    order15 = Order(order_date="2017-12-08 13:28:24", order_price="2200", user_id=6, restaurant_id=1,
                    payment_type="Készpénz")
    order16 = Order(order_date="2017-12-08 13:28:24", order_price="1000", user_id=5, restaurant_id=1,
                    payment_type="Bankkártya")
    order17 = Order(order_date="2017-12-08 14:28:24", order_price="1200", user_id=4, restaurant_id=1,
                    payment_type="Bankkártya")
    order18 = Order(order_date="2017-12-08 15:28:24", order_price="3500", user_id=6, restaurant_id=1,
                    payment_type="Bankkártya")
    order19 = Order(order_date="2017-12-08 16:28:24", order_price="4600", user_id=5, restaurant_id=1,
                    payment_type="Bankkártya")
    order20 = Order(order_date="2017-12-08 17:28:24", order_price="1200", user_id=4, restaurant_id=1,
                    payment_type="Bankkártya")
    order21 = Order(order_date="2017-12-08 17:28:24", order_price="1000", user_id=6, restaurant_id=1,
                    payment_type="Bankkártya")
    order22 = Order(order_date="2017-12-08 18:28:24", order_price="1150", user_id=4, restaurant_id=1,
                    payment_type="SZÉP kártya")
    order23 = Order(order_date="2017-12-08 18:28:24", order_price="1800", user_id=5, restaurant_id=1,
                    payment_type="SZÉP kártya")
    order24 = Order(order_date="2017-12-08 18:28:24", order_price="2300", user_id=4, restaurant_id=1,
                    payment_type="Bankkártya")

    db.session.add(order1)
    db.session.add(order2)
    db.session.add(order3)
    db.session.add(order4)
    db.session.add(order5)
    db.session.add(order6)
    db.session.add(order7)
    db.session.add(order8)
    db.session.add(order9)
    db.session.add(order10)
    db.session.add(order11)
    db.session.add(order12)
    db.session.add(order13)
    db.session.add(order14)
    db.session.add(order15)
    db.session.add(order16)
    db.session.add(order17)
    db.session.add(order18)
    db.session.add(order19)
    db.session.add(order20)
    db.session.add(order21)
    db.session.add(order22)
    db.session.add(order23)
    db.session.add(order24)
    db.session.commit()

    order_meals1 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=1, meal_id=1)
    order_meals2 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=1, meal_id=2)
    order_meals3 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=1, meal_id=5)
    order_meals4 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=2, meal_id=7)
    order_meals5 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=3, meal_id=1)
    order_meals6 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=3, meal_id=10)
    order_meals7 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=3, meal_id=11)
    order_meals8 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=4, meal_id=2)
    order_meals9 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=4, meal_id=8)
    order_meals10 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=5, meal_id=9)
    order_meals11 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=6, meal_id=11)
    order_meals12 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=6, meal_id=2)
    order_meals13 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=6, meal_id=1)

    order_meals14 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=7, meal_id=2)
    order_meals15 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=8, meal_id=5)
    order_meals16 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=8, meal_id=7)
    order_meals17 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=9, meal_id=1)
    order_meals18 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=10, meal_id=10)
    order_meals19 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=10, meal_id=11)
    order_meals20 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=10, meal_id=2)
    order_meals21= Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=11, meal_id=8)
    order_meals22 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=11, meal_id=9)
    order_meals23 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=12, meal_id=11)
    order_meals24 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=12, meal_id=2)
    order_meals25 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=13, meal_id=1)

    order_meals26 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=14, meal_id=2)
    order_meals27 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=14, meal_id=5)
    order_meals28 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=14, meal_id=7)
    order_meals29 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=15, meal_id=1)
    order_meals30 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=16, meal_id=10)
    order_meals31 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=16, meal_id=11)
    order_meals32 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=16, meal_id=2)
    order_meals33 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=17, meal_id=8)
    order_meals34 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=17, meal_id=9)
    order_meals35 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=18, meal_id=11)
    order_meals36 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=18, meal_id=2)
    order_meals37 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=19, meal_id=1)

    order_meals38 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=20, meal_id=2)
    order_meals39 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=20, meal_id=5)
    order_meals40 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=21, meal_id=7)
    order_meals41 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=21, meal_id=1)
    order_meals42 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=21, meal_id=10)
    order_meals43 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=21, meal_id=11)
    order_meals44 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=22, meal_id=2)
    order_meals45 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=22, meal_id=8)
    order_meals46 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=23, meal_id=9)
    order_meals47 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=23, meal_id=11)
    order_meals48 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=23, meal_id=2)
    order_meals49 = Order_meals(order_meals_quantity=1, order_meals_price=600, order_id=24, meal_id=1)

    db.session.add(order_meals1)
    db.session.add(order_meals2)
    db.session.add(order_meals3)
    db.session.add(order_meals4)
    db.session.add(order_meals5)
    db.session.add(order_meals6)
    db.session.add(order_meals7)
    db.session.add(order_meals8)
    db.session.add(order_meals9)
    db.session.add(order_meals10)
    db.session.add(order_meals11)
    db.session.add(order_meals12)
    db.session.add(order_meals13)
    db.session.add(order_meals14)
    db.session.add(order_meals15)
    db.session.add(order_meals16)
    db.session.add(order_meals17)
    db.session.add(order_meals18)
    db.session.add(order_meals19)
    db.session.add(order_meals20)
    db.session.add(order_meals21)
    db.session.add(order_meals22)
    db.session.add(order_meals23)
    db.session.add(order_meals24)
    db.session.add(order_meals25)
    db.session.add(order_meals26)
    db.session.add(order_meals27)
    db.session.add(order_meals28)
    db.session.add(order_meals29)
    db.session.add(order_meals30)
    db.session.add(order_meals31)
    db.session.add(order_meals32)
    db.session.add(order_meals33)
    db.session.add(order_meals34)
    db.session.add(order_meals35)
    db.session.add(order_meals36)
    db.session.add(order_meals37)
    db.session.add(order_meals38)
    db.session.add(order_meals39)
    db.session.add(order_meals40)
    db.session.add(order_meals41)
    db.session.add(order_meals42)
    db.session.add(order_meals43)
    db.session.add(order_meals44)
    db.session.add(order_meals45)
    db.session.add(order_meals46)
    db.session.add(order_meals47)
    db.session.add(order_meals48)
    db.session.add(order_meals49)

    db.session.commit()

    print("Ready")
