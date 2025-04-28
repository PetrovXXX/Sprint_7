import allure
from methods.courier_methods import CourierMethods

class TestLoginCourier:
    @allure.title('Проверка успешной авторизации курьера')
    @allure.description('Проверка ответа и тела ответа при успешной авторизации')
    def test_successful_login(self, generate_courier_login_data):
        courier_body, login, password, firstname, courier_id = generate_courier_login_data
        response = CourierMethods.login_courier(login, password)
        assert response.status_code == 200
        assert response.json().get('id') == courier_id

    @allure.title('Проверка попытки входа с неправильным паролем')
    def test_login_with_invalid_password(self, generate_courier_login_data):
        courier_body, login, password, firstname, courier_id = generate_courier_login_data
        invalid_password = "wrong_password"
        response = CourierMethods.login_courier(login, invalid_password)
        assert response.status_code == 404
        assert response.json().get('message') == "Учетная запись не найдена"

    @allure.title('Проверка авторизации без логина')
    @allure.description('Проверка ошибки при отсутствии логина')
    def test_login_without_login_field(self, generate_courier_login_data):
        courier_body, login, password, firstname, courier_id = generate_courier_login_data
        response = CourierMethods.login_courier("", password)
        assert response.status_code == 400
        assert response.json().get('message') == "Недостаточно данных для входа"

    @allure.title('Проверка авторизации без пароля')
    @allure.description('Проверка ошибки при отсутствии пароля')
    def test_login_without_password_field(self, generate_courier_login_data):
        courier_body, login, password, firstname, courier_id = generate_courier_login_data
        response = CourierMethods.login_courier(login, "")
        assert response.status_code == 400
        assert response.json().get('message') == "Недостаточно данных для входа"

    @allure.title('Проверка авторизации несуществующего пользователя')
    @allure.description('Проверка ошибки при авторизации несуществующего курьера')
    def test_login_nonexistent_user(self):
        response = CourierMethods.login_courier("nonexistent_user", "any_password")
        assert response.status_code == 404
        assert response.json().get('message') == "Учетная запись не найдена"
