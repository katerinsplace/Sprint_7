import allure
import requests
import pytest
from handle import Handle
from urls import Urls
from data import generate_data_new_courier


class TestLoginCourier:
    payload = generate_data_new_courier()
    ids = []

    @classmethod
    def setup_class(cls):
        response = requests.post(f'{Urls.SCOOTER}{Handle.CREATE_COURIER}', data=cls.payload)

    @allure.title("Успешная авторизация курьера")
    def test_login_courier(self):
        data_login = {
            'login': self.payload['login'], 
            'password': self.payload['password']
        }
        response = requests.post(f'{Urls.SCOOTER}{Handle.LOGIN_COURIER}', data=data_login)
        
        assert 'id' in response.json()
        TestLoginCourier.ids.append(response.json()['id'])
        assert response.status_code == 200

    @allure.title("Попытка авторизации без логина")  
    def test_login_without_login(self):
        data_login = {'login': '', 'password': self.payload['password']}
        response = requests.post(f'{Urls.SCOOTER}{Handle.LOGIN_COURIER}', data=data_login)

        assert response.status_code == 400
        assert 'Недостаточно данных для входа' in response.text    

    @allure.title("Попытка авторизации без пароля") 
    def test_login_without_password(self):
        data_login = {'login': self.payload['login'], 'password': ''}
        response = requests.post(f'{Urls.SCOOTER}{Handle.LOGIN_COURIER}', data=data_login)

        assert response.status_code == 400
        assert 'Недостаточно данных для входа' in response.text 

    @allure.title("Ошибка авторизации при вводе неверного логина или пароля")
    def test_login_courier_negative(self):
        new_payload = generate_data_new_courier()
        del new_payload["name"]
        response = requests.post(f'{Urls.SCOOTER}{Handle.LOGIN_COURIER}', data=new_payload)
        
        assert 'Учетная запись не найдена' in response.text
        assert response.status_code == 404

    @classmethod
    def teardown_class(cls):
        for id in cls.ids:
            requests.delete(f'{Urls.SCOOTER}{Handle.DELETE_COURIER}/{id}')
            