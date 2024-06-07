import allure
from pages.main_page import MainPage
from urls import Urls


class TestMainPage:
    @allure.title('Переход по кнопке Конструктор')
    @allure.description('Ожидаем: страница Конструктор отображается')
    def test_switch_to_constructor_button_current_url_correct(self, driver):
        switch = MainPage(driver)
        switch.open_page_on_url(Urls.LOGIN_PAGE_URL)
        switch.click_on_button_constructor()

        assert switch.get_current_url(Urls.BASE_URL) == Urls.BASE_URL

    @allure.title('Переход по кнопке Лента заказов')
    @allure.description('Ожидаем: страница Лента заказов отображается')
    def test_switch_to_order_feed_current_url_correct(self, driver):
        switch = MainPage(driver)
        switch.open_page_on_url(Urls.LOGIN_PAGE_URL)
        switch.click_on_order_feed_button()

        assert switch.get_current_url(Urls.ORDER_FEED_URL) == Urls.ORDER_FEED_URL

    @allure.title('Выбор ингредиента')
    @allure.description('Ожидаем: открылось окно со свойствами ингредиента')
    def test_choose_ingredient_window_is_visible(self, driver):
        switch = MainPage(driver)
        switch.open_page_on_url(Urls.BASE_URL)
        switch.click_on_ingredient()

        assert switch.check_ingredient_window_is_visible()

    @allure.title('Закрытие окна свойств Ингредиента')
    @allure.description('Ожидаем: окно закрылось')
    def test_close_window_ingredient_window_is_not_visible(self, driver):
        switch = MainPage(driver)
        switch.open_page_on_url(Urls.BASE_URL)
        switch.click_on_ingredient()
        switch.click_on_close_button()
        assert switch.check_window_ingredient_is_invisible()

    @allure.title('Добавление ингредиента')
    @allure.description('Ожидаем: счетчик ингредиента увеличился на 2')
    def test_add_ingredient_count_plus_number_two(self, driver):
        switch = MainPage(driver)
        switch.open_page_on_url(Urls.BASE_URL)
        switch.add_bread_ingredient()

        assert switch.check_count_ingredient() == '2'

    @allure.title('Проверка возможности сделать заказ авторизованному пользователю')
    @allure.description('Ожидаем: пользователь может создать заказ')
    def test_auth_user_may_create_order_window_finish_create_order_is_visible(self, driver, create_and_delete_user,
                                                                              user_data_registration):
        switch = MainPage(driver, user_data_registration)
        switch.login()
        switch.add_bread_ingredient()
        switch.click_on_button_create_order()

        assert switch.check_window_finish_create_order()
