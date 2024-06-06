import allure

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop
from locators.login_page_locators import LoginPageLocators
from urls import Urls


class BasePage:
    def __init__(self, driver, user_data_registration=None):
        self.driver = driver
        self.user_data_registration = user_data_registration

    def get_user_data(self):
        if self.user_data_registration is not None:
            return self.user_data_registration

    def get_user_name(self):
        return self.get_user_data()["name"]

    def get_user_email(self):
        return self.get_user_data()["email"]

    def get_user_password(self):
        return self.get_user_data()["password"]

    def open_page_on_url(self, url):
        self.driver.get(url)

    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_and_find_element_invisible(self, locator):
        WebDriverWait(self.driver, 30).until(expected_conditions.invisibility_of_element_located(locator))
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

    @allure.step('Возвращаем текущую ссылку на страницу')
    def get_current_url(self, url):
        WebDriverWait(self.driver, 30).until(expected_conditions.url_to_be(url))
        return self.driver.current_url

    @allure.step('Возвращаем текст элемента найденного по локатору')
    def get_text_element(self, locator):
        return self.wait_and_find_element(locator).text

    @allure.step('Возвращаем тип элемента найденного по локатору')
    def get_attribute_element(self, locator, attribute):
        return self.wait_and_find_element(locator).get_attribute(attribute)

    @allure.step('Проверяем что элемент отображается пользователю')
    def check_is_displayed(self, locator):
        element = self.wait_and_find_element(locator)
        return element.is_displayed()

    def check_is_not_displayed(self, locator):
        element = self.wait_and_find_element_invisible(locator)
        return not element.is_displayed()

    def add_ingredient_drag_and_drop(self, source_locator, target_locator):
        source = self.wait_and_find_element(source_locator)
        target = self.wait_and_find_element(target_locator)
        drag_and_drop(self.driver, source, target)

    # Метод для авторизации на сайте, чтобы был общим разместил в BasePage
    def login(self):
        self.open_page_on_url(Urls.LOGIN_PAGE_URL)
        self.set_field_argument(LoginPageLocators.LOGIN_EMAIL_FIELD, self.get_user_email())
        self.set_field_argument(LoginPageLocators.LOGIN_PASSWORD_FIELD, self.get_user_password())
        self.click_on_button_wait_of_visible(LoginPageLocators.LOGIN_BUTTON_ENTER)
