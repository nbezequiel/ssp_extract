from unittest import TestCase
from navigator import Validate
from test.test_utils import ExtractorHelper
from unittest.mock import patch
from model import Element, ActionType

class TestValidator(TestCase):

    validator = Validate()
    helper = ExtractorHelper()
    params = []
    elements_year = []
    elements_department = []
    node_year = Element("dummy", "years", ActionType.LOOP)
    node_department = Element("dummy", "departments", ActionType.LOOP)


    def setUp(self):
        self.elements_year = self.helper.get_year_elements()
        self.elements_department = self.helper.get_department_elements()

    ## validate -> is_valid
    @patch("navigator.validate.Occurrence")
    def test_is_valid_should_be_true(self, mock_occurrence):
        self.helper.mock_is_valid_should_be_ok(mock_occurrence)
        is_valid = self.validator.is_valid()
        self.assertEqual(is_valid, True)
    
    @patch("navigator.validate.Occurrence")
    def test_is_valid_should_be_false(self, mock_occurrence):
        self.helper.mock_is_valid_should_be_false(mock_occurrence)
        is_valid = self.validator.is_valid()
        self.assertEqual(is_valid, False)

    ## validate -> filter
    @patch("navigator.validate.Occurrence")
    def test_filter_should_return_same_list_when_latest_none(self, mock_occurrence):
        self.helper.mock_filter_latest_should_be_none(mock_occurrence)
        elem_list = self.validator.filter(self.elements_year, self.node_year)
        self.assertEqual(self.elements_year, elem_list)
    
    @patch("navigator.validate.Occurrence")
    def test_filter_year_list_when_latest_valid_and_all_departments(self, mock_occurrence):
        self.helper.mock_filter_by_year_all_departments(mock_occurrence)
        value = self.validator.filter(self.elements_year, self.node_year)
        self.assertEqual(2, len(value))
        self.assertIsNotNone(value)
    
    @patch("navigator.validate.Occurrence")
    def test_filter_year_list_when_latest_valid(self, mock_occurrence):
        self.helper.mock_filter_by_year_missing_departments(mock_occurrence)
        value = self.validator.filter(self.elements_year, self.node_year)
        self.assertEqual(3, len(value))
        self.assertIsNotNone(value)
    
    @patch("navigator.validate.Occurrence")
    def test_filter_department_list(self, mock_occurrence):
        self.helper.mock_filter_by_departments(mock_occurrence)
        value = self.validator.filter(self.elements_department, self.node_department)
        self.assertEqual(3, len(value))
        self.assertIsNotNone(value)
        
    