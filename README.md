# Desafio-modulo7

## Descripción del Sistema

Este sistema implementa una arquitectura de procesamiento de mensajes en AWS utilizando los siguientes servicios:

- **Amazon SNS (Simple Notification Service)**: Servicio de mensajería pub/sub para la publicación de notificaciones
- **Amazon SQS (Simple Queue Service)**: Cola de mensajes que almacena los mensajes para su procesamiento
- **AWS Lambda**: Función serverless que procesa los mensajes de la cola SQS y los reenvía a SNS

La arquitectura funciona de la siguiente manera:
1. Los mensajes son publicados en un tema SNS
2. El tema SNS está conectado a una cola SQS
3. La función Lambda se activa cuando hay mensajes en la cola SQS
4. La función procesa el mensaje y lo publica nuevamente en SNS con un formato específico

## Configuración del Proyecto

### Prerequisitos

1. Una cuenta de AWS con acceso programático (Access Key y Secret Key)
2. GitHub Actions habilitado en tu repositorio
3. AWS CLI instalado localmente (para pruebas)

### Variables de Entorno Requeridas

Configurar en GitHub (Settings > Variables > Actions):

**Variables:**
```
AWS_REGION: us-east-1
```

**Secrets:**
```
AWS_ACCESS_KEY_ID: [Tu AWS Access Key ID]
AWS_SECRET_ACCESS_KEY: [Tu AWS Secret Access Key]
SNS_TOPIC_NAME: mi-tema-notificaciones
SQS_QUEUE_NAME: mi-cola-mensajes
LAMBDA_FUNCTION_NAME: sqs-sns-processor
LAMBDA_ROLE_NAME: lambda-sns-sqs-role
```

### Estructura del Proyecto

```
.
├── .github/
│   └── workflows/
│       └── deploy.yml
├── lambda_function.py
└── README.md
```
## GitHub Actions

### Ejecutar el Workflow

1. Asegúrate de tener configuradas todas las variables y secrets necesarios en GitHub
2. Realiza un push a la rama main:
```bash
git add .
git commit -m "Deploy AWS resources"
git push origin main
```

3. El workflow se ejecutará automáticamente y:
   - Creará/actualizará el tema SNS
   - Creará/actualizará la cola SQS
   - Configurará la suscripción entre SNS y SQS
   - Desplegará la función Lambda
   - Configurará el trigger de SQS para Lambda

### Monitorear el Deployment

1. Ve a la pestaña "Actions" en tu repositorio de GitHub
2. Selecciona el workflow más reciente para ver el progreso
3. Revisa los logs de cada paso para verificar el éxito o identificar errores

## Pruebas del Sistema

### Verificar el Procesamiento
1. Ve a CloudWatch Logs en la consola de AWS
2. Busca el grupo de logs de tu función Lambda
3. Verifica los logs más recientes para ver el procesamiento del mensaje
