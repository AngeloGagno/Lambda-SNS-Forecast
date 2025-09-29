import urllib.request
import json
from urllib.parse import urlencode, quote


def fetch_api(lat: float, long: float, forecast_days: int = 1, timezone: str = 'America/Sao_Paulo') -> list[dict]:
    base_url = 'https://api.open-meteo.com/v1/forecast'

    params = {
        'latitude': lat,
        'longitude': long,
        'hourly': 'temperature_2m,rain',
        'timezone': timezone,
        'forecast_days': forecast_days
    }

    
    url = f"{base_url}?{urlencode(params, encoding='utf-8', quote_via=quote, safe=',/')}"
    print(url)

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())

    return data



