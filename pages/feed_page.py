from locators.base_page_locators import BasePageLocators
from locators.feed_page_locators import FeedPageLocators
from locators.main_page_locators import MainPageLocators
from locators.personal_account_page_locators import PersonalAccountPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):
    def create_order_and_close_window(self):
        self.add_bread_ingredient()
        self.click_on_button_clickable(MainPageLocators.BUTTON_CREATE_ORDER)
        self.click_on_button_wait_of_visible(MainPageLocators.CLOSE_BUTTON_FINISH_ORDER)

    def switch_to_order_history(self):
        self.click_on_button_wait_of_visible(PersonalAccountPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.click_on_button_wait_of_visible(PersonalAccountPageLocators.HISTORY_ORDER_BUTTON)

    def add_souse_ingredient(self):
        self.add_ingredient_drag_and_drop(FeedPageLocators.SOUSE_FIRST, BasePageLocators.SECTION_DROP_INGREDIENT)
        self.add_ingredient_drag_and_drop(FeedPageLocators.SOUSE_SECOND, BasePageLocators.SECTION_DROP_INGREDIENT)

    def wait_visible_modal_window_order_success(self):
        self.wait_presents_element_located(FeedPageLocators.MODAL_WINDOW_ORDER_SUCCESS)
