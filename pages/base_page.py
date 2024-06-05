from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page_on_url(self, url):
        self.driver.get(url)

    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_clickable_and_find_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(locator))

        return element

    def click_on_button_wait_of_visible(self, locator):
        button = self.wait_and_find_element(locator)
        button.click()

    def click_on_button_clickable(self, locator):
        button_header = self.wait_clickable_and_find_element(locator)
        button_header.click()

    def set_field_argument(self, locator,
                           argument):
        input_element = self.wait_and_find_element(locator)
        input_element.send_keys(argument)
