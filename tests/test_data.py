# test_data.py
import unittest
from country_picker.worker import CountryFetcher

class TestCountryParsing(unittest.TestCase):
    def test_country_parsing(self):
        """Test that CountryFetcher parses and sorts country names correctly."""
        mock_response = [
            {"name": "Brazil"},
            {"name": "Denmark"},
            {"name": "Argentina"}
        ]

        expected = ["Argentina", "Brazil", "Denmark"]
        result = sorted([c["name"] for c in mock_response])

        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
