class Url:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    CREAT_COURIER_URL = '/api/v1/courier'
    LOGIN_COURIER_URL = '/api/v1/courier/login'
    BASE_ORDER_URL = '/api/v1/orders'
    LIST_ORDER_URL = '/api/v1/orders'

class DataForCreatCourier:
    CREAT_COURIER_BODY = {
        "login": "ninja",
        "password": "1234",
        "firstName": "saske"
    }

class DataForCreateOrder:
    CREATE_ORDER_BODY = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2025-05-02",
    "comment": "Saske, come back to Konoha"
}

class ListOfOrders:
    LIST_OF_ORDERS_BODY = {
        "id": 4,
        "courierId": None,
        "firstName": "ваыпывп",
        "lastName": "ывпывп",
        "address": "пывпывп",
        "metroStation": "2",
        "phone": "423424234432",
        "rentTime": 4,
        "deliveryDate": "2020-06-21T21:00:00.000Z",
        "track": 400443,
        "color": ["BLACK", "GREY"],
        "comment": "ываимм",
        "createdAt": "2020-06-21T13:21:30.067Z",
        "updatedAt": "2020-06-21T13:21:30.067Z",
        "status": 0
    }