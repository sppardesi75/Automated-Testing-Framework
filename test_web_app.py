import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class WebAppTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_home_page_title(self):
        self.driver.get("https://example.com")
        self.assertEqual(self.driver.title, "Expected Title", "Title does not match")

    def test_login_functionality(self):
        self.driver.get("https://example.com/login")
        username = self.driver.find_element(By.ID, "username")
        password = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        username.send_keys("testuser")
        password.send_keys("password123")
        login_button.click()

        welcome_message = self.driver.find_element(By.ID, "welcome-message")
        self.assertTrue("Welcome, testuser" in welcome_message.text, "Login failed")

    def test_api_integration(self):
        self.driver.get("https://example.com/api-status")
        api_status = self.driver.find_element(By.ID, "api-status")
        self.assertEqual(api_status.text, "API is running", "API status is not as expected")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
