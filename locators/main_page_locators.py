from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']/parent::a")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']/parent::a")
    BREAD_INGREDIENT_FIRST = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/parent::a")
    WINDOW_INGREDIENT = (By.XPATH, "//h2[text()='Детали ингредиента']/parent::div")
    WINDOW_FINISH_CREATE_ORDER = (By.XPATH, "//p[text()='идентификатор заказа']/parent::div/parent::div")
    CLOSE_BUTTON = (By.XPATH, "//h2[text()='Детали ингредиента']/parent::div/following-sibling::button")
    SECTION_DROP_INGREDIENT = (By.XPATH, "//ul/parent::section")
    COUNT_ADD_INGREDIENT = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/parent::a/div/"
                                      "p[@class='counter_counter__num__3nue1']")
    BUTTON_CREATE_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")
