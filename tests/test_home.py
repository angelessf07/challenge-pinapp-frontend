from src.pages.home_page import HomePage
from src.helpers.data.home import TEXTS
import pytest, time


@pytest.mark.home
class TestHome:

    def test_home_text(self, login):
        home_page = HomePage(login)
        for text in TEXTS:
            assert home_page.is_visible_text(text), f"{text} was not visible"
        home_page.btn_click('APP_CONTROL_STOCK')
        home_page.scroll_to_exact_text("Pagos recibidos")
        home_page.btn_click('IMAGE_PNG')
        home_page.go_back()
        