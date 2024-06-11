import allure
from faker import Faker


class HelperApi:
    @staticmethod
    @allure.step('Создаем данные для регистрации пользователя')
    def random_user():
        faker = Faker()
        return {
            "email": faker.email(),
            "password": faker.password(),
            "name": faker.name()
        }

    @staticmethod
    @allure.step('Вызываем метод получения accessToken из запроса')
    def get_access_token(response):
        access_token = response.json()["accessToken"]
        return access_token
