from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '[href="/auth/login"]')        
    
class LoginPageLocators():
    LOGIN_REGISTER_BUTTON = (By.CSS_SELECTOR, '[href="/auth/registration"]')

class RegisterPageLocators():    
    REGISTER_FIRST_NAME_FIELD = (By.ID, 'firstName')
    REGISTER_LAST_NAME_FIELD = (By.ID, 'lastName')
    REGISTER_EMAIL_FIELD = (By.ID, 'email')
    REGISTER_PASSWORD_FIELD = (By.ID, 'password')    
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')    
