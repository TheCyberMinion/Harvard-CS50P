import sys
import requests

key = '7f58dd5e74a2c47ac580d081c40e690f1073ae7f4314fc36d26c09b0253fbc14'
url = "https://rest.coincap.io/v3/assets/bitcoin"

def main():
    n = set_bitcoin()
    price = get_cost()
    cost = n * price
    print(f'${cost:,.4f}')

def get_cost():
    try:
        response = requests.get(url, params={"apiKey": key})
        data = response.json()
        price = float(data["data"]["priceUsd"])
        return price
    except requests.RequestException:
        sys.exit('Error Getting Price')

def set_bitcoin():
    if len(sys.argv) == 1:
        sys.exit('Missing command-line argument')
    else:
        try:
            return float(sys.argv[1])
        except ValueError:
            sys.exit('Command-line argument is not a number')

main()
