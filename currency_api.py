import logging
import requests
import pandas as pd
from currency_labels import currency_labels


class CurrencyDashboard:
    """Handle API requests, validation, and data retrieval for the currency dashboard."""

    BASE_URL = "https://api.frankfurter.app"

    # Validating currency code
    def validate_currency_code(self, code: str) -> None:
        """Validate that the currency code exists in the supported labels."""
        if code not in currency_labels:
            raise ValueError(f"'{code}' is not a supported currency code.")

    # Validating amount
    def validate_amount(self, amount: float) -> None:
        """Validate that the amount is greater than zero."""
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

    # Getting latest exchange rate
    def get_latest_rate(self, base: str, target: str, amount: float) -> float:
        """Get the latest exchange rate conversion result."""
        self.validate_currency_code(base)
        self.validate_currency_code(target)
        self.validate_amount(amount)

        url = f"{self.BASE_URL}/latest?from={base}&to={target}&amount={amount}"

        logging.info("Requesting latest exchange rate: %s", url)

        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if "rates" not in data or target not in data["rates"]:
            raise ValueError("Invalid currency code or API response.")

        return float(data["rates"][target])

    # Getting historical exchange rates
    def get_historical_rates(self, base: str, target: str) -> pd.DataFrame:
        """Get historical exchange rates for the selected currencies."""
        self.validate_currency_code(base)
        self.validate_currency_code(target)

        url = f"{self.BASE_URL}/2024-01-01..2024-12-31?from={base}&to={target}"

        logging.info("Requesting historical exchange rates: %s", url)

        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if "rates" not in data:
            raise ValueError("Unable to retrieve historical data.")

        records = []

        for date, values in data["rates"].items():
            if target in values:
                records.append({
                    "Date": date,
                    "Rate": float(values[target])
                })

        if not records:
            raise ValueError("No historical records were returned from the API.")

        df = pd.DataFrame(records)
        df["Date"] = pd.to_datetime(df["Date"])
        df = df.sort_values("Date")

        return df

    # Getting currency comparison data
    def get_currency_comparison(self, base: str, amount: float) -> pd.DataFrame:
        """Get latest exchange rates for several common currencies."""
        self.validate_currency_code(base)
        self.validate_amount(amount)

        comparison_targets = ["EUR", "GBP", "JPY", "CAD", "AUD", "MXN"]

        # Remove the base currency from the comparison list if it is included
        comparison_targets = [
            currency for currency in comparison_targets if currency != base
        ]

        target_string = ",".join(comparison_targets)

        url = (
            f"{self.BASE_URL}/latest?"
            f"from={base}&to={target_string}&amount={amount}"
        )

        logging.info("Requesting currency comparison data: %s", url)

        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if "rates" not in data:
            raise ValueError("Unable to retrieve currency comparison data.")

        records = []

        for currency, value in data["rates"].items():
            records.append({
                "Currency": currency,
                "Converted Value": float(value)
            })

        return pd.DataFrame(records)