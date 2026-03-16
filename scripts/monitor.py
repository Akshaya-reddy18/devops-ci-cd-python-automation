import requests
import time
import logging
import os
import smtplib
from email.message import EmailMessage

# Setup Logging
log_format = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=log_format, handlers=[
    logging.FileHandler("api_monitor.log"),
    logging.StreamHandler()
])

API_URL = os.getenv("MONITOR_API_URL", "http://localhost:5000/health")
CHECK_INTERVAL_SECONDS = int(os.getenv("MONITOR_INTERVAL", 60))
ALERT_EMAIL = os.getenv("ALERT_EMAIL", "")

def send_alert(error_msg):
    logging.error(f"ALERT: {error_msg}")
    if not ALERT_EMAIL:
        logging.warning("No ALERT_EMAIL set. Skipping email alert.")
        return
        
    try:
        msg = EmailMessage()
        msg.set_content(f"The API monitor detected an issue:\n\n{error_msg}")
        msg['Subject'] = 'CRITICAL: API Health Check Failed'
        msg['From'] = 'monitor@devops-demo.local'
        msg['To'] = ALERT_EMAIL
        
        # This assumes a local SMTP server for demo purposes.
        # Use proper SMTP configs in production.
        smtp_host = os.getenv("SMTP_HOST", "localhost")
        smtp_port = int(os.getenv("SMTP_PORT", 25))
        
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.send_message(msg)
            
        logging.info("Alert email sent successfully.")
    except Exception as e:
        logging.error(f"Failed to send alert email: {e}")

def check_health():
    try:
        logging.info(f"Checking health at {API_URL}")
        response = requests.get(API_URL, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "healthy":
                logging.info(f"Health Check Passed. Service is healthy.")
            else:
                send_alert(f"API is up but health status is not healthy: {data}")
        else:
            send_alert(f"API Returned status code {response.status_code}")
            
    except requests.exceptions.Timeout:
        send_alert(f"Request to {API_URL} timed out after 5 seconds")
    except requests.exceptions.ConnectionError:
        send_alert(f"Failed to connect to {API_URL}. Is the service running?")
    except Exception as e:
        send_alert(f"Unexpected error during health check: {e}")

if __name__ == "__main__":
    logging.info(f"Starting API Monitoring Service...")
    logging.info(f"Target: {API_URL} | Interval: {CHECK_INTERVAL_SECONDS}s")
    
    while True:
        check_health()
        time.sleep(CHECK_INTERVAL_SECONDS)
