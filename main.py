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

headers = {
    'X-USER-TOKEN': SH_TOKEN
}


