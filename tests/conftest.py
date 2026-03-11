import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import xcuitest
from src.page import BasePage


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Remote(
        "127.0.0.1:4723",
        options=UiAutomator2Options().load_capabilities(
            {
                "platformName": "Android",
                "appium:automationName": "UiAutomator2",
                "appium:deviceName": "Pixel_9",
                "appium:app": "/Users/alexanderivchenko/Desktop/prod-com.heatbit-v2.14.0(137)_2026_01_27_16_46-prod-release.apk",
                "appium:appPackage": "com.heatbit",
                "appium:enforceAppInstall": True
            }
        ))

    yield driver
#    driver.quit()


@pytest.fixture(scope="session")
def page(driver):
    return BasePage(driver)


@pytest.fixture(scope="class", autouse=True)
def with_page(request, page):
    request.cls.page = page
