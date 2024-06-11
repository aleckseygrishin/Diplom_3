import allure
from helper import Helper
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage


class TestOrderFeed:
    @allure.title('Проверка отображение заказа пользователя из истории в ленте')
    @allure.description('Ожидаем: заказ присутствует')
    def test_order_is_visible_in_history_order_user(self, driver, create_and_delete_user, user_data_registration):
        order = FeedPage(driver, user_data_registration)
        main_page = MainPage(driver)
        personal_account = PersonalAccountPage(driver)
        order.login()
        main_page.add_bread_ingredient()
        main_page.click_on_button_create_order()
        main_page.click_on_close_button_finish_order()
        main_page.click_on_lk_button()
        personal_account.click_on_history_order()
        id_order = order.get_text_order_id_locators()
        main_page.click_on_order_feed_button()
        paragraph_locator = Helper.get_locators_with_custom_text(id_order)
        checking = order.check_is_displayed(paragraph_locator)

        assert checking

    @allure.title('Проверка прибавления счетчика за всё время, при создании заказа')
    @allure.description('Ожидаем: счётчик прибавился')
    def test_order_count_all_time_count_plus_where_order_create(self, driver, create_and_delete_user,
                                                                user_data_registration):
        order = FeedPage(driver, user_data_registration)
        main_page = MainPage(driver)
        order.login()
        main_page.click_on_order_feed_button()
        count = order.get_text_done_order_all_time()
        main_page.click_on_button_constructor()
        main_page.add_bread_ingredient()
        main_page.add_bread_ingredient()
        main_page.click_on_button_create_order()
        main_page.click_on_close_button_finish_order()
        main_page.click_on_order_feed_button()
        count_plus = order.get_text_done_order_all_time()

        assert int(count_plus) - int(count) == 1

    @allure.title('Проверка прибавления счетчика за сегодня, при создании заказа')
    @allure.description('Ожидаем: счётчик прибавился')
    def test_order_count_today_count_plus_where_order_create(self, driver, create_and_delete_user,
                                                             user_data_registration):
        order = FeedPage(driver, user_data_registration)
        main_page = MainPage(driver)
        order.login()
        main_page.click_on_order_feed_button()
        count = order.get_text_done_order_today()
        main_page.click_on_button_constructor()
        main_page.add_bread_ingredient()
        main_page.add_bread_ingredient()
        main_page.click_on_button_create_order()
        main_page.click_on_close_button_finish_order()
        main_page.click_on_order_feed_button()
        count_plus = order.get_text_done_order_today()

        assert int(count_plus) - int(count) == 1

    @allure.title('Проверка отображения заказа в Ленте заказов в графе - В работе')
    @allure.description('Ожидаем: заказ отображается')
    def test_order_in_work_id_located_in_work(self, driver, create_and_delete_user, user_data_registration):
        order = FeedPage(driver, user_data_registration)
        main_page = MainPage(driver)
        order.login()
        main_page.add_souse_ingredient()
        main_page.add_bread_ingredient()
        main_page.click_on_button_create_order()
        order.wait_visible_modal_window_order_success()
        order_id = order.get_text_order_id_in_window_order()
        main_page.click_on_close_button_finish_order()
        main_page.click_on_order_feed_button()
        locator = Helper.get_li_locators_with_custom_text(order_id)

        assert order.check_is_displayed(locator)

    @allure.title('Проверка отображения окна заказа')
    @allure.description('Ожидаем: окно заказа открывается')
    def test_open_order_window_is_visible(self, driver, create_and_delete_user, user_data_registration):
        order = FeedPage(driver, user_data_registration)
        main_page = MainPage(driver)
        order.login()
        main_page.add_souse_ingredient()
        main_page.add_bread_ingredient()
        main_page.click_on_button_create_order()
        order.wait_visible_modal_window_order_success()
        order_id = order.get_text_order_id_in_window_order()
        main_page.click_on_close_button_finish_order()
        main_page.click_on_order_feed_button()
        locator = Helper.get_p_locator_on_feed_page(order_id)
        # Используется из BasePage, так как точный локатор до создания заказа неизвестен
        order.click_on_button_wait_of_visible(locator)
        locator_modal_window = Helper.get_div_locator_modal_window_order(order_id)

        assert order.check_is_displayed(locator_modal_window)
