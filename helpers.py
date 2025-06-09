import requests
from faker import Faker
from urls import Url

# Инициализация Faker
fake = Faker()

class UserAPI:
    @staticmethod
    def generate_random_user():
        # Генерируем случайные данные пользователя
        return {
            'email': fake.email(),
            'password': fake.password(),
            'name': fake.name()
        }


    @staticmethod
    def register(user_data):
         # Регистрируем пользователя с предоставленными данными
        response = requests.post(Url.BASE_URL + Url.USER_REGISTRATION_URL, json=user_data)
        return response


    @staticmethod
    def delete_user(access_token):
        # Удаляет пользователя

        headers  = {'Authorization': f'Bearer {access_token}'}

        # Выполняем DELETE-запрос с передачей токена в заголовке
        requests.delete(Url.BASE_URL + Url.USER_DATA_URL, headers=headers)


class OrderAPI:
    @staticmethod
    def create_order(registered_user, ingredients):
        # Создаем заказ с указанными ингредиентами
        user_data = registered_user
        headers = {
            'Authorization': user_data['access_token'],
            'Content-Type': 'application/json'
        }

        return requests.post(
            Url.BASE_URL + Url.ORDER_CREATION_POST_URL,
            json={"ingredients": ingredients},
            headers=headers
        )



"""
    @staticmethod
    def get_ingredients():
        # Получаем список ингредиентов
        return requests.get(Url.BASE_URL + Url.INGREDIENTS_GET_URL)
    

    @staticmethod
    def get_access_token(user_data):
        # Авторизовываем пользователя с предоставленными данными
        response = requests.post(Url.BASE_URL + Url.USER_LOGIN_URL, json=user_data)
        return response.json()['accessToken']
"""