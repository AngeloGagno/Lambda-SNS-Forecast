from datetime import datetime
from dotenv import load_dotenv
import os

def filter_workdays(workdays:list) -> bool:
    if datetime.weekday(datetime.now()) in workdays:
        return True
    else: return False

def filter_raindays(rain_amount):
    if rain_amount >= 0.5:
        return True
    else: return False

def filter_cold_temperature(temperature):
    if temperature <= 18.0:
        return True
    else: return False

def get_lat_long():
    _ = load_dotenv(override=True)
    return os.getenv('lat'),os.getenv('long')

def formated_date():
    return datetime.now().strftime(r'%d/%m/%Y')