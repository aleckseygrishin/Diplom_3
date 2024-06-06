from locators.personal_account_page_locators import PersonalAccountPageLocators
from pages.base_page import BasePage
from urls import Urls


class PersonalAccountPage(BasePage):
    def click_on_personal_account_button(self):
        self.click_on_button_wait_of_visible(PersonalAccountPageLocators.PERSONAL_ACCOUNT_BUTTON)

    def click_on_history_order(self):
        self.click_on_button_wait_of_visible(PersonalAccountPageLocators.HISTORY_ORDER_BUTTON)

    def click_on_exit_button(self):
        self.click_on_button_wait_of_visible(PersonalAccountPageLocators.EXIT_BUTTON)
