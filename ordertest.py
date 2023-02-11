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

    # The locators supported by WinAppDriver are similar to the ones in Selenium WebDriver.
    # The following table shows the mapping between the locators in Selenium WebDriver and WinAppDriver.
    #
    # Selenium WebDriver locator    Locator strategy    Inspect.exe property
    # --------------------------------------------------------------------------------------------
    # FindElementByAccessibilityId  accessibility id    AutomationId
    # FindElementByClassName        class name          ClassName   
    # FindElementById               id                  RuntimeId(decimal)
    # FindElementByName             name                Name
    # FindElementByTagName          tag name            LocalizedControlType(upper camel case)

    def selectproduct(self, product):
        self.driver.find_element_by_accessibility_id("cbSortCriterion").click()
        self.driver.find_element_by_accessibility_id("cbSortCriterion").find_element_by_id(product).click()
        displayResult = self.driver.find_element_by_accessibility_id("cbSortCriterion")
        return displayResult

    def insertAmount(self, amount):
        # insert value to amount text box
        self.driver.find_element_by_accessibility_id("tbProductPcs").send_keys(amount)

    def test_selectProduct(self):
        #self.selectproduct(0)
        self.insertAmount(5)
        self.assertEqual(self.getresults(), "Hello")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleCalculatorTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
