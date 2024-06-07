from selenium.webdriver.common.by import By


class Helper:
    @staticmethod
    def get_locators_with_custom_text(text):
        locator = (By.XPATH, f"//p[text()='{text}']")
        return locator

    @staticmethod
    def get_li_locators_with_custom_text(text):
        locator = (By.XPATH, f"//li[text()='{text}']")
        return locator

    @staticmethod
    def get_p_locator_on_feed_page(text):
        locator = (By.XPATH, f"//p[text()='#0{text}']/parent::div/parent::a")
        return locator

    @staticmethod
    def get_div_locator_modal_window_order(text):
        locator = (By.XPATH, f"//p[text()='{text}']/parent::div/parent::div")
        return locator
