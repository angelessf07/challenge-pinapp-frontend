from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException

class HomePage(BasePage):

    APP_CONTROL_STOCK = (By.XPATH, "//android.view.ViewGroup[@content-desc=', Pendiente, App Control De Stock, Actualizado 09 de nov de 2025, ']")
    IMAGE_PNG = (By.XPATH, "//android.view.ViewGroup[@content-desc=', imagen.png, , Imagen, , 28 Dic 2025, ']")

    def is_visible_text(self, text):
        try:
            locator = (By.XPATH, f"//android.widget.TextView[@text='{text}']")
            element = self.find(locator)
            return element.is_displayed()
        except TimeoutException:
            return False

    def btn_click(self, btn):
        self.find(getattr(self, btn)).click()