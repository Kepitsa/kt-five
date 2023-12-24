import allure
import requests
from pydantic import BaseModel, ValidationError

BASE_URL_PETSTORE = 'https://petstore.swagger.io/v2'

class UserData(BaseModel):
    id: int
    username: str
    firstName: str
    lastName: str
    email: str
    phone: str

class OrderData(BaseModel):
    id: int
    petId: int
    quantity: int
    shipDate: str
    status: str

@allure.title("Get User")
def test_get_user():
    user_id = 1
    response = requests.get(f'{BASE_URL_PETSTORE}/user/{user_id}')
    allure.attach("Request URL", response.request.url, allure.attachment_type.TEXT)
    allure.attach("Request Headers", str(response.request.headers), allure.attachment_type.TEXT)
    allure.attach("Request Body", str(response.request.body), allure.attachment_type.TEXT)
    allure.attach("Response Code", str(response.status_code), allure.attachment_type.TEXT)
    assert response.status_code == 200

@allure.title("Create User")
def test_create_user():
    user_data = {
        'id': 1,
        'username': 'BobFr',
        'firstName': 'Bob',
        'lastName': 'Bobino',
        'email': 'Bob@rambler.com',
        'phone': '0000000000'
    }

    try:
        UserData(**user_data)
    except ValidationError as e:
        allure.attach("Validation Error", str(e), allure.attachment_type.TEXT)
        assert False, "User data validation failed"

    response = requests.post(f'{BASE_URL_PETSTORE}/user', json=user_data)
    allure.attach("Request URL", response.request.url, allure.attachment_type.TEXT)
    allure.attach("Request Headers", str(response.request.headers), allure.attachment_type.TEXT)
    allure.attach("Request Body", str(response.request.body), allure.attachment_type.TEXT)
    allure.attach("Response Code", str(response.status_code), allure.attachment_type.TEXT)
    assert response.status_code == 200

@allure.title("Get Order")
def test_get_order():
    order_id = 1
    response = requests.get(f'{BASE_URL_PETSTORE}/store/order/{order_id}')
    allure.attach("Request URL", response.request.url, allure.attachment_type.TEXT)
    allure.attach("Request Headers", str(response.request.headers), allure.attachment_type.TEXT)
    allure.attach("Request Body", str(response.request.body), allure.attachment_type.TEXT)
    allure.attach("Response Code", str(response.status_code), allure.attachment_type.TEXT)
    assert response.status_code == 200

@allure.title("Create Order")
def test_create_order():
    order_data = {
        "id": 1,
        "petId": 1,
        "quantity": 1,
        "shipDate": "2023-12-25T12:00:00Z",
        "status": "placed"
    }

    try:
        OrderData(**order_data)
    except ValidationError as e:
        allure.attach("Validation Error", str(e), allure.attachment_type.TEXT)
        assert False, "Order data validation failed"

    response = requests.post(f'{BASE_URL_PETSTORE}/store/order/{order_id}', json=order_data)
    allure.attach("Request URL", response.request.url, allure.attachment_type.TEXT)
    allure.attach("Request Headers", str(response.request.headers), allure.attachment_type.TEXT)
    allure.attach("Request Body", str(response.request.body), allure.attachment_type.TEXT)
    allure.attach("Response Code", str(response.status_code), allure.attachment_type.TEXT)
    assert response.status_code == 200


if __name__ == "__main__":

    import pytest
    pytest.main(['-s', '-v', '--alluredir', 'allure-results'])
