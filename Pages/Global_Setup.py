from selenium import webdriver
import unittest
from Landing_Page import LandingPage


class GlobalSetupPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:\Personal\HTML-CSS\Python\chromedriver.exe')
        self.driver.implicitly_wait(10)

    def test_Search_By_Train_No(self):
        driver = self.driver
        LandingPage.test_Landing_Page(self)
        #test_Landing_Page.globalsetup.click()
        #LandingPage.globalsetup.click()
        globalsetup = driver.find_element_by_id('db_click_uzd')
        globalsetup.click()
        infoText = driver.find_element_by_class_name('info-text')
        self.assertTrue('Bitte gib deine Zuginfos ein',infoText.text)
        trainnumber = driver.find_element_by_id('db_input_train_number')
        trainnumber.send_keys('41334')
        searchbutton = driver.find_element_by_id('db_button_search_train')
        searchbutton.click()
        routetext = driver.find_element_by_class_name('train-list-header')
        self.assertTrue('Wähle deinen Streckenabschnitt',routetext.text)
        trainline = driver.find_element_by_id('db_text_train_line_name')
        self.assertTrue('XDTV  - AWHOS', trainline.text)
        trainline.click()
        trainnotoverify = driver.find_element_by_id('db_text_train_number')
        self.assertTrue('41334', trainnotoverify.text)
        linenametoverify = driver.find_element_by_id('db_text_train_name')
        self.assertTrue('XDTV  - AWHOS', linenametoverify.text)
        regionname = driver.find_element_by_id('db_text_region')
        self.assertTrue('CMR Ost',regionname.text)
        pndteamname = driver.find_element_by_id('db_text_team')
        self.assertTrue('P&D Ausland Hl', pndteamname.text)
        arbeitsplatz = driver.find_element_by_id('db_text_workplace')
        self.assertTrue('32', arbeitsplatz.text)
        basanr = driver.find_element_by_id('db_text_base')
        self.assertTrue('927 3674',basanr.text)
        telefonnr = driver.find_element_by_id('db_text_contact')
        self.assertTrue('0341 968 3674',telefonnr.text)
        telefonnr.click()
        #dialog = self.driver.switch_to.active_element
        #self.assertTrue('Close ', dialog.text)
        #assert dialog.text == 'Open Pick an app?'
        #self.assertIn('Open Pick an app?', dialog.text)

    def test_Search_Train_By_Start_Station(self):
        driver = self.driver
        LandingPage.test_Landing_Page(self)
        #GlobalSetupPage.test_Search_By_Train_No(self)
        globalsetup = driver.find_element_by_id('db_click_uzd')
        globalsetup.click()
        infoText = driver.find_element_by_class_name('info-text')
        self.assertTrue('Bitte gib deine Zuginfos ein', infoText.text)
        trainnumber = driver.find_element_by_id('db_input_train_number')
        trainnumber.send_keys('41335')
        searchbutton = driver.find_element_by_id('db_button_search_train')
        searchbutton.click()
        errormessage = driver.find_element_by_class_name('error-text')
        self.assertTrue('Zug leider nicht gefunden, bitte Startpunkt eingeben', errormessage.text)
        trainstartstation = driver.find_element_by_class_name('train-label')
        self.assertTrue('Startpunkt des Zuges', trainstartstation.text)
        startstation = driver.find_element_by_id('db_input_start_station')
        startstation.send_keys('EDRH')
        stationcode = driver.find_element_by_id('db_text_station_code')
        self.assertTrue('EDRH', stationcode.text)
        stationcode.click()
        textstationcode = driver.find_element_by_id('db_text_station_code')
        self.assertTrue('EDRH', textstationcode.text)
        stationname = driver.find_element_by_id('db_text_station_name')
        self.assertTrue('Du-Ruhrort Hafen', stationname.text)
        regionname = driver.find_element_by_id('db_text_region')
        self.assertTrue('CMR WEST', regionname.text)
        pndteamname = driver.find_element_by_id('db_text_team')
        self.assertTrue('P&D volatil Du', pndteamname.text)
        arbeitsplatz = driver.find_element_by_id('db_text_workplace')
        self.assertTrue('92', arbeitsplatz.text)
        basanr = driver.find_element_by_id('db_text_base')
        self.assertTrue('9481 4988', basanr.text)
        telefonnr = driver.find_element_by_id('db_text_contact')
        self.assertTrue('0203 3017 4988', telefonnr.text)

    def Teardown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()