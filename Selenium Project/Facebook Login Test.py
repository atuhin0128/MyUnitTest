import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from PIL import Image


class FaceBookLogin(unittest.TestCase):

    def setUp(self):
        s = Service("D:\Chrome Driver\chromedriver.exe")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=s, options=chrome_options)


    def test_facebook_login(self):
        driver = self.driver
        driver.get("https://www.facebook.com/")
        driver.implicitly_wait(5000)
        self.assertIn("Facebook fd", driver.title)
        user_id = driver.find_element(By.NAME, "email")
        user_id.send_keys("test")
        user_pass = driver.find_element(By.NAME, "pass")
        user_pass.send_keys("test")
        login_but = driver.find_element(By.NAME, "login")
        driver.implicitly_wait(5000)
        login_but.click()



        # elem.send_keys(Keys.RETURN)
        # self.assertNotIn("No results found.", driver.page_source)

    def test_screenshots(self):
        driver = self.driver
        driver.save_screenshot("image.png")
        image = Image.open("image.png")
        image.show()

   # def tearDown(self):
     #   self.driver.close()


if __name__ == "__main__":
    unittest.main()
