import smtplib
import time
from email.message import EmailMessage

def send_email():
    # Email configurations
    smtp_server = "smtp.office365.com"
    smtp_port = 587
    email_address = "wordlai@hotmail.com"
    email_password = "723996lai"
    recipient = "laiwc0723@gmail.com"
    subject = "Automated Email"
    body = "This is an automated email sent every 5 minutes."

    # Create an email message
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = email_address
    msg['To'] = recipient

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Upgrade the connection to a secure one using TLS
        server.login(email_address, email_password)
        server.send_message(msg)

# Interval in minutes
interval = 5

while True:
    send_email()
    print("Email sent.")
    time.sleep(interval * 60)  # Wait for the specified number of minutes
