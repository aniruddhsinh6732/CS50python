import requests
import sys
import json

try:
    if len(sys.argv) == 1:
        print("Missing command-line argument")
        sys.exit()
    
    n = float(sys.argv[1])
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
    result = float(o["bpi"]["USD"]["rate_float"])*n
    print(result)
except ValueError:
    print("command-line argument is not number")
    sys.exit()  

#except requests.RequestException: