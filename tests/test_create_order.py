import json
import allure
import pytest
import requests
from data import Orders
from handle import Handle
from urls import Urls

class TestCreateOrder:
    
    @pytest.mark.parametrize('color_data', [{"color": ["BLACK"]}, {"color": ["GREY"]}, {"color": [""]}, {"color": ["BLACK", "GREY"]}])
    @allure.title('Создание заказа')
    def test_create_order(self, color_data, delete_order):
        order_data = Orders.new_order_data() | color_data
        order_data = json.dumps(order_data)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(f'{Urls.SCOOTER}{Handle.CREATE_ORDER}', data=order_data, headers=headers)
        delete_order.append(response.json()['track'])

        assert response.status_code == 201
        assert 'track' in response.json()

    
