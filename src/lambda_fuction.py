from aws_config import sns_config
from transform import *
from extractor import fetch_api
from utils import get_lat_long,formated_date
import os

def filtered_data() -> list[dict]:
    lat,long = get_lat_long()
    json_request = fetch_api(lat=lat,long=long)
    return transform_pipeline(json_request)

def message_creator(data: list[dict] = filtered_data()) -> str:
    cold_status, tmin, tmax = get_cold_weather(data)
    vai_chover = get_rain(data)

    message = f"""
        Olá,

        Segue a previsão do tempo para hoje:

        - Temperatura máxima: {tmax}
        - Temperatura mínima: {tmin}
        """

    if cold_status:
        message += "\n Leve um casaco, pois estará frio."
    if vai_chover:
        message += "\n Atenção: há chance de chuva — não esqueça o guarda-chuva."

    message += "\n\nTenha um ótimo dia!\nEquipe de Previsão"

    return message

def lambda_handler():
    topic_name= os.getenv('SNS_ARN')
    aws_key = os.getenv('AWS_KEY')
    aws_secret_key= os.getenv('AWS_SECRET_KEY')
    message = message_creator()
    subject = f"Previsão do tempo para hoje - {formated_date()}"
    sns_config(message=message,subject=subject,topic_name=topic_name,aws_access_key_id=aws_key,aws_secret_access_key=aws_secret_key,region_name='us-west-1')
