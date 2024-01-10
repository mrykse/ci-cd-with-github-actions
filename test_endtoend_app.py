import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeType


class TestAppE2E(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1920,1200')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        self.driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install(),
                                       options=chrome_options)

    def test_add_and_delete_and_update_item(self):
        self.driver.set_window_size(1406, 860)
        self.driver.get("http://localhost:5000")  # Replace with the correct URL

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

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
