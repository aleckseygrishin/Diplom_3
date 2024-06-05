from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from urls import Urls


class LoginPage(BasePage):
    def click_on_password_recovery(self):
        self.click_on_button_clickable(LoginPageLocators.REMEMBER_PASSWORD)

    def open_login_page_on_url(self):
        self.open_page_on_url(Urls.LOGIN_PAGE_URL)
