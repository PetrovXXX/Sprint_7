import pytest

from generators import generate_couriers_body
from methods.courier_methods import CourierMethods


@pytest.fixture
def generate_courier_data():
    courier_body = generate_couriers_body()
    login = courier_body['login']
    password = courier_body['password']
    firstname = courier_body['firstName']
    yield [courier_body, login, password, firstname]
    courier_id = CourierMethods.login_courier(login, password)
    CourierMethods.delete_courier(courier_id)

@pytest.fixture
def generate_courier_login_data():
    # Генерация данных для курьера
    courier_body = generate_couriers_body()
    login = courier_body['login']
    password = courier_body['password']
    firstname = courier_body['firstName']
    # Регистрация курьера
    CourierMethods.create_courier(courier_body)
    # Вход с созданными данными
    response = CourierMethods.login_courier(login, password)
    courier_id = response.json().get('id')  # Получаем ID курьера
    # Возвращаем данные для тестов
    yield [courier_body, login, password, firstname, courier_id]
    # Удаление курьера после завершения теста
    CourierMethods.delete_courier(courier_id)