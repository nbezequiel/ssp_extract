from selenium.webdriver.support.select import Select
from config import Logger
from abc import ABC, abstractmethod
from ..storage_service import storage
from ..extractor_service import Extractor
from ..filter_service import Filter
from ..page_service import Page


class Action(ABC):

    def __init__(self):
        self._storage = storage
        super().__init__()
        

    @abstractmethod
    def execute(self):
        pass

class ReadAction(Action, Logger):

    def __init__(self):
        super().__init__()
        self._extractor = Extractor() 
        self._page = Page()
    
    def execute(self, node):
        try:
            elements = self._page._get_web_elements(node)
            if elements != False:
                self._extractor.extract(self._storage.saved[0], self._storage.saved[1], elements)
                self._storage.saved = []
        except Exception as ex:
            self.log.info(ex)
            raise ex

    
class ClickAction(Logger, Action):

    def __init__(self):
        super().__init__()
        self._page = Page()

    def execute(self, node):
        try:
            element = self._page._get_web_element(node)
            self._page._click_web_element(element)
        except Exception as ex:
            self.log.error(str(ex))
            raise ex

class LoopAction(Logger, Action):

    def __init__(self):
        super().__init__()
        self._filter = Filter()
        self._page = Page()
    
    def execute(self, node):
        self.log.info("init")
        try:  
            elements = self._page._get_web_elements(node) 
            elements.pop(0)

            elements_value = self._filter.filter(elements, node)
            elements = []

            for el in elements_value:
                element = self._page._find_element_by_value(el)
                self._page._click_web_element(element)
                node.child.execute_action()
        
        except Exception as ex:
            self.log.error(str(ex))
            raise ex

class StoreAction(Action,Logger):

    def __init__(self):
        super().__init__()
        self._page = Page()

    def execute(self, node):
        try:
            elements = Select(self._page._get_web_element(node))
            element_text =  elements.first_selected_option.text
            self.log.info(element_text)
            self._storage.saved.append(element_text)
        except Exception as ex:
            self.log.error(ex)
            raise ex
