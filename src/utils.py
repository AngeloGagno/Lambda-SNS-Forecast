from datetime import datetime
from dotenv import load_dotenv
import os

def filter_workdays(workdays:list) -> bool:
    if datetime.weekday(datetime.now()) in workdays:
        return True
    else: return False

def filter_raindays(rain_amount:float) -> bool:
    if rain_amount >= 0.5:
        return True
    else: return False

def filter_cold_temperature(temperature:float) -> bool:
    if temperature <= 18.0:
        return True
    else: return False

def get_lat_long() -> float:
    _ = load_dotenv(override=True)
    return os.getenv('lat'),os.getenv('long')

def formated_date() -> str:
    return datetime.now().strftime(r'%d/%m/%Y')