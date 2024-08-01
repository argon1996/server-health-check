import requests
import smtplib
from email.mime.text import MIMEText

def check_server_health(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        return False

def send_email(subject, body, to_email):
    from_email = 'youremail@domain.com'
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    with smtplib.SMTP('smtp.yourserver.com') as server:
        server.login('yourusername', 'yourpassword')
        server.sendmail(from_email, to_email, msg.as_string())

if __name__ == "__main__":
    url = 'http://mi-aplicacion.com/health'
    if check_server_health(url):
        print("Server is healthy")
    else:
        send_email('Server Health Alert', 'The server is down!', 'recipient@domain.com')
