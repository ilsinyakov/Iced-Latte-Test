from base_page import BasePage
from locators import LoginPageLocators

 
class LoginPage(BasePage):
    def go_to_register_page(self):
        link = self.browser.find_element(*LoginPageLocators.LOGIN_REGISTER_BUTTON)
        link.click()
