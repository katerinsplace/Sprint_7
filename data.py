from faker import Faker

def generate_data_new_courier():
    fake = Faker(locale="ru_RU")
    login = fake.user_name()
    password = fake.password()
    firstName = fake.name()
    payload = {
        "login": login,
        "password": password,
        "name": firstName
    }
    return payload

class Orders:
    def new_order_data(color=[""]):
        data_order = {
            "firstName": "Elizabeth",
            "lastName": "Taylor",
            "address": "London, Piccadilly St. 44",
            "metroStation": "Piccadilly Circus",
            "phone": "+79991234567",
            "rentTime": 4,
            "deliveryDate": "2026-08-25",
            "comment": "test",
            "color": color
            }
        return data_order
        
        