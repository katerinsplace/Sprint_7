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
        
class Responses:
    LOGIN_USE = 'Этот логин уже используется'
    NOT_ENOUGH_DATA_REG = 'Недостаточно данных для создания учетной записи'
    ACCOUNT_NOT_FOUND = 'Учетная запись не найдена'
    NOT_ENOUGH_DATA_LOGIN = 'Недостаточно данных для входа'
