import requests

# 地域名を指定
region_name = "札幌市"
api_key = "あなたのapikey"

# 警報をリクエストするためのURL
api_url = f"https://weather-aler-api.onrender.com/weather/{region_name}?api_key={api_key}"

# リクエストを送信
response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    alert = data['alert']
    warnings = data['warnings']
    warning_message = warnings[0] if warnings else '特になし'

    print(f"<地域 : {alert}\n警報&注意報 : {warning_message}")
elif response.status_code == 403:
    print("無効なAPIキーです。")
elif response.status_code == 404:
    print("警報または注意報はありません。")
else:
    print(f"HTTPエラーが発生しました: {response.status_code}")