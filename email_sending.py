import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from urllib.parse import quote

def send_email(recipients, cc=None):
    # Email settings
    email_from = 'kartik@project-lithium.com'
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = 'kartik@project-lithium.com'
    smtp_password = 'lpolrrwyvnffyynv'  # Replace with your secure password or app password

    subject = "Test Email with Tracking Pixel"

    # Initialize the email content
    message = MIMEMultipart("alternative")
    message["From"] = email_from
    message["To"] = ", ".join(recipients)
    message["Subject"] = subject

    # Add CC recipients if any
    if cc:
        message["Cc"] = ", ".join(cc)
        all_recipients = recipients + cc
    else:
        all_recipients = recipients

    # Construct the HTML email content with tracking pixel for each recipient
    for recipient in recipients:
        encoded_recipient = quote(recipient)
        # Update the tracking pixel URL to point to your publicly accessible Streamlit app
        html_content = f"""
        <html>
        <body>
            <p>Hello, this is a test email with a tracking pixel for {recipient}!</p>
            <img src="http://localhost:8501/?recipient={encoded_recipient}" style="display:none" />
        </body>
        </html>
        """
        # Attach the HTML content
        message.attach(MIMEText(html_content, "html"))

    # Send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure connection using TLS
            server.login(smtp_user, smtp_password)
            server.sendmail(email_from, all_recipients, message.as_string())
        print(f"Email successfully sent to {', '.join(recipients)}")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

# Call the function to send email with multiple recipients
send_email(
    recipients=[
        'kartikpande12@gmail.com',
        'vrushabhnichat@gmail.com'
    ],
    cc=None  # Optional: Add CC recipients here
)
