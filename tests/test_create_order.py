import pytest
import requests
import data
from methods.order_methods import OrderMethods
import allure

class TestCreateOrder:
    @allure.title('Проверка создания заказа с выбором цвета BLACK, GREY, оба цвета или без выбора цвета')
    @pytest.mark.parametrize("color, expected_status, should_have_track", [
        ({"color": ["BLACK"]}, 201, True),  # Один цвет
        ({"color": ["GREY"]}, 201, True),  # Один цвет
        ({"color": ["BLACK", "GREY"]}, 201, True),  # Оба цвета
        ({}, 201, True)  # Без указания цвета
    ])
    def test_create_order(self, color, expected_status, should_have_track):
        # Подготовка тела запроса
        order_body = {
            **data.DataForCreateOrder.CREATE_ORDER_BODY,
            **color  # Добавляем цвет в тело запроса
        }
        # Отправка запроса на создание заказа
        response = OrderMethods.create_order(order_body)
        # Проверка статуса ответа
        assert response.status_code == expected_status
        response_json = response.json()
        assert "track" in response_json
