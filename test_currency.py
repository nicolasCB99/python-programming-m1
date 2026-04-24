import unittest
from unittest.mock import patch, Mock
from currency_api import CurrencyDashboard


class TestCurrencyDashboard(unittest.TestCase):
    """Test the main currency dashboard functions."""

    # Setting up test object

    def setUp(self):
        self.dashboard = CurrencyDashboard()

    # Testing for valid latest rate retrieval
    
    @patch("currency_api.requests.get")
    def test_latest_rate(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {
            "amount": 1.0,
            "base": "USD",
            "date": "2026-04-23",
            "rates": {"EUR": 0.92}
        }
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        result = self.dashboard.get_latest_rate("USD", "EUR", 1)
        self.assertEqual(result, 0.92)

    # Testing for invalid base currency

    def test_invalid_currency_code(self):
        with self.assertRaises(ValueError):
            self.dashboard.validate_currency_code("XXX")

    # Testing for invalid amount
    
    def test_invalid_amount(self):
        with self.assertRaises(ValueError):
            self.dashboard.validate_amount(0)

    # Testing for negative amount
    
    def test_negative_amount(self):
        with self.assertRaises(ValueError):
            self.dashboard.validate_amount(-5)

    # Testing for historical data retrieval

    @patch("currency_api.requests.get")
    def test_historical_rates_dataframe(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {
            "rates": {
                "2024-01-01": {"EUR": 0.91},
                "2024-01-02": {"EUR": 0.92},
                "2024-01-03": {"EUR": 0.93}
            }
        }
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        df = self.dashboard.get_historical_rates("USD", "EUR")

        self.assertEqual(len(df), 3)
        self.assertIn("Date", df.columns)
        self.assertIn("Rate", df.columns)


if __name__ == "__main__":
    unittest.main()