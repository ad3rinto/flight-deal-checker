#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_data import FlightData
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import requests
import os
import datetime
from dotenv import load_dotenv

load_dotenv()

SH_TOKEN = os.environ.get("SHEETY_TOKEN")
TW_SID = os.environ.get("TWILIO_ACC_SID")
TW_TOKEN = os.environ.get("TWILIO_TOKEN")
TW_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER")
TEQUILA_TOKEN = os.environ.get("TEQUILA_KEY")
TEQUILA_SEARCH_ENDPOINT = "https://api.tequila.kiwi/v2/locations/query"
SHEETY_URL = "https://api.sheety.co/83f756b5b637bb7aaefd61fc0a250dde/personalFlightDeals2024/prices"

# flight_params = {
#     "term": "MAN",

# }


sheety_headers = {
    'Authorization': 'Bearer '+ SH_TOKEN,
}


response_from_sheety = requests.get(url=SHEETY_URL, headers=sheety_headers)
print(response_from_sheety.json())