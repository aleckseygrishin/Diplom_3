import allure
import requests

from urls import Urls


class BurgerApi:
    @staticmethod
    @allure.step('Возвращаем ответ на запрос (регистрация пользователя)')
    def create_user(body):
        response = requests.post(Urls.API_USER_REGISTRATION_URL, json=body)
        return response

    @staticmethod
    @allure.step('Возвращаем ответ на запрос (удаление пользователя)')
    def delete_user(token):
        response = requests.delete(Urls.API_DELETE_OR_PATCH_USER_URL, headers={'Authorization': token})
        return response
