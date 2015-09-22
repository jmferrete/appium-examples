#!/usr/bin/env python

import os
import glob
import unittest
from time import sleep
from appium import webdriver

class AndroidWebViewTests(unittest.TestCase):

	EMAIL_TEST = 'test_user@example.com'
	PASSWORD_TEST = 'test_PASSWORD_1234'
	PLATFORM_VERSION = '4.4'
	RELATIVE_APK_PATH = '../relative/path/to/your/application.apk'
	MAIN_ACTIVITY = '.MainActivity'
	PACKAGE = 'com.example.main'
	EMULATOR_NAME = 'emulator_name'
	APPIUM_SERVER = 'http://localhost:4723/wd/hub'
	WEBVIEW_CONTEXT = 'WEBVIEW_com.example.main'

	def setUp(self):
		app = os.path.abspath(
				os.path.join(os.path.dirname(__file__),
					RELATIVE_APK_PATH))

		desired_caps = {
			'app': app,
			'appPackage': PACKAGE,
			'appActivity': MAIN_ACTIVITY,
			'platformName': 'Android',
			'platformVersion': PLATFORM_VERSION,
			'deviceName': EMULATOR_NAME
		}

		if (PLATFORM_VERSION != '4.4'):
			desired_caps['automationName'] = 'selendroid'

		self.driver = webdriver.Remote(APPIUM_SERVER,
			desired_caps)
		self.driver.switch_to.context(WEBVIEW_CONTEXT)

	def test_user_can_login_and_go_to_home(self):
		# Given:
		email_input = self.driver.find_element_by_id('emailInputId')
		email_input.clear()
		password_input = self.driver.find_element_by_id('passwordInputId')
		password_input.clear()
		submit_button = self.driver.find_element_by_id('loginButtonId')

		# When:
		email_input.send_keys(EMAIL_TEST)
		password_input.send_keys(PASSWORD_TEST)
		submit_button.click()

		# Then:
		sleep(5)
		source = self.driver.page_source
		self.assertNotEqual(-1, source.find("anyResultPageContent"))

	def tearDown(self):
		self.driver.quit()


if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(AndroidWebViewTests)
	unittest.TextTestRunner(verbosity=2).run(suite)
