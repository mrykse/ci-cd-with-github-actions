import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pyvirtualdisplay import Display


class TestAppE2E(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Start virtual display
        cls.display = Display(visible=0, size=(800, 800))
        cls.display.start()

        # Configure Chrome options
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--window-size=1406,860')
        chrome_options.add_argument('--ignore-certificate-errors')

        # Initialize WebDriver
        cls.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

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
        # Stop virtual display and close WebDriver
        cls.display.stop()
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
