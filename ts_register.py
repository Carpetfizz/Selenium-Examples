import unittest
from random import uniform
from math import floor
from selenium import webdriver


class roommatesRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_registration(self):
        print("Running registration test...")
        driver = self.driver 
        driver.get("http://next.roommates.net")      
        button_signup = driver.find_element_by_xpath("//*[@id='welcome']/a[2]")
        button_signup.click();
        textField_name = driver.find_element_by_xpath("//*[@id='sign-up']/form/div[1]/input")
        textField_name.send_keys("Test") 
        textField_email = driver.find_element_by_xpath("//*[@id='sign-up']/form/div[2]/div[1]/div/input")
        textField_email.send_keys(self.mailGen()) 
        textField_password = driver.find_element_by_xpath("//*[@id='sign-up']/form/div[2]/div[2]/div/input")
        textField_password.send_keys("password") 
        button_submit = driver.find_element_by_xpath("//*[@id='sign-up']/form/div[2]/div[4]/button")
        button_submit.click(); 
           

    def mailGen(self):
        """log.txt must be in working directory. if you move it, make sure to change the below code"""
        self.email = "tester%s@example.com" % floor(uniform(1,10)*100)
        logFile=open('ts_logs/log.txt','w') #change first param, if you move directories
        logFile.write('')
        logFile.write(self.email)
        return self.email
    
        
    def tearDown(self):
        self.driver.close();

if __name__=='__main__':
    print("ts_register.py directly invoked")
    unittest.main()
else:
    print("ts_register.py imported as module")

