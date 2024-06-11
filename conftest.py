import allure
import pytest
from selenium import webdriver
from create_user_api.burger_api import BurgerApi
from create_user_api.helper_api import HelperApi


# Тесты на Firefox работают, через раз, выполнение только на Chrome
@pytest.fixture(scope='function')
def driver():
    browser = webdriver.Chrome()

    yield browser

    browser.quit()


@allure.step('Вызываем фикстуру (создание json для регистрации пользователя)')
@pytest.fixture(scope='function')
def user_data_registration():
    return HelperApi.random_user()


@allure.step('Вызываем фикстуру (создание и удаление по окончанию теста пользователя)')
@pytest.fixture(scope='function')
def create_and_delete_user(user_data_registration):
    create = BurgerApi.create_user(user_data_registration)
    token = HelperApi.get_access_token(create)

    yield create

    BurgerApi.delete_user(token)
