# Currency Exchange Rate Calculator

This Python script allows you to retrieve currency exchange rates and calculate the converted amount between two currencies using the ExchangeRate API.

## Prerequisites

- Python 3.x
- `requests` library (install using `pip install requests`)

## Usage

1. Clone the repository or download the script.

2. Open a terminal and navigate to the directory containing the script.

3. Run the script using the command: `python exchange_rate_calculator.py`

4. Follow the prompts to enter the base currency, target currency, and the amount to exchange.

5. The script will retrieve the exchange rate and calculate the converted amount, which will be displayed in the console.

## Example

Let's say we want to convert 100 USD to EUR.

```shell
What currency do you want to exchange?: USD
What currency do you want to exchange to?: EUR
Enter the amount you want to exchange: 100
Output:
-------------------------------
instant exchange rate
USD = 0.8413
------------result------------
100.0 USD = 84.13
In this example, the exchange rate from USD to EUR is 0.8413, and the converted amount is 84.13 EUR.
Credits

This script uses the ExchangeRate API (https://api.exchangerate.host) to retrieve currency exchange rates.
License

This project is licensed under the MIT License.
