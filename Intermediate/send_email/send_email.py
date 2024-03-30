import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = "********@gmail.com"
receiver_email = "********@gmial.com"
password = "********"

# Create message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Test Email"

body = "This is a test email sent using Python."
message.attach(MIMEText(body, "plain"))

# Connect to Gmail's SMTP server
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()  # Secure the connection
    server.login(sender_email, password)
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
