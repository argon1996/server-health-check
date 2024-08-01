# Server Health Check

Este repositorio contiene un script en Python para verificar el estado de un servidor.

## Script

- **health_check.py**: Script principal para verificar el estado del servidor y enviar notificaciones por correo electrónico en caso de que el servidor esté caído.

## Configuración

### Variables

- **url**: URL del servidor a verificar.
- **smtpServer**: Servidor SMTP para enviar correos.
- **smtpFrom**: Dirección de correo del remitente.
- **smtpTo**: Dirección de correo del destinatario.
- **smtpUsername**: Usuario para el servidor SMTP.
- **smtpPassword**: Contraseña para el servidor SMTP.

## Uso

1. Clonar este repositorio.
2. Configurar las variables de entorno necesarias.
3. Ejecutar el script:
   ```sh
   python health_check.py
