from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']/parent::a")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']/parent::a")
    WINDOW_INGREDIENT = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened__3ISw4')]")
    WINDOW_FINISH_CREATE_ORDER = (By.XPATH, "//p[text()='идентификатор заказа']/parent::div/parent::div")
    CLOSE_BUTTON_FINISH_ORDER = (By.XPATH, "//button[@type='button']")
    CLOSE_BUTTON = (By.XPATH, "//h2[text()='Детали ингредиента']/parent::div/following-sibling::button")
    COUNT_ADD_INGREDIENT = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/parent::a/div/"
                                      "p[@class='counter_counter__num__3nue1']")
    BUTTON_CREATE_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")
    SECTION_OPENED_WINDOW = (By.XPATH, "//h2[text()='Детали ингредиента']/parent::div"
                                       "/parent::div/parent::section[@class='Modal_modal__P3_V5']")
    SOUSE_FIRST = (By.XPATH, "//p[text()='Соус Spicy-X']/parent::a")
    SOUSE_SECOND = (By.XPATH, "//p[text()='Соус фирменный Space Sauce']/parent::a")
    SECTION_DROP_INGREDIENT = (By.XPATH, "//ul/parent::section")
    BREAD_INGREDIENT_FIRST = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/parent::a")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account']")
