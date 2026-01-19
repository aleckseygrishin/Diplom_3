from selenium.webdriver.common.by import By


class FeedPageLocators:
    USER_ORDER_IN_FEED_PAGE = (By.XPATH, "//h2[text()='Флюоресцентный бургер']/parent::a/parent::li")
    ORDER_ID_LOCATORS = (By.XPATH, "//div[contains(@class, 'OrderHistory_textBox__3lgbs')]"
                                   "/p[contains(@class, 'text_type_digits-default')]")
    DONE_ORDER_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    DONE_ORDER_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")

    ORDER_ID_IN_WINDOW_ORDER = (By.XPATH, "//p[text()='идентификатор заказа']/parent::div/h2")
    TICK_SUCCESS = (By.XPATH, "//img[@alt='tick animation']")
    MODAL_WINDOW_ORDER_SUCCESS = (By.XPATH, "//div[@class='Modal_modal__P3_V5']")
