"use strict";

require("./third_parties/appium/helpers/setup");

var wd = require("wd"),
		_ = require('underscore'),
		serverConfigs = require('./third_parties/appium/helpers/appium-servers');

describe("android webview", function () {

	const EMAIL_TEST = "test_user@example.com";
	const PASSWORD_TEST = "test_PASSWORD_1234";
	const APPIUM_VERSION = '1.4.11';
	const PLATFORM_VERSION = '4.4';
	const EMULATOR_NAME = 'emulator_name';
	const APK_PATH = '/path/to/your/application.apk';
	const WEBVIEW_CONTEXT = 'WEBVIEW_com.example.main';
	const WAIT_TIMEOUT = 3000;
	const THIS_TIMEOUT = 300000;

	this.timeout(THIS_TIMEOUT);
	var driver;
	var allPassed = true;

	var android44 = {
		browserName: '',
		'appium-version': APPIUM_VERSION,
		platformName: 'Android',
		platformVersion: PLATFORM_VERSION,
		deviceName: EMULATOR_NAME,
		app: APK_PATH
	};

	before(function () {
		var serverConfig = serverConfigs.local;
		driver = wd.promiseChainRemote(serverConfig);
		require("./third_parties/appium/helpers/logging").configure(driver);

		var desired = android44;
		return driver
			.init(desired)
			.setImplicitWaitTimeout(WAIT_TIMEOUT);
	});

	after(function () {
		return driver.quit();
	});

	afterEach(function () {
		allPassed = allPassed && this.currentTest.state === 'passed';
	});

	it("test user can login and go to home", function () {
		return driver
			.contexts(WEBVIEW_CONTEXT)
			.then(function (ctxs) {
				console.log(ctxs);
				return driver.context(ctxs[ctxs.length - 1]);
			})
			.elementById('emailInputId')
				.clear()
				.sendKeys(EMAIL_TEST)
			.elementById('passwordInputId')
				.clear()
				.sendKeys(PASSWORD_TEST)
			.elementById('loginButtonId')
				.click()
			.sleep(5000)
			.source().then(function (source) {
				source.should.include('anyResultPageContent');
			});
	});
});
