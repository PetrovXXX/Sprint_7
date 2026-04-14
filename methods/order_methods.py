import requests
import data

class OrderMethods:
    @staticmethod
    def create_order(body):
        return requests.post(f'{data.Url.BASE_URL}{data.Url.BASE_ORDER_URL}', json=body)

    @staticmethod
    def list_order(body):
        return requests.post(f'{data.Url.BASE_URL}{data.Url.LIST_ORDER_URL}', json=body)

    @staticmethod
    def get_orders_list(limit=5, page=0):
        params = {
            'limit': limit,
            'page': page
        }
        return requests.get(f'{data.Url.BASE_URL}{data.Url.LIST_ORDER_URL}', params=params)