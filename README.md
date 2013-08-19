TestScripts
===========

##Login/Registration

Copy `ts_registration.py`, `ts_login.py`, and `ts_logs` to your Python Lib directory. 

Windows Default: `C://PythonXY/Lib/`.

OSX Preinstalled: Run `type -a python` in Terminal.

Both scripts will run standalone. `ts_login.py` will run `ts_registration.py` if an email is not detected in `log.txt`

NOTE: If you are importing the `ts_login.py` module into other TestScripts, find the `self.tearDownBool` variable in the setup function an set it to false. Ex:

`self.tearDownBool=False`

This will ensure that `ts_login.py` does not close the browser once the login test has been run, so that the test depending on login can run properly. 