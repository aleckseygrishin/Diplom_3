import pytest
from selenium import webdriver


# Тесты на Firefox работают, через раз, выполнение только на Chrome
@pytest.fixture(scope='function')
def driver(request):
    browser = webdriver.Chrome()

    yield browser

    browser.quit()

