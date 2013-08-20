TestScripts
===========

##Login/Registration

Copy `ts_registration.py`, `ts_login.py`, and `ts_logs` to your Python Lib directory. 

Windows Default: `C://PythonXY/Lib/`.

OSX Preinstalled: Run `type -a python` in Terminal.

Both scripts will run standalone. `ts_login.py` will run `ts_registration.py` if an email is not detected in `log.txt`

`log.txt` will only update in the current working directory that contains the `ts_logs` folder. So, if you copy all three files into `PythonXY/Lib`, the `ts_logs` folder will only work if you run the scripts from that directory.

###Using `ts_login` in other test scripts

Ensure that `ts_login.py` is in your `PythonXY/Libs` folder. In your new test script, have these imports, along with any existing ones.

    import unittest
    from webdriverplus import WebDriver
    import ts_login

In your `setUp()`, add the following line, if you want to reuse the browser for another outer level test.

    self.driver=WebDriver('firefox',reuse_browser=True)
