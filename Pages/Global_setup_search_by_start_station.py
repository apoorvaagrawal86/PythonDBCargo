from selenium import webdriver
import unittest
from Global_Setup import GlobalSetupPage

class GlobalSetupSearchStationPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('C:\Personal\HTML-CSS\Python\chromedriver.exe')
        self.driver.implicitly_wait(10)

    def test_Search_By_Start_Station(self):
        driver = self.driver

