import os
import unittest
from appium import webdriver # appium 1.3.0, had trouble with latest version


class SimpleCalculatorTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        os.system(r'start "" /d "C:\Program Files (x86)\Windows Application Driver\" "WinAppDriver.exe"')

        # set up appium
        desired_caps = {}
        desired_caps["platformName"] = "Windows"
        desired_caps["platformVersion"] = "10"
        desired_caps["deviceName"] = "WindowsPC"
        desired_caps["app"] = "C:\\Temp\\testapp\\RPA_TestApp.exe"

        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities=desired_caps)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def getresults(self):
        displayResult = self.driver.find_element_by_accessibility_id("tbBtnText").text
        return displayResult

    def test_helloButton(self):
        self.driver.find_element_by_accessibility_id("btnHelloText").click()
        self.assertEqual(self.getresults(), "Hello")

    def test_howButton(self):
        self.driver.find_element_by_accessibility_id("btnHowText").click()
        self.assertEqual(self.getresults(), "How are you?")

    def test_seeButton(self):
        self.driver.find_element_by_accessibility_id("btnSeeText").click()
        self.assertEqual(self.getresults(), "See you later!")

    def test_goodbyeButton(self):
        self.driver.find_element_by_accessibility_id("btnGoodbyeText").click()
        self.assertEqual(self.getresults(), "Goodbye")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleCalculatorTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
