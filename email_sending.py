import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from urllib.parse import quote

def send_email(recipients, cc=None):
    # Email settings
    email_from = 'kartik@project-lithium.com'  # Sender email
    smtp_server = 'smtp.gmail.com'              # SMTP server
    smtp_port = 587                              # SMTP port for TLS
    smtp_user = 'kartik@project-lithium.com'    # SMTP username
    smtp_password = 'lpolrrwyvnffyynv'           # SMTP password or app password

    subject = "Test Email with Tracking Pixel"   # Subject of the email

    # Set up the MIME (Multipurpose Internet Mail Extensions)
    message = MIMEMultipart("alternative")
    message["From"] = email_from
    message["To"] = ", ".join(recipients)        # Join multiple recipients with a comma
    message["Subject"] = subject

    # Base URL for tracking pixel (your deployed Streamlit app)
    tracking_pixel_url = "https://emailappg-jffcb4rrgn2mf7rez44ddv.streamlit.app"

    # Construct the HTML email content for each recipient
    for recipient in recipients:
        # Encode the recipient's email for the URL
        encoded_recipient = quote(recipient)
        
        # HTML content with tracking pixel
        html_content = f"""
        <html>
        <body>
            <p>Hello, this is a test email with a tracking pixel for {recipient}!</p>
            <img src="{tracking_pixel_url}/?recipient={encoded_recipient}" style="display:none" />
        </body>
        </html>
        """
        
        # Attach the HTML content to the message
        message.attach(MIMEText(html_content, "html"))

    # Send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade to a secure connection using TLS
            server.login(smtp_user, smtp_password)  # Log in to the SMTP server
            server.sendmail(email_from, recipients, message.as_string())  # Send the email
        print(f"Email successfully sent to {', '.join(recipients)}")  # Success message
    except Exception as e:
        print(f"Failed to send email: {str(e)}")  # Error message

# Call the function to send email with multiple recipients
send_email(
    recipients=[
        'kartikpande12@gmail.com',
        'vrushabhnichat@gmail.com'
    ],
    cc=None  # You can add CC recipients here if needed
)
