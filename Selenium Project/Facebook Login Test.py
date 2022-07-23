import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from PIL import Image

class FaceBookLogin(unittest.TestCase):

    def setUp(self):
        s = Service("D:\Chrome Driver\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)


    def test_facebook_login(self):
        driver = self.driver
        driver.get("https://www.facebook.com/")
        self.assertIn("Facebook", driver.title)
        user_id = driver.find_element(By.NAME, "email")
        user_id.send_keys("atuhin37@yahoo.com")
        user_pass = driver.find_element(By.NAME, "pass")
        user_pass.send_keys("lovebird")
        login_but = driver.find_element(By.NAME,"login")
        login_but.submit()
        driver.implicitly_wait(2000)
        #elem.send_keys(Keys.RETURN)
        #self.assertNotIn("No results found.", driver.page_source)

    def test_screenshots(self):
        driver = self.driver
        driver.save_screenshot("image.png")
        image = Image.open("image.png")
        image.show()
   # def tearDown(self):
       # self.driver.close()

if __name__ == "__main__":
    unittest.main()