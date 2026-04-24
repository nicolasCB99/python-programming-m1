import logging
from currency_api import CurrencyDashboard
from currency_labels import currency_labels
from visualization import create_line_chart, create_comparison_bar_chart


# Configure logging
logging.basicConfig(
    filename="currency_dashboard.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# Display supported currencies
def display_supported_currencies() -> None:
    """Display supported currency codes and labels for the user."""
    print("\n=== Supported Currency Examples ===")
    for code, name in currency_labels.items():
        print(f"{code} - {name}")


# Getting valid currency code from user
def get_currency_input(prompt_text: str, dashboard: CurrencyDashboard) -> str:
    """Prompt the user for a valid currency code."""
    while True:
        user_input = input(prompt_text).strip().upper()

        try:
            dashboard.validate_currency_code(user_input)
            return user_input
        except ValueError as error:
            print(f"Error: {error}")
            logging.error("Invalid currency input: %s", user_input)


# Getting valid amount from user
def get_amount_input(prompt_text: str, dashboard: CurrencyDashboard) -> float:
    """Prompt the user for a valid positive amount."""
    while True:
        user_input = input(prompt_text).strip()

        try:
            amount = float(user_input)
            dashboard.validate_amount(amount)
            return amount
        except ValueError:
            print("Error: Please enter a valid positive number.")
            logging.error("Invalid amount input: %s", user_input)


# Asking user if they want to continue
def ask_to_continue() -> bool:
    """Ask the user whether they want to run another comparison."""
    while True:
        choice = input("\nWould you like to run another comparison? (yes/no): ")
        choice = choice.strip().lower()

        if choice in ["yes", "y"]:
            return True
        elif choice in ["no", "n"]:
            print("\nThank you for using the Currency Exchange Dashboard.")
            print("Program closing.")
            return False
        else:
            print("Please enter yes or no.")


# Running one dashboard session
def run_dashboard() -> None:
    """Run one full currency dashboard session."""
    dashboard = CurrencyDashboard()

    print("\n=== Currency Exchange Dashboard ===")
    display_supported_currencies()

    base_currency = get_currency_input(
        "\nEnter base currency code (example: USD): ",
        dashboard
    )
    target_currency = get_currency_input(
        "Enter target currency code (example: EUR): ",
        dashboard
    )
    amount = get_amount_input(
        "Enter amount to convert: ",
        dashboard
    )

    try:
        # Retrieving the latest exchange rate conversion
        converted_amount = dashboard.get_latest_rate(
            base_currency,
            target_currency,
            amount
        )

        print("\n=== Conversion Result ===")
        print(
            f"{amount:.2f} {currency_labels.get(base_currency, base_currency)} "
            f"= {converted_amount:.2f} "
            f"{currency_labels.get(target_currency, target_currency)}"
        )

        # Retrieving historical exchange rates
        history_df = dashboard.get_historical_rates(
            base_currency,
            target_currency
        )

        print("\n=== Historical Exchange Rate Data ===")
        print(history_df.head())

        # Retrieving comparison data for several currencies
        comparison_df = dashboard.get_currency_comparison(
            base_currency,
            amount
        )

        print("\n=== Currency Comparison Data ===")
        print(comparison_df)

        # Creating project charts
        create_line_chart(history_df, base_currency, target_currency)
        create_comparison_bar_chart(comparison_df, base_currency)

        logging.info(
            "Successful conversion: %s to %s for amount %.2f",
            base_currency,
            target_currency,
            amount
        )

    except Exception as error:
        print(f"Error: {error}")
        logging.exception("Program error occurred")


# Main program
if __name__ == "__main__":
    keep_running = True

    while keep_running:
        run_dashboard()
        keep_running = ask_to_continue()
