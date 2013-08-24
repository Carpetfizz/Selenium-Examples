TestScripts
===========

##Login/Registration

Copy `ts_registration.py`, `ts_login.py`, and `ts_logs` to your Python Lib directory. 

Windows Default: `C://PythonXY/Lib/`.

OSX Preinstalled: Run `type -a python` in Terminal.

Both scripts will run standalone. `ts_login.py` will run `ts_registration.py` if an email is not detected in `log.txt`

`log.txt` will only update in the current working directory that contains the `ts_logs` folder. So, if you copy all three files into `PythonXY/Lib`, the `ts_logs` folder will only work if you run the scripts from that directory.

###Using `ts_login` in other test scripts

Ensure that `ts_login.py` and `ts_register.py` is in your `PythonXY/Libs` folder. In your new test script, have these imports, along with any existing ones. In your constructor, or setup, add the following code in the event that you want to login.

    self.driver=ts_login.getOrCreateWebDriver()

Example:

	#someTest.py
	import stuff
	import ts_login

	class myTest(unittest.TestCase):
		def setUp():
			self.driver=ts_login.getOrCreateWebDriver()