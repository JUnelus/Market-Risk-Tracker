import schedule
import time
import os

def run_data_ingestion():
    print("Running data ingestion...")
    os.system('python data_ingestion.py')

def run_risk_calculator():
    print("Running risk calculator...")
    os.system('python risk_calculator.py')

def run_alert_system():
    print("Running alert system...")
    os.system('python alert_system.py')

# Schedule the tasks
schedule.every(1).hours.do(run_data_ingestion)  # Runs every 1 hour
schedule.every(2).hours.do(run_risk_calculator)  # Runs every 2 hours
schedule.every(2).hours.do(run_alert_system)  # Runs every 2 hours after risk calculation

# If you want to run it at a specific time:
# schedule.every().day.at("10:00").do(run_data_ingestion)  # Runs daily at 10:00 AM

# Infinite loop to keep the scheduler running
while True:
    schedule.run_pending()
    time.sleep(1)
