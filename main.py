import os
import requests
#from dotenv import load_dotenv

#load_dotenv()  # loads variables from .env into the environment

parameters = {
    "lat":51.435517,
    "lon":14.239534,
    "appid":os.environ.get("OWM_API_KEY"),
    "cnt":4
}

response = requests.get('https://api.openweathermap.org/data/2.5/forecast',params=parameters)
response.raise_for_status()
data = response.json()
print(f'HTTP Status Code: {response.status_code}')


code_list = [weather['id'] for item in data['list'] for weather in item['weather'] ]
if max(code_list)>= 500:
    print("Bring an umbrella")
