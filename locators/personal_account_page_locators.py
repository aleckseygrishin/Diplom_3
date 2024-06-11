from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:
    HISTORY_ORDER_BUTTON = (By.XPATH, "//a[text()='История заказов']")
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    HISTORY_ORDER_ORDER_NUMBER = (By.XPATH, "//p[@class='text text_type_digits-default']")
