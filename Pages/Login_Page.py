from selenium import webdriver
import unittest


class LoginToApplication(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('C:\Personal\HTML-CSS\Python\chromedriver.exe')
        self.driver.implicitly_wait(10)

    def test_Login_to_Application(self):
        driver = self.driver
        driver.get('http://applabscloudndev.bcg.com:42031/login')
        self.assertIn('DB Cargo Routing', driver.title)
        info = driver.find_element_by_class_name('info-text')
        self.assertIn('Bitte geben Sie Ihren 4-stelligen Pin ein', info.text)
        key1 = driver.find_element_by_id('db_input_login_one')
        key1.send_keys('1')
        key2 = driver.find_element_by_id('db_input_login_two')
        key2.send_keys('2')
        key3 = driver.find_element_by_id('db_input_login_three')
        key3.send_keys('3')
        key4 = driver.find_element_by_id('db_input_login_four')
        key4.send_keys('4')
        username = driver.find_element_by_id('db_text_user_name')
        self.assertIn('Hallo Daniel !',username.text)

    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main()



