import unittest
from selenium import webdriver
import ts_register

class roommatesLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        logFile=open('ts_logs/log.txt','r')
        self.email=logFile.read()
        if(self.email==""):
            print("No email found, running ts_register.py...")
            registrationTest=unittest.TestLoader().loadTestsFromModule(ts_register)
            unittest.TextTestRunner(verbosity=2).run(registrationTest)
            self.email=logFile.read()
        

    def test_login(self):
        driver = self.driver
        driver.get("http://next.roommates.net")
        button_signin = driver.find_element_by_xpath("//*[@id='welcome']/a[1]")
        button_signin.click()
        textField_email=driver.find_element_by_xpath("//*[@id='sign-in']/div/form/input[1]")
        textField_email.send_keys(self.email)
        textField_password=driver.find_element_by_xpath("//*[@id='sign-in']/div/form/input[2]")
        textField_password.send_keys("password")
        button_submit = driver.find_element_by_xpath("//*[@id='sign-in']/div/form/button")
        button_submit.click()
        #add assertions

    

    def tearDown(self):
        self.driver.close()


        
if __name__=='__main__':
    print("ts_login.py directly invoked")
    unittest.main()
else:
    print("ts_login.py running as module")
