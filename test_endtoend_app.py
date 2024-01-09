import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class TestAppE2E(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument('--headless')
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        cls.driver.set_window_size(1406, 860)

    def test_add_and_delete_and_update_item(self):
        self.driver.find_element(By.NAME, "item").click()
        self.driver.find_element(By.NAME, "item").send_keys("12")
        self.driver.find_element(By.CSS_SELECTOR, "button").click()

        self.driver.find_element(By.NAME, "item").click()
        self.driver.find_element(By.NAME, "item").send_keys("123")
        self.driver.find_element(By.CSS_SELECTOR, ".container > form > button").click()

        self.driver.find_element(By.NAME, "item").click()
        self.driver.find_element(By.NAME, "item").send_keys("10")
        self.driver.find_element(By.CSS_SELECTOR, ".container > form > button").click()

        self.driver.find_element(By.NAME, "new_item").click()
        self.driver.find_element(By.NAME, "new_item").send_keys("100")
        self.driver.find_element(By.NAME, "new_item").send_keys(Keys.ENTER)

        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) input").click()
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) input").send_keys("14")
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) input").send_keys(Keys.ENTER)

        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) > a").click()
        self.driver.find_element(By.LINK_TEXT, "Delete").click()
        self.driver.find_element(By.LINK_TEXT, "Delete").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
