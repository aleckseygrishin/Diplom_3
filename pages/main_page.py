from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def click_on_button_constructor(self):
        self.click_on_button_wait_of_visible(MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_on_order_feed_button(self):
        self.click_on_button_wait_of_visible(MainPageLocators.ORDER_FEED_BUTTON)

    def click_on_ingredient(self):
        self.click_on_button_wait_of_visible(MainPageLocators.BREAD_INGREDIENT_FIRST)

    def click_on_close_button(self):
        self.click_on_button_wait_of_visible(MainPageLocators.CLOSE_BUTTON)

    def check_ingredient_window_is_visible(self):
        return self.check_is_displayed(MainPageLocators.WINDOW_INGREDIENT)

    def check_window_ingredient_is_invisible(self):
        return self.check_is_not_displayed(MainPageLocators.WINDOW_INGREDIENT)

    def check_window_finish_create_order(self):
        return self.check_is_displayed(MainPageLocators.WINDOW_FINISH_CREATE_ORDER)

    def add_ingredient(self):
        self.add_ingredient_drag_and_drop(source_locator=MainPageLocators.BREAD_INGREDIENT_FIRST,
                                          target_locator=MainPageLocators.SECTION_DROP_INGREDIENT)

    def check_count_ingredient(self):
        return self.get_text_element(MainPageLocators.COUNT_ADD_INGREDIENT)

    def click_on_button_create_order(self):
        self.click_on_button_wait_of_visible(MainPageLocators.BUTTON_CREATE_ORDER)
