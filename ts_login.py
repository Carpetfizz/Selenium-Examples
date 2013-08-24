import unittest
from selenium import webdriver
import ts_register
from time import sleep

class roommatesLogin(unittest.TestCase):

    def setUp(self):
        logFile=open('ts_logs/log.txt','r')
        self.email=logFile.read()
        if(self.email==""):
            print("No email found, running ts_register.py...")
            registrationTest=unittest.TestLoader().loadTestsFromModule(ts_register)
            unittest.TextTestRunner(verbosity=2).run(registrationTest)
            self.email=logFile.read()
            self.driver=ts_register.getOrCreateWebDriver()
        else:
            print("Email found in log.txt")
            self.driver=webdriver.Firefox()
        if __name__=='__main__':
            self.quitBrowser=True
        
        

    def test_login(self):
        print("Running ts_login.py...")
        print("Logging in with: "+self.email)
        driver = self.driver
        driver.get("http://next.roommates.net")
        assert "http://next.roommates.net/#/welcome" in driver.current_url
        sleep(2)
        button_signin=driver.find_element_by_xpath("//*[@id='welcome']/a[1]")
        button_signin.click()
        assert "http://next.roommates.net/#/sign-in" in driver.current_url
        textField_email=driver.find_element_by_xpath("//*[@id='sign-in']/div/form/input[1]")
        textField_email.send_keys(self.email)
        textField_pass=driver.find_element_by_xpath("//*[@id='sign-in']/div/form/input[2]")
        textField_pass.send_keys("password")
        button_submitForm=driver.find_element_by_xpath("//*[@id='sign-in']/div/form/button")
        button_submitForm.click()
       
                    
    def tearDown(self):
        if(self.quitBrowser):
            self.driver.quit()


        
if __name__=='__main__':
    print("ts_login.py directly invoked")
    unittest.main()
else:
    print("ts_login.py running as module")
    
