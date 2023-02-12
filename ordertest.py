import os
import unittest
from selenium.webdriver.common.keys import Keys
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

    def selectProduct(self, product):
        # auto complete combobox
        productComboBox = self.driver.find_element_by_accessibility_id("cbSortcriterion")
        productComboBox.click()

        # fill product number
        productComboBox.send_keys(f'{product}\n')

    def insertAmount(self, amount):
        # textbox
        tbProductPcs = self.driver.find_element_by_accessibility_id("tbProductPcs")

        # select all from textbox and delete
        tbProductPcs.send_keys(Keys.CONTROL + "a")
        tbProductPcs.send_keys(Keys.DELETE)

        # set new value to textbox
        tbProductPcs.send_keys(amount)

    def selectDoor(self, downPress):
        # combobox without auto complete
        doorComboBox = self.driver.find_element_by_accessibility_id("cbDestination")

        # press down n times to set door from dropdownlist
        for i in range(downPress):
            doorComboBox.send_keys(Keys.ARROW_DOWN)

    def addRow(self):
        # button
        self.driver.find_element_by_accessibility_id("btnAdd").click()

    def addProductRow(self, product, amount, downPress, firstRow):
        self.selectProduct(product)  
        self.insertAmount(amount)

        # second to n row is delivered to same location as first row
        if firstRow:
            self.selectDoor(downPress)

        self.addRow()


    def test_addProductRows(self):
        self.addProductRow('1122', 500, 4, True)
        self.addProductRow('1132', 200, None, False)
        self.addProductRow('1161', 50, None, False)
        self.addProductRow('1165', 200, None, False)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleCalculatorTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
