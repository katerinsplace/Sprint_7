import json
import allure
import pytest
import requests
from data import Orders
from handle import Handle
from urls import Urls

class TestCreateOrder:
    def setup_method(self):
        self.tracks_to_clean = []

    @pytest.mark.parametrize('color_data', [{"color": ["BLACK"]}, {"color": ["GREY"]}, {"color": [""]}, {"color": ["BLACK", "GREY"]}])
    @allure.title('Создание заказа')
    def test_create_order(self, color_data):
        order_data = Orders.new_order_data() | color_data
        order_data = json.dumps(order_data)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(f'{Urls.SCOOTER}{Handle.CREATE_ORDER}', data=order_data, headers=headers)
        self.tracks_to_clean.append(response.json()['track'])

        assert response.status_code == 201
        assert 'track' in response.json()

    def teardown_method(self):
        for track_id in self.tracks_to_clean:
            requests.put(
                f'{Urls.SCOOTER}{Handle.CANCEL_ORDER}', 
                params={"track": track_id}, 
            )

    
