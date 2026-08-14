import allure
import requests
from handle import Handle
from urls import Urls
from data import Responses
from helpers import generate_data_new_courier


class TestLoginCourier:

    @allure.title("Успешная авторизация курьера")
    def test_login_courier(self, payload_reg_courier):
        payload = payload_reg_courier
        data_login = {
            'login': payload['login'], 
            'password': payload['password']
        }
        response = requests.post(f'{Urls.SCOOTER}{Handle.LOGIN_COURIER}', data=data_login)
        
        assert 'id' in response.json()
        assert response.status_code == 200

    @allure.title("Попытка авторизации без логина")  
    def test_login_without_login(self, payload_reg_courier):
        payload = payload_reg_courier
        data_login = {'login': '', 'password': payload['password']}
        response = requests.post(f'{Urls.SCOOTER}{Handle.LOGIN_COURIER}', data=data_login)

        assert response.status_code == 400
        assert Responses.NOT_ENOUGH_DATA_LOGIN in response.text    

    @allure.title("Попытка авторизации без пароля") 
    def test_login_without_password(self, payload_reg_courier):
        payload = payload_reg_courier
        data_login = {'login': payload['login'], 'password': ''}
        response = requests.post(f'{Urls.SCOOTER}{Handle.LOGIN_COURIER}', data=data_login)

        assert response.status_code == 400
        assert Responses.NOT_ENOUGH_DATA_LOGIN in response.text 

    @allure.title("Ошибка авторизации при вводе неверного логина или пароля")
    def test_login_courier_negative(self):
        new_payload = generate_data_new_courier()
        del new_payload["name"]
        response = requests.post(f'{Urls.SCOOTER}{Handle.LOGIN_COURIER}', data=new_payload)
        
        assert Responses.ACCOUNT_NOT_FOUND in response.text
        assert response.status_code == 404
