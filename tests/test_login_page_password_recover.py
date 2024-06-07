import allure
from pages.login_page import LoginPage
from urls import Urls


class TestLoginPagePasswordRecover:
    @allure.title('Переход на страницу забыли пароль по кнопке "Восстановить пароль"')
    @allure.description('Ожидаем переход на страницу "забыли пароль"')
    def test_switch_on_forgot_password_page_current_url_correct(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page_on_url()
        login_page.click_on_password_recovery()

        assert login_page.get_current_url(Urls.FORGOT_PAGE_URL) == Urls.FORGOT_PAGE_URL

    @allure.title('Переход на страницу восстановления')
    @allure.description('Ожидаем переход на страницу восстановления пароля')
    def test_switch_on_reset_password_page_current_url_correct(self, driver, create_and_delete_user,
                                                               user_data_registration):
        login_page = LoginPage(driver, user_data_registration=user_data_registration)
        login_page.open_login_page_on_url()
        login_page.click_on_password_recovery()
        email = login_page.get_user_email()
        login_page.send_email_filed(email)
        login_page.click_on_button_recover()

        assert login_page.get_current_url(Urls.RESET_PASSWORD_URL) == Urls.RESET_PASSWORD_URL

    @allure.title('Проверка активности поля Пароль при нажатии на раскрытие пароля')
    @allure.description('Ожидаем: поле Пароль становится активным')
    def test_click_on_eye_button_field_password_is_active(self, driver, create_and_delete_user,
                                                          user_data_registration):
        login_page = LoginPage(driver, user_data_registration=user_data_registration)
        login_page.open_login_page_on_url()
        login_page.click_on_password_recovery()
        email = login_page.get_user_email()
        login_page.send_email_filed(email)
        login_page.click_on_button_recover()
        login_page.click_on_eye_button()

        assert (login_page.get_type_password_field() == "text"
                and "input_status_active" in login_page.include_class_name_in_element())
