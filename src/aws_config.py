import boto3

def sns_config(message:str,subject:str,topic_name:str,aws_access_key_id:str,aws_secret_access_key:str,region_name:str) -> None:
    try:
        sns = boto3.client('sns', aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key,region_name=region_name)
        response = sns.publish(
            TopicArn=topic_name,
            Message=message,
            Subject=subject                     
        )
        print("Mensagem enviada com ID:", response["MessageId"])
    except Exception as e:
        print(f'Error ao enviar a mensagem: {e}')
