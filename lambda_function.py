import boto3
import os
import json

# Cliente para interactuar con SNS
sns_client = boto3.client('sns')

def lambda_handler(event, context):
    try:
        # Iterar sobre los mensajes recibidos del evento de SQS
        for record in event['Records']:
            # Extraer el cuerpo del mensaje SQS
            message_body = record['body']
            print(f"Mensaje recibido: {message_body}")
            
            # Parsear el cuerpo del mensaje a JSON (si aplica)
            try:
                parsed_message = json.loads(message_body)
                print(f"Mensaje parseado: {parsed_message}")
            except json.JSONDecodeError:
                parsed_message = message_body  # Si no es JSON, usar el texto como está
            
            # Construir mensaje para SNS
            sns_message = f"Nuevo mensaje en SQS: {parsed_message}"
            
            # Obtener el ARN del tema SNS desde las variables de entorno
            sns_topic_arn = os.environ['SNS_TOPIC_ARN']
            
            # Publicar mensaje en el tema SNS
            response = sns_client.publish(
                TopicArn=sns_topic_arn,
                Message=sns_message,
                Subject="Notificación de mensaje en SQS"
            )
            print(f"Notificación enviada con ID: {response['MessageId']}")
        
        # Respuesta exitosa después de procesar todos los mensajes
        return {
            'statusCode': 200,
            'body': "Mensajes procesados con éxito"
        }
    
    except Exception as e:
        # Manejo de errores
        print(f"Error procesando el evento: {str(e)}")
        return {
            'statusCode': 500,
            'body': f"Error: {str(e)}"
        }
