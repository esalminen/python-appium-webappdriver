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
        desired_caps["app"] = "C:\\Temp\\testapp\\OrderPrototype_v4.exe"

        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities=desired_caps)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    # The following table shows the mapping between the locators in Appium and Inspector.
    #
    # Appium WebDriver locator      Inspect.exe property
    # ------------------------------------------------------------------------------------
    # FindElementByAccessibilityId  AutomationId
    # FindElementByClassName        ClassName   
    # FindElementById               RuntimeId(decimal)
    # FindElementByName             Name
    # FindElementByTagName          LocalizedControlType(upper camel case)

    def selectproduct(self, product):
        productComboBox = self.driver.find_element_by_accessibility_id("cbSortcriterion")
        productComboBox.click()
        productComboBox.send_keys(f'{product}\n')

    def insertAmount(self, amount):
        self.driver.find_element_by_accessibility_id("tbProductPcs").send_keys(amount)

    def selectDoor(self, door):
        # select door
        doorComboBox = self.driver.find_element_by_accessibility_id("cbDestination")
        doorComboBox.click()
        # doorComboBox.send_keys(f'{door}\n')
        doorComboBox.send_keys()

    def test_selectProduct(self):
        self.selectproduct('1122')
        self.insertAmount(5)
        self.selectDoor('Door 1')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleCalculatorTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
