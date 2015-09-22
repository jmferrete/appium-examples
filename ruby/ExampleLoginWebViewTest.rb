#!/usr/bin/env ruby

require 'rubygems'
require 'spec'
require 'appium_lib'
require 'selenium-webdriver'

describe 'Login' do

	EMAIL_TEST = 'test_user@example.com'
	PASSWORD_TEST = 'test_PASSWORD_1234'
	RELATIVE_APK_PATH = '../relative/path/to/your/application.apk'
	PLATFORM_VERSION = '4.4'
	EMULATOR_NAME = 'emulator_name'
	WEBVIEW_CONTEXT = 'WEBVIEW_com.example.main'
	APPIUM_VERSION = '1.4.11'

	def desired_caps
		{
			caps: {
				:'appium-version' => APPIUM_VERSION,
				platformName: 'Android',
				platformVersion: PLATFORM_VERSION,
				deviceName: EMULATOR_NAME,
				app: RELATIVE_APK_PATH,
				name: 'Sample mobile test'
			},
			appium_lib: {
				wait: 360
			}
		}
	end

	before do
		Appium::Driver.new(desired_caps).start_driver
		set_context(WEBVIEW_CONTEXT)
	end

	after do
		driver_quit
	end

	it 'test user can login and go to home' do
		# Given:
		email_input = find_element(:id,'emailInputId')
		email_input.clear()
		password_input = find_element(:id,'passwordInputId')
		password_input.clear()
		submit_button = find_element(:id,'loginButtonId')

		# When:
		email_input.type(EMAIL_TEST)
		password_input.type(PASSWORD_TEST)
		submit_button.click()

		# Then:
		sleep(5)
		otherNewsHome = driver.find_element(:id,'anyResultPageContentId')
		otherNewsHome.instance_of?Selenium::WebDriver::Element
	end
end

print Minitest.run_specs({ :info => [__FILE__] }).first

