from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.XPATH, "//android.widget.EditText[@text='ej: cristian@crisoft.dev']")
    PASSWORD = (By.XPATH, "//android.widget.EditText[@text='********']")
    LOGIN_BTN = (By.XPATH, "//android.view.ViewGroup[@content-desc=', Ingresar']/android.view.View")

    def login(self, user, password):
        self.find(self.USERNAME).send_keys(user)
        self.find(self.PASSWORD).send_keys(password)
        self.find(self.LOGIN_BTN).click()