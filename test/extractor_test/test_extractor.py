from extrator import Extractor
from test.test_utils import ExtractorHelper
from unittest import TestCase
from unittest.mock import patch
from model import Occurrence


class TestExtractor(TestCase):

    extractor = Extractor()
    helper = ExtractorHelper()
    year = "2019"
    department = "DP Sé"
    elements = []
    occurrencies = []

    def setUp(self):
        self.occurrencies =  self.helper.mock_occurrencies_values()
        self.elements = self.helper.get_default_elements()

    # extractor -> _set_data
    @patch("extrator.extractor.Occurrence")
    def test_set_data_should_be_ok(self, mock_ocurrence):
        self.helper.mock_set_data_should_be_ok(mock_ocurrence)
        self.extractor._set_data(self.year, self.department, self.occurrencies)

    # extractor -> _get_occurrences
    def test_get_occurrences_should_be_valid(self):
        ocurrencies = self.extractor._get_occurrences(
            self.year, self.department, self.elements
        )
        [self.assertEqual(i, "default") for i in ocurrencies[0]]
        assert type(ocurrencies) == list

    # extractor -> extract
    @patch("extrator.extractor.Occurrence")
    def test_extract_should_be_ok(self, mock_ocurrence):
        self.helper.mock_set_data_should_be_ok(mock_ocurrence)
        self.extractor.extract(self.year, self.department, self.elements)
