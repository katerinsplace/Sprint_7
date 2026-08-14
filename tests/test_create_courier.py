from urls import Urls
from handle import Handle
from data import Responses
import requests
import allure

class TestCreatCourier():

    @allure.title('Создание курьера')
    def test_create_courier(self, payload):
        response = requests.post(f'{Urls.SCOOTER}{Handle.CREATE_COURIER}', data=payload)
            
        assert response.text == '{"ok":true}'
        assert response.status_code == 201

    @allure.title('Нельзя создать двух курьеров с одинаковыми логинами')
    def test_create_courier_the_same_data(self, payload):
        response = requests.post(f'{Urls.SCOOTER}{Handle.CREATE_COURIER}', data=payload)
        response_2 = requests.post(f'{Urls.SCOOTER}{Handle.CREATE_COURIER}', data=payload)

        assert response_2.status_code == 409
        assert Responses.LOGIN_USE in response_2.text

    @allure.title('Нельзя создать курьера без логина')
    def test_create_courier_without_login(self, payload):
        data_login = {
                "password": payload["password"],
                "name": payload["name"]
            }
        response = requests.post(f'{Urls.SCOOTER}{Handle.CREATE_COURIER}', data=data_login)

        assert response.status_code == 400
        assert Responses.NOT_ENOUGH_DATA_REG in response.text

    @allure.title('Нельзя создать курьера без пароля')
    def test_create_courier_without_password(self, payload):
        data_login = {
                        "login": payload["login"],
                        "name": payload["name"]
                    }
        response = requests.post(f'{Urls.SCOOTER}{Handle.CREATE_COURIER}', data=data_login)

        assert response.status_code == 400
        assert Responses.NOT_ENOUGH_DATA_REG in response.text
