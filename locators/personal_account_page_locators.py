from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account']")
    HISTORY_ORDER_BUTTON = (By.XPATH, "//a[text()='История заказов']")
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")
