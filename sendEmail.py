import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Email account credentials
sender_email = "boot.taherhasan@gmail.com"
receiver_email = "eng.taherhasan@gmail.com"
password = "huew xzqj wmzw bmdg"  # Use App Passwords if using Gmail with 2FA

# Create the multipart message
msg = MIMEMultipart()
msg['Subject'] = "Here is your screenshot"
msg['From'] = sender_email
msg['To'] = receiver_email

# Add plain text
text = "Hello,\n\nPlease find the screenshot below.\n\nBest regards."
msg.attach(MIMEText(text, 'plain'))

# Add HTML with inline image
html = """
<html>
  <body>
    <p>Hello,<br>
       Here is the screenshot:<br>
       <img src="cid:image1">
    </p>
  </body>
</html>
"""
msg.attach(MIMEText(html, 'html'))

# Attach the image inline
def start(filename):
    with open(filename, 'rb') as img_file:
        img = MIMEImage(img_file.read(), name="screenshot.png")
        img.add_header('Content-ID', '<image1>')
        img.add_header('Content-Disposition', 'inline', filename="screenshot.png")
        msg.attach(img)

    # Send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, password)
        smtp.send_message(msg)
    print("Email sent successfully.")






