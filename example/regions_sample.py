import requests

API = "https://weather-aler-api.onrender.com/regions"

try:
    res = requests.get(API)
    res.raise_for_status()
    data = res.json()
    print(data)

except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except requests.exceptions.RequestException as err:
    print(f"An error occurred: {err}")