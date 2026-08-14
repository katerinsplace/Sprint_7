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