import pytest
import requests
from urls import Urls
from handle import Handle
from helpers import generate_data_new_courier


@pytest.fixture
def payload():
    payload = generate_data_new_courier()
          
    yield payload

    login_payload = {
        "login": payload["login"],
        "password": payload["password"]
    }
    login_response = requests.post(f'{Urls.SCOOTER}{Handle.LOGIN_COURIER}', data=login_payload)

    if login_response.status_code == 200:
        courier_id = login_response.json().get("id")
        requests.delete(f'{Urls.SCOOTER}{Handle.DELETE_COURIER}/{courier_id}')

@pytest.fixture(scope='class')
def payload_reg_courier():
    payload = generate_data_new_courier()
    response = requests.post(f'{Urls.SCOOTER}{Handle.CREATE_COURIER}', data=payload)
    
    yield payload

    login_payload = {
            "login": payload["login"],
            "password": payload["password"]
        }
    login_response = requests.post(f'{Urls.SCOOTER}{Handle.LOGIN_COURIER}', data=login_payload)
    
    if login_response.status_code == 200:
        id = login_response.json().get("id")
        requests.delete(f'{Urls.SCOOTER}{Handle.DELETE_COURIER}/{id}')
    

@pytest.fixture
def delete_order():
    tracks_to_clean = []
    yield tracks_to_clean

    for track_id in tracks_to_clean:
        requests.put(
                f'{Urls.SCOOTER}{Handle.CANCEL_ORDER}', 
                params={"track": track_id}, 
            )

    

