from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.registration_page import RegistrationPage
from time import sleep


def test_guest_can_register(browser):
    link = "https://iced-latte.uk/"
    first_name = "Test"
    last_name = "Testtest"
    email = "test@test.com"
    password = "15678asdfg!"
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.go_to_registration_page()
    registration_page = RegistrationPage(browser, browser.current_url)
    registration_page.register_new_user(first_name, last_name, email, password)
    sleep(5)
