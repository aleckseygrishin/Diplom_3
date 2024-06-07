import allure
from helper import Helper
from locators.feed_page_locators import FeedPageLocators
from locators.main_page_locators import MainPageLocators
from pages.feed_page import FeedPage


class TestOrderFeed:
    @allure.title('Проверка отображение заказа пользователя из истории в ленте')
    @allure.description('Ожидаем: заказ присутствует')
    def test_order_is_visible_in_history_order_user(self, driver, create_and_delete_user, user_data_registration):
        order = FeedPage(driver, user_data_registration)
        order.login()
        order.create_order_and_close_window()
        order.switch_to_order_history()
        id_order = order.get_text_element(FeedPageLocators.ORDER_ID_LOCATORS)
        order.click_on_button_wait_of_visible(MainPageLocators.ORDER_FEED_BUTTON)
        paragraph_locator = Helper.get_locators_with_custom_text(id_order)
        checking = order.check_is_displayed(paragraph_locator)

        assert checking

    @allure.title('Проверка прибавления счетчика за всё время, при создании заказа')
    @allure.description('Ожидаем: счётчик прибавился')
    def test_order_count_all_time_count_plus_where_order_create(self, driver, create_and_delete_user,
                                                                user_data_registration):
        order = FeedPage(driver, user_data_registration)
        order.login()
        order.click_on_button_wait_of_visible(MainPageLocators.ORDER_FEED_BUTTON)
        count = order.get_text_element(FeedPageLocators.DONE_ORDER_ALL_TIME)
        order.click_on_button_wait_of_visible(MainPageLocators.CONSTRUCTOR_BUTTON)
        order.add_bread_ingredient()
        order.create_order_and_close_window()
        order.click_on_button_wait_of_visible(MainPageLocators.ORDER_FEED_BUTTON)
        count_plus = order.get_text_element(FeedPageLocators.DONE_ORDER_ALL_TIME)

        assert int(count_plus) - int(count) == 1

    @allure.title('Проверка прибавления счетчика за сегодня, при создании заказа')
    @allure.description('Ожидаем: счётчик прибавился')
    def test_order_count_today_count_plus_where_order_create(self, driver, create_and_delete_user,
                                                             user_data_registration):
        order = FeedPage(driver, user_data_registration)
        order.login()
        order.click_on_button_wait_of_visible(MainPageLocators.ORDER_FEED_BUTTON)
        count = order.get_text_element(FeedPageLocators.DONE_ORDER_TODAY)
        order.click_on_button_wait_of_visible(MainPageLocators.CONSTRUCTOR_BUTTON)
        order.add_bread_ingredient()
        order.create_order_and_close_window()
        order.click_on_button_wait_of_visible(MainPageLocators.ORDER_FEED_BUTTON)
        count_plus = order.get_text_element(FeedPageLocators.DONE_ORDER_TODAY)

        assert int(count_plus) - int(count) == 1

    @allure.title('Проверка отображения заказа в Ленте заказов в графе - В работе')
    @allure.description('Ожидаем: заказ отображается')
    def test_order_in_work_id_located_in_work(self, driver, create_and_delete_user, user_data_registration):
        order = FeedPage(driver, user_data_registration)
        order.login()
        order.add_souse_ingredient()
        order.add_bread_ingredient()
        order.click_on_button_clickable(MainPageLocators.BUTTON_CREATE_ORDER)
        order.wait_visible_modal_window_order_success()
        order_id = order.get_text_element(FeedPageLocators.ORDER_ID_IN_WINDOW_ORDER)
        order.click_on_button_wait_of_visible(MainPageLocators.CLOSE_BUTTON_FINISH_ORDER)
        order.click_on_button_wait_of_visible(MainPageLocators.ORDER_FEED_BUTTON)
        locator = Helper.get_li_locators_with_custom_text(order_id)

        assert order.check_is_displayed(locator)

    @allure.title('Проверка отображения окна заказа')
    @allure.description('Ожидаем: окно заказа открывается')
    def test_open_order_window_is_visible(self, driver, create_and_delete_user, user_data_registration):
        order = FeedPage(driver, user_data_registration)
        order.login()
        order.add_souse_ingredient()
        order.add_bread_ingredient()
        order.click_on_button_clickable(MainPageLocators.BUTTON_CREATE_ORDER)
        order.wait_visible_modal_window_order_success()
        order_id = order.get_text_element(FeedPageLocators.ORDER_ID_IN_WINDOW_ORDER)
        order.click_on_button_wait_of_visible(MainPageLocators.CLOSE_BUTTON_FINISH_ORDER)
        order.click_on_button_wait_of_visible(MainPageLocators.ORDER_FEED_BUTTON)
        locator = Helper.get_p_locator_on_feed_page(order_id)
        order.click_on_button_wait_of_visible(locator)
        locator_modal_window = Helper.get_div_locator_modal_window_order(order_id)

        assert order.check_is_displayed(locator_modal_window)
