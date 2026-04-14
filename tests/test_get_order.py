import pytest
import allure
from methods.order_methods import OrderMethods

class TestGetOrders:
    @allure.title('Проверка списка заказов')
    def test_orders_list_basic(self):
        response = OrderMethods.get_orders_list()
        assert response.status_code == 200
        orders = response.json().get('orders', [])
        assert isinstance(orders, list), "Должен возвращаться список заказов"
