from data import generate_data_new_courier
from urls import Urls
from handle import Handle
import requests
import allure

class TestCreatCourier():

    @allure.title('Создание курьера')
    def test_create_courier(self):
        payload = generate_data_new_courier()
        response = requests.post(f'{Urls.SCOOTER}{Handle.CREATE_COURIER}', data=payload)
        assert response.text == '{"ok":true}'
        assert response.status_code == 201

    @allure.title('Нельзя создать двух курьеров с одинаковыми логинами')
    def test_create_courier_the_same_data(self):
        payload = generate_data_new_courier()
        response = requests.post(f'{Urls.SCOOTER}{Handle.CREATE_COURIER}', data=payload)
        response_2 = requests.post(f'{Urls.SCOOTER}{Handle.CREATE_COURIER}', data=payload)

        assert response_2.status_code == 409
        assert 'Этот логин уже используется' in response_2.text

    @allure.title('Нельзя создать курьера без логина')
    def test_create_courier_without_login(self):
        payload = generate_data_new_courier()
        del payload['login']
        response = requests.post(f'{Urls.SCOOTER}{Handle.CREATE_COURIER}', data=payload)

        assert response.status_code == 400
        assert 'Недостаточно данных для создания учетной записи' in response.text

    @allure.title('Нельзя создать курьера без пароля')
    def test_create_courier_without_password(self):
        payload = generate_data_new_courier()
        del payload['password']
        response = requests.post(f'{Urls.SCOOTER}{Handle.CREATE_COURIER}', data=payload)

        assert response.status_code == 400
        assert 'Недостаточно данных для создания учетной записи' in response.text
