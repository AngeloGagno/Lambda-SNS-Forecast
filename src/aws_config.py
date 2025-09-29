import boto3

def sns_config(message,subject,topic_name,aws_access_key_id,aws_secret_access_key,region_name):
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
