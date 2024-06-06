from pages.personal_account_page import PersonalAccountPage
from urls import Urls


class TestPersonalAccountPage:
    def test_switch_to_personal_account_without_auth_user_current_url_correct(self, driver):
        switch = PersonalAccountPage(driver)
        switch.open_page_on_url(Urls.BASE_URL)
        switch.click_on_personal_account_button()

        assert switch.get_current_url(Urls.LOGIN_PAGE_URL) == Urls.LOGIN_PAGE_URL

    def test_switch_to_personal_account_with_auth_user_current_url_correct(self, driver, create_and_delete_user, user_data_registration):
        switch = PersonalAccountPage(driver=driver, user_data_registration=user_data_registration)
        switch.login()
        switch.click_on_personal_account_button()

        assert switch.get_current_url(Urls.ACCOUNT_PROFILE_URL) == Urls.ACCOUNT_PROFILE_URL

    def test_switch_to_history_order_current_url_correct(self, driver, create_and_delete_user, user_data_registration):
        switch = PersonalAccountPage(driver=driver, user_data_registration=user_data_registration)
        switch.login()
        switch.click_on_personal_account_button()
        switch.click_on_history_order()

        assert switch.get_current_url(Urls.ORDER_HISTORY_URL) == Urls.ORDER_HISTORY_URL

    def test_exit_from_account_current_url_correct(self, driver, create_and_delete_user, user_data_registration):
        switch = PersonalAccountPage(driver=driver, user_data_registration=user_data_registration)
        switch.login()
        switch.click_on_personal_account_button()
        switch.click_on_exit_button()

        assert switch.get_current_url(Urls.LOGIN_PAGE_URL) == Urls.LOGIN_PAGE_URL
