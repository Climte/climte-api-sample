import requests

region_name = "沖縄市"

API = f"https://weather-aler-api.onrender.com/weather/{region_name}"

try:
    res = requests.get(API)
    res.raise_for_status()
    data = res.json()

    alert = data['alert']
    warnings = data['warnings']
    warning_message = warnings[0] if warnings else '特になし'

    print(f"< {region_name} >\n地域 : {alert}\n警報&注意報 : {warning_message}")

except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except requests.exceptions.RequestException as err:
    print(f"An error occurred: {err}")
