from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLanguage:
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    def test_lang(self, browser):
        browser.get(self.link)
        try:
            WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket"))
            )
        except Exception:
            raise Exception("Add button not found")

