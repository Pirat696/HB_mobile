from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from collections.abc import Callable


class BasePage:
    WAIT_TIMEOUT_S = 10

    def __init__(self, driver):
        self.driver = driver

    def wait(
        self,
        locator: tuple[str, str],
        timeout_s: float = WAIT_TIMEOUT_S,
        condition: Callable = EC.presence_of_element_located,
    ) -> WebElement:
        element = WebDriverWait(
            self.driver, timeout_s).until(condition(locator))
        return element

    def send(
        self,
        locator: tuple[str, str],
        keys: str | int,
        timeout_s: float = WAIT_TIMEOUT_S,
        condition: Callable = EC.presence_of_element_located
    ):
        element = self.wait(locator, timeout_s, condition)
        element.send_keys(keys)

    def tap(
        self,
        locator: tuple[str, str],
        timeout_s: float = WAIT_TIMEOUT_S,
        condition: Callable = EC.element_to_be_clickable

    ):
        element = self.wait(locator, timeout_s, condition)
        self.driver.execute_script('mobile: clickGesture', {
                                   'element': element.id})
