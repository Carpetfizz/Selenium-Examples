import unittest
from selenium import webdriver
from ts_login import roommatesLogin

class roommatesCreateHome(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Firefox()

    def suite(self):
      
        suite=unittest.TestSuite()
        suite.addTest(roommatesCreateHome("test_create_home"))
        suite.addTest(roommatesLogin("test_login"))
        return suite

    def test_create_home(self):
        driver=self.driver
        driver.get("http://next.roommates.net")
    
    def tear_down(self):
        self.driver.quit()

if __name__=='__main__':
