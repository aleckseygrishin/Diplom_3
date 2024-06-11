from selenium.webdriver.common.by import By


class LoginPageLocators:
    REMEMBER_PASSWORD = (By.XPATH, "//a[text()='Восстановить пароль']")
    REMEMBER_PASSWORD_INPUT_EMAIL = (By.XPATH, "//input")
    BUTTON_RECOVER = (By.XPATH, "//button[text()='Восстановить']")
    PASSWORD_FIELD_REMEMBER = (By.XPATH, "//input[@name='Введите новый пароль']")
    PASSWORD_FIELD_DIV = (By.XPATH, "//label[text()='Пароль']/parent::div")
    EYE_BUTTON = (By.XPATH, "//input[@type='password']/following-sibling::div")
