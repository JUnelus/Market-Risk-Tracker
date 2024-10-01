import os
import smtplib
from email.mime.text import MIMEText
from risk_calculator import RiskCalculator
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

THRESHOLD = -0.05  # Example threshold for Value-at-Risk

def send_alert(message):
    sender = "JimmyUnelus@gmail.com"
    recipient = "JimmyUnelus@gmail.com"
    msg = MIMEText(message)
    msg['Subject'] = "Risk Alert!"
    msg['From'] = sender
    msg['To'] = recipient

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(f"{os.getenv('email')}", f"{os.getenv('password')}")
        server.sendmail(sender, recipient, msg.as_string())

if __name__ == "__main__":
    calculator = RiskCalculator()
    data = calculator.get_market_data()
    var = calculator.calculate_var(data)
    print(f"Calculation to Email: {var}")

    if var < THRESHOLD:
        send_alert(f"Value-at-Risk exceeded threshold! Current VaR: {var}")