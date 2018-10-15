from selenium import webdriver
import unittest
from selenium.common.exceptions import NoSuchElementException
from Login_Page import LoginToApplication


class RegionalSetupPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:\Personal\HTML-CSS\Python\chromedriver.exe')
        self.driver.implicitly_wait(10)

    def test_Mark_Attendance(self):
        driver = self.driver
        LoginToApplication.test_Login_to_Application(self)
        regionalsetup = driver.find_element_by_id('db_click_rzd')
        regionalsetup.click()
        markattendance = driver.find_element_by_id('db_mark_attendance')
        self.assertTrue('Dienstantritt melden', markattendance.text)
        searchdispatcher = driver.find_element_by_id('db_mark_other_question')
        self.assertTrue('Direkte Fragen an rZD',searchdispatcher.text)
        driver.execute_script("arguments[0].click();", markattendance)
        #markattendance.click()
        #successmessage = driver.find_element_by_id('db_text_message_success')
        #self.assertTrue('Danke dein')
        close = driver.find_element_by_id('db_click_dismiss')
        #close.click()
        #markattendance.click()
        driver.execute_script("arguments[0].click();", markattendance)
        failuremessage = driver.find_element_by_id('db_text_message_failure')
        self.assertTrue('Service bereits gemeldet', failuremessage.text)
        driver.execute_script("arguments[0].click();", close)
        #close.click()

    def test_View_Dispatcher(self):
        driver = self.driver
        LoginToApplication.test_Login_to_Application(self)
        regionalsetup = driver.find_element_by_id('db_click_rzd')
        regionalsetup.click()
        viewdispatcher = driver.find_element_by_id('db_mark_other_question')
        viewdispatcher.click()
        def search_dispatcher_loads():
            try:
                driver.find_element_by_id('db_input_start_station')
            except NoSuchElementException:
                return False
            return True
        search_dispatcher_loads()
        search_dispatcher = driver.find_element_by_id('db_input_start_station')
        search_dispatcher.send_keys('BERLIN')
        station_name = driver.find_element_by_id('db_text_region_location')
        self.assertTrue('rZD Berlin ',station_name.text)

    def tearDown(self):
        self.driver.close()

if __name__== '__main__':
    unittest.main()
