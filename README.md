Currency Exchange Dashboard
Project Overview

This project is a Python Currency Exchange Dashboard that uses the Frankfurter API to retrieve real-time and historical exchange rate data.

The program allows users to:

- Convert one currency to another
- View historical exchange rate trends
- Generate comparison charts for multiple currencies
- Validate currency codes and amount input
- Handle invalid user input safely
- Record activity using logging
- Run unit tests for core functions

This project demonstrates modular programming, object-oriented design, data manipulation, API integration, visualization, testing, and debugging.

Project Files:

- main.py → runs the main dashboard program
- currency_api.py → handles API requests and validation
- currency_labels.py → stores supported currency labels
- visualization.py → creates line charts and comparison bar charts
- test_currency.py → unit tests for the main functions
- requirements.txt → required Python libraries
- currency_dashboard.log → stores logs for errors and successful runs

Libraries Used:

- requests
- pandas
- matplotlib
- unittest
- logging
- Installation

Install the required libraries using:

pip install -r requirements.txt

How to Run the Program

Run the main dashboard with:

python main.py

The program will ask for:

- Base currency code (example: USD)
- Target currency code (example: EUR)
- Amount to convert

For Example:

- Enter base currency code: USD
- Enter target currency code: EUR
- Enter amount to convert: 100

The program will display:

- Current conversion result
- Historical exchange rate data
- Historical line chart
- Currency comparison bar chart

After completion, the program asks:

Would you like to run another comparison? (yes/no)

- which will bring you to the start again or give a message about the program is being closed

Running Unit Tests

Run the test file using:

python test_currency.py

Expected result:

.....

Ran 5 tests

OK

This confirms that the validation methods and conversion logic are working correctly.

Logging and Debugging

The program creates a log file named:

currency_dashboard.log

This file records:

- Invalid currency inputs
- Invalid amount inputs
- Successful API requests
- Successful conversions
- Program errors if they occur

This helps with debugging and testing reliability.

Example Features Tested

The following error handling was tested:

- Invalid currency codes
- Negative amounts
- Zero values
- Non-numeric input
- Invalid yes/no responses

The program handles these safely without it crashing.