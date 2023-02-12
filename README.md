# Windows Forms UI testing with Python, Appium and Webappdriver

## Installation
- Install latest stable Python environment from **[here](https://www.python.org/downloads/)**
- Install Appium v.1.3.0 with command `pip install appium-python-client==1.3.0`
- Install WinAppDriver from **[here](https://github.com/microsoft/WinAppDriver/releases/download/v1.2.1/WindowsApplicationDriver_1.2.1.msi)**
- You also need some windows element inspecting tool. **[Here](https://learn.microsoft.com/en-us/windows/win32/winauto/inspect-objects)** is info about Accessibility Insights which Microsoft recommends and **[here](https://learn.microsoft.com/en-us/windows/win32/winauto/inspect-objects)** is more info about Microsoft Inspect.exe which is a legacy tool.

## C# Project RPA_TestApp
Is a simple C# test application for file `desktopdemo.py` where each of the UI buttons print different text to the middle of the form. Appium tests that the text is correct after pressing each of the four buttons.

## How to use the Appium with Windows Forms application
 #### The following table shows the mapping between the locators in Appium and Inspector.

    Appium WebDriver locator            Accessibility Insight / Inspect.exe property
    ------------------------------------------------------------------------------------
    find_element_by_name                Name
    find_element_by_accessibility_id    AutomationId
    find_element_by_classname           ClassName   
    find_element_by_id                  RuntimeId