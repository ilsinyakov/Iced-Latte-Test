from pages.base_page import BasePage
from pages.login_page import LoginPage


def test_guest_can_register(browser):
    link = "https://iced-latte.uk/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    