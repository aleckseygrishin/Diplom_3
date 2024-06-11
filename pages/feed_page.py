import allure
from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):
    @allure.step('Ожидание, пока элемент модальное окно не появится')
    def wait_visible_modal_window_order_success(self):
        self.wait_presents_element_located(FeedPageLocators.MODAL_WINDOW_ORDER_SUCCESS)

    @allure.step('Получаем текст элемента ORDER_ID_LOCATORS')
    def get_text_order_id_locators(self):
        return self.get_text_element(FeedPageLocators.ORDER_ID_LOCATORS)

    @allure.step('Получаем текст элемента DONE_ORDER_ALL_TIME')
    def get_text_done_order_all_time(self):
        return self.get_text_element(FeedPageLocators.DONE_ORDER_ALL_TIME)

    @allure.step('Получаем текст элемента DONE_ORDER_TODAY')
    def get_text_done_order_today(self):
        return self.get_text_element(FeedPageLocators.DONE_ORDER_TODAY)

    @allure.step('Получаем текст элемента ORDER_ID_IN_WINDOW_ORDER')
    def get_text_order_id_in_window_order(self):
        return self.get_text_element(FeedPageLocators.ORDER_ID_IN_WINDOW_ORDER)
