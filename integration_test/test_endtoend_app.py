import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestAppE2E(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options)
        self.driver.get('http://localhost:5000')

    def tearDown(self):
        self.driver.quit()

    def test_add_and_delete_and_update_item(self):
        self.driver.set_window_size(1406, 860)
        self.driver.get("http://localhost:5000/")
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


if __name__ == "__main__":
    unittest.main()
