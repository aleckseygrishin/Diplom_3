import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop
from locators.base_page_locators import BasePageLocators
from urls import Urls


class BasePage:
    def __init__(self, driver, user_data_registration=None):
        self.driver = driver
        self.user_data_registration = user_data_registration

    @allure.step("Возвращаем данные пользователя переданные в конструктор класс")
    def get_user_data(self):
        if self.user_data_registration is not None:
            return self.user_data_registration

    @allure.step("Возвращаем email пользователя")
    def get_user_email(self):
        return self.get_user_data()["email"]

    @allure.step("Возвращаем password пользователя")
    def get_user_password(self):
        return self.get_user_data()["password"]

    @allure.step("Открываем страницу по url")
    def open_page_on_url(self, url):
        self.driver.get(url)

    @allure.step("Возвращаем элемент после ожидания по видимости")
    def wait_and_find_element(self, locator, get_element=None):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))
        if (get_element is None) or (get_element is True):
            return self.driver.find_element(*locator)

    @allure.step("Возвращаем элемент после ожидания по появлению")
    def wait_presents_element_located(self, locator):
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(locator))

    @allure.step("Возвращаем элемент после ожидания по кликабельности")
    def wait_clickable_and_find_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(locator))

        return element

    @allure.step("Кликаем по кнопке, после ожидания по появлению")
    def click_on_button_wait_of_visible(self, locator):
        button = self.wait_and_find_element(locator)
        button.click()

    @allure.step("Кликаем по кнопке, после ожидания по кликабельности")
    def click_on_button_clickable(self, locator):
        button_header = self.wait_clickable_and_find_element(locator)
        button_header.click()

    @allure.step("Заполняем поле переданным аргументом")
    def set_field_argument(self, locator, argument):
        input_element = self.wait_and_find_element(locator)
        input_element.send_keys(argument)

    @allure.step('Возвращаем текущую ссылку на страницу')
    def get_current_url(self, url):
        WebDriverWait(self.driver, 30).until(expected_conditions.url_to_be(url))
        return self.driver.current_url

    @allure.step('Возвращаем текст элемента найденного по локатору')
    def get_text_element(self, locator):
        return self.wait_and_find_element(locator).text

    @allure.step('Возвращаем атрибут элемента найденного по локатору')
    def get_attribute_element(self, locator, attribute):
        return self.wait_and_find_element(locator).get_attribute(attribute)

    @allure.step('Проверяем что элемент отображается пользователю')
    def check_is_displayed(self, locator):
        element = self.wait_and_find_element(locator)
        return element.is_displayed()

    @allure.step("Перетаскиваем ингредиент в поле добавления")
    def add_ingredient_drag_and_drop(self, source_locator, target_locator):
        source = self.wait_and_find_element(source_locator)
        target = self.wait_and_find_element(target_locator)
        drag_and_drop(self.driver, source, target)

    # Сделал общим, для нескольких тестов, поэтому поместил в BasePage
    @allure.step("Перетаскиваем булочку, в поле добавления ингредиента")
    def add_bread_ingredient(self):
        self.add_ingredient_drag_and_drop(source_locator=BasePageLocators.BREAD_INGREDIENT_FIRST,
                                          target_locator=BasePageLocators.SECTION_DROP_INGREDIENT)

    @allure.step("Авторизация на сайте")
    # Метод для авторизации на сайте, чтобы был общим разместил в BasePage
    def login(self):
        self.open_page_on_url(Urls.LOGIN_PAGE_URL)
        self.set_field_argument(BasePageLocators.LOGIN_EMAIL_FIELD, self.get_user_email())
        self.set_field_argument(BasePageLocators.LOGIN_PASSWORD_FIELD, self.get_user_password())
        self.click_on_button_wait_of_visible(BasePageLocators.LOGIN_BUTTON_ENTER)
