import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_SearchTest(self):
        driver = self.driver
        driver.get("https://www.python.org")
        driver.maximize_window()
        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys('pycon')
        elem.send_keys(Keys.RETURN)
        assert "No results found" not in driver.page_source

    def test_Minimize_window(self):
        self.driver.get("https://www.google.edu")

   
    @classmethod
    def tearDownClass(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/Emad/Desktop/selenium"))
