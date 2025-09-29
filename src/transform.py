from datetime import datetime
from utils import filter_raindays,filter_cold_temperature


def format_json(data:list[dict]) -> list[dict]:
    list = []
    hours = data['hourly']['time']
    temperature = data['hourly']['temperature_2m']
    rain = data['hourly']['rain']
    for i in range(0,len(hours)):
        date_formated = datetime.fromisoformat(hours[i])
        json = {'hour':date_formated,
                'n_day_week':datetime.weekday(date_formated),
                'temperature': temperature[i],
                'rain':rain[i]}
        list.append(json)
    return list

def filter_workhours(data:list[dict],begin_work:int,leave_work:int) ->list[dict]:
    filtered_list = []
    for weather in data:
        if weather['hour'].hour >= begin_work and weather['hour'].hour <= leave_work:
            filtered_list.append(weather)

    return filtered_list

def get_rain(data:list[dict]) -> bool:
    rain_amount = [rain['rain'] for rain in data]
    max_rain = sorted(rain_amount)[0]
    return filter_raindays(max_rain) 

def get_cold_weather(data:list[dict]):
    cold_weather = [cold_weather['temperature'] for cold_weather in data]
    temperature = sorted(cold_weather)
    min_temperature =  temperature[-1]
    max_temperature = temperature[0]
    return filter_cold_temperature(max_temperature),max_temperature,min_temperature

def transform_pipeline(data,begin_work:int=6,leave_work:int=19):
    json_formated = format_json(data)
    return filter_workhours(json_formated,begin_work,leave_work)