import pytest
from src.page import BasePage
from src.locators.login_page import LoginPageLocators


class TestLogin:

    page: BasePage

    def test_login(self):
        self.page.tap(LoginPageLocators.GET_STARTED_BUTTON)
        self.page.tap(LoginPageLocators.NEXT_BUTTON)
        self.page.tap(LoginPageLocators.NEXT_BUTTON)
        self.page.tap(LoginPageLocators.LETS_GO_BUTTON)
        self.page.tap(LoginPageLocators.SIGN_IN_BUTTON)
        self.page.tap(LoginPageLocators.TAP_PHONE_BUTTON)
        self.page.send(LoginPageLocators.TAP_PHONE_BUTTON, '00000000000')
        self.page.tap(LoginPageLocators.NEXT_BUTTON)
        self.page.tap(LoginPageLocators.TAP_PHONE_VERIFY_BUTTON)
        self.page.send2(LoginPageLocators.TAP_PHONE_VERIFY_BUTTON, '0000')
