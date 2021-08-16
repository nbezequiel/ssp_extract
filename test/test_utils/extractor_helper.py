from selenium.webdriver.firefox.webelement import FirefoxWebElement
from unittest.mock import MagicMock, patch, Mock, PropertyMock
from model import Occurrence
from mapper import OccurrenceMapper


class ExtractorHelper:
    occurrence_list_1 = list(range(0,15))
    occurrence_list_2 = list(range(0,15))

    def mock_set_data_should_be_ok(self, mock_ocurrence):
        mock_query = Mock()
        mock_query.count.return_value = 0
        mock_ocurrence.objects.return_value = mock_query
    
    def mock_is_valid_should_be_ok(self, mock_ocurrence):
        mock_ocurrence.objects.distinct.return_value = 119

    def mock_is_valid_should_be_false(self, mock_ocurrence):
        mock_ocurrence.objects.distinct.return_value = 120

    def mock_filter_latest_should_be_none(self, mock_ocurrence):
        mock_ocurrence.objects.order_by().first.return_value = None
    
    def mock_filter_by_year_all_departments(self, mock_ocurrence):
        occurrence = OccurrenceMapper.values_to_occurrence(self.occurrence_list_1, '2018', 'DP Barra Funda')
        mock_ocurrence.objects.order_by().first.return_value = occurrence
        mock_ocurrence.objects().distinct().count.return_value = 119
    
    def mock_filter_by_year_missing_departments(self, mock_ocurrence):
        occurrence = OccurrenceMapper.values_to_occurrence(self.occurrence_list_1, '2018', 'DP Barra Funda')
        mock_ocurrence.objects.order_by().first.return_value = occurrence
        mock_ocurrence.objects().distinct().count.return_value = 100
        
    def mock_filter_by_departments(self, mock_ocurrence):
        occurrence = OccurrenceMapper.values_to_occurrence(self.occurrence_list_1, '2018', 'DP Barra Funda')
        mock_ocurrence.objects.order_by().first.return_value = occurrence
        mock_ocurrence.objects().distinct().count.return_value = 100

    def _generate_web_element(self, text = 'default'):
        web_element = WebElementMock(text)
        return web_element

    def get_department_elements(self):
        names = ['DP Sé', 'DP Pinheiros', 'DP Barra Funda', 'DP A', 'DP B', 'DP C']
        web_elements = []
        for name in names:
            elem = self._generate_web_element(name)
            web_elements.append(elem)
        return web_elements
    
    def get_year_elements(self):
        names = ['2021', '2020', '2019', '2018', '2017', '2016']
        web_elements = []
        for name in names:
            elem = self._generate_web_element(name)
            web_elements.append(elem)
        return web_elements

    def get_default_elements(self):
        web_elements = []
        for i in range(0,14):
            elem = self._generate_web_element()
            web_elements.append(elem)
        return web_elements
    
    def mock_occurrencies_values(self):
        return [self.occurrence_list_1, self.occurrence_list_2]



class WebElementMock:
    def __init__(self, text):
        self.text = text
