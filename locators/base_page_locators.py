from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    LOGIN_PASSWORD_FIELD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    LOGIN_BUTTON_ENTER = (By.XPATH, "//button[text()='Войти']")
    SECTION_DROP_INGREDIENT = (By.XPATH, "//ul/parent::section")
    BREAD_INGREDIENT_FIRST = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/parent::a")
