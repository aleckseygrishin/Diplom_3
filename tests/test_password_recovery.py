from locators.login_page_locators import LoginPageLocators
from pages.login_page import LoginPage
from urls import Urls


class TestPasswordRecovery:
    def test(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page_on_url()
        login_page.click_on_password_recovery()
