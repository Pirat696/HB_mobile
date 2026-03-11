from appium.webdriver.common.appiumby import AppiumBy


class LoginPageLocators:
    SIGN_IN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'SIGN IN')
    GET_STARTED_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'GET STARTED')
    NEXT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'NEXT')
    LETS_GO_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "LET`S GO")
    TAP_PHONE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText")')
    TAP_PHONE_VERIFY_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,
                               'new UiSelector().className("android.view.View").instance(2)')
