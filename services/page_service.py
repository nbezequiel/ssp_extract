from config import Logger
from .navigator_service import driver


class Page(Logger):

    def __init__(self):
        super().__init__()
        self._driver = driver

    def _init_driver(self):
        try:
            self._driver.get(self._driver_path)
        except Exception as ex:
            self.log.error(str(ex))
            raise ex

    def _click_web_element(self, web_element):
            web_element.click()

    def _get_web_element(self, element):
        return self._driver.find_element_by_css_selector(element.name)

    def _get_web_elements(self, element):
        try:
            return self._driver.find_elements_by_css_selector(element.name)
        except:
            return False

    def _find_element_by_value(self, value):
        return self._driver.find_element_by_xpath("//option[text()='"+value+"']")

