import unittest
import time
from random import uniform
from math import floor
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class roommatesRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_registration(self):
        driver = self.driver 
        driver.get("http://next.roommates.net")      
        button_signup = driver.find_element_by_xpath("//*[@id='welcome']/a[2]")
        button_signup.click(); #sign up button on home page
        textField_name = driver.find_element_by_xpath("//*[@id='sign-up']/form/div[1]/input")
        textField_name.send_keys("Test") #username textfield
        textField_email = driver.find_element_by_xpath("//*[@id='sign-up']/form/div[2]/div[1]/div/input")
        textField_email.send_keys(self.mailGen()) #email textfield
        textField_password = driver.find_element_by_xpath("//*[@id='sign-up']/form/div[2]/div[2]/div/input")
        textField_password.send_keys("password") #password textfield
        button_submit = driver.find_element_by_xpath("//*[@id='sign-up']/form/div[2]/div[4]/button")
        button_submit.click(); #click submit button
        note_confirmEmail = driver.find_element_by_xpath("//*[@id='check-email']/div[2]") #email confirm box
        assert note_confirmEmail
        self.login()
        

    def login(self):
        self.driver.get("http://next.roommates.net") #goes back to homepage
        button_signin = self.driver.find_element_by_xpath("//*[@id='welcome']/a[1]")
        button_signin.click()
        """Logs in with the previously created userID and pass"""
        textField_email = self.driver.find_element_by_xpath("//*[@id='sign-in']/div/form/input[1]")
        textField_email.send_keys(self.email)
        textField_loginPass = self.driver.find_element_by_xpath("//*[@id='sign-in']/div/form/input[2]")
        textField_loginPass.send_keys("password")
        button_signin = self.driver.find_element_by_xpath("//*[@id='sign-in']/div/form/button")
        button_signin.click()
        button_createHome = self.driver.find_element_by_xpath("//*[@id='choose-home']/div/center/a[1]")
        assert button_createHome #checks if createHome is there
        button_joinHome = self.driver.find_element_by_xpath("//*[@id='choose-home']/div/center/a[2]")
        assert button_joinHome #checks if joinHome is there

    def mailGen(self):

        self.email = "tester%s@example.com" % floor(uniform(1,10)*100) 
        return self.email
    
        
    def tearDown(self):
        self.driver.close();

if __name__ == "__main__":
    unittest.main()

