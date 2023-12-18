import sys
import requests

# If does not have command line argument
if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")

# If has one command line argument
if len(sys.argv) == 2:

    # Take command line argument and case it float
    try:
        amount = float(sys.argv[1])

    # Handle exception releated to Value Error and Print "Command-line argument is not a number"
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # Request API from "https://api.coindesk.com/v1/bpi/currentprice.json"
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

        # Check API status for any error
        response.raise_for_status()

        # If the request is successful, parse the JSON response to get the Bitcoin price information.
        price = response.json()

        # Calculate total price requested by user
        total_price = (float(price["bpi"]["USD"]["rate_float"]) * amount)

        # Print and display with thousands separator and four decimal place
        print(f"${total_price:,.4f}")

    # Handle exceptions related to the API request
    except requests.RequestException as e:
        sys.exit(f"Error making API request: {e}")
