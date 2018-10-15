from selenium import webdriver
import unittest
from Login_Page import LoginToApplication


class LandingPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('C:\Personal\HTML-CSS\Python\chromedriver.exe')
        self.driver.implicitly_wait(10)

    def test_Landing_Page(self):
        driver = self.driver
        LoginToApplication.test_Login_to_Application(self)
        logo = driver.find_element_by_id('db_button_logo')
        self.assertTrue(logo.is_displayed())
        globalsetup = driver.find_element_by_id('db_click_uzd')
        self.assertTrue('üZD',globalsetup.text)
        regionalsetup = driver.find_element_by_id('db_click_rzd')
        self.assertTrue('rZD', regionalsetup.text)
        regionalsetup.click()
        markattendance = driver.find_element_by_id('db_mark_attendance')
        self.assertTrue('Dienstantritt melden',markattendance.text)
        regionaldispatcher = driver.find_element_by_id('db_mark_other_question')
        self.assertTrue('Direkte Fragen an rZD',regionaldispatcher.text)


    def Teardown(self):
        self.driver.close()


#if __name__ == '__main__':
def main():
    unittest.main()

if  __name__ =='__main__':main()

