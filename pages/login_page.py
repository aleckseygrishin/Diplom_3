from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from urls import Urls


class LoginPage(BasePage):
    def click_on_password_recovery(self):
        self.click_on_button_wait_of_visible(LoginPageLocators.REMEMBER_PASSWORD)

    def open_login_page_on_url(self):
        self.open_page_on_url(Urls.LOGIN_PAGE_URL)

    def send_email_filed(self, argument):
        self.set_field_argument(LoginPageLocators.REMEMBER_PASSWORD_INPUT_EMAIL, argument)

    def click_on_button_recover(self):
        self.click_on_button_wait_of_visible(LoginPageLocators.BUTTON_RECOVER)

    def click_on_eye_button(self):
        self.click_on_button_wait_of_visible(LoginPageLocators.EYE_BUTTON)

    def get_type_password_field(self):
        return self.get_attribute_element(LoginPageLocators.PASSWORD_FIELD_REMEMBER, "type")

    def include_class_name_in_element(self):
        return self.get_attribute_element(LoginPageLocators.PASSWORD_FIELD_DIV, "class")
