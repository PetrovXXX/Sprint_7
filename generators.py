from faker import Faker
import random

fake = Faker()


def generate_couriers_body():
    # Генерация части логина
    base_login = fake.user_name()  # Используем user_name для генерации логина
    # Генерация 5 случайных цифр от 1 до 5
    random_digits = ''.join(random.choices('12345', k=5))  # Генерируем 5 случайных цифр

    # Формируем окончательный логин
    login = f"{base_login}{random_digits}"

    courier_body = {
        "login": login,  # Используем сгенерированный логин
        "password": fake.password(),  # Генерация пароля
        "firstName": fake.first_name()  # Генерация имени
    }
    return courier_body