import allure
from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Нажимаем на кнопку Конструктор')
    def click_on_button_constructor(self):
        self.click_on_button_wait_of_visible(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Нажимаем на кнопку Лента заказов')
    def click_on_order_feed_button(self):
        self.click_on_button_wait_of_visible(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Нажимаем на ингредиент')
    def click_on_ingredient(self):
        self.click_on_button_wait_of_visible(BasePageLocators.BREAD_INGREDIENT_FIRST)

    @allure.step('Нажимаем кнопку "Закрыть" в свойствах ингредиента')
    def click_on_close_button(self):
        self.click_on_button_wait_of_visible(MainPageLocators.CLOSE_BUTTON)

    @allure.step('Проверяем отображения окна')
    def check_ingredient_window_is_visible(self):
        return self.check_is_displayed(MainPageLocators.WINDOW_INGREDIENT)

    @allure.step('Проверяем, что окно ингредиентов не отображается')
    def check_window_ingredient_is_invisible(self):
        return self.check_is_displayed(MainPageLocators.SECTION_OPENED_WINDOW)

    @allure.step('Проверяем, что окно окончания создания заказа отображается')
    def check_window_finish_create_order(self):
        return self.check_is_displayed(MainPageLocators.WINDOW_FINISH_CREATE_ORDER)

    @allure.step('Получаем количество ингредиентов')
    def check_count_ingredient(self):
        return self.get_text_element(MainPageLocators.COUNT_ADD_INGREDIENT)

    @allure.step('Нажимаем на кнопку "Оформить заказ"')
    def click_on_button_create_order(self):
        self.click_on_button_wait_of_visible(MainPageLocators.BUTTON_CREATE_ORDER)
