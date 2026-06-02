import smtplib
from email.message import EmailMessage
def send_email(sender,receiver,body,subject,app_password):
    # EmailMessage Object 
    message = EmailMessage()

    # General Info into the class
    message["From"] = sender
    message["To"]= receiver
    message["Subject"] = subject

    # Body
    message.set_content(body)

    # Creating a SMTP SSL connection manually 
    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)

    # Login Into gmail
    smtp.login(sender,app_password)

    # Sending Email
    smtp.send_message(message)

    # Close the SMTP connection
    smtp.quit()

def main():
    sender_email = "demo89631@gmail.com"
    password = "qexpqfwefsfbytcu"
    receiver_email = "patiljayesh9923@gmail.com"

    subj = "Test Mail From Python Script"

    body = '''Jay Ganesh,
    This is a test email send using Marvellous Python.

    Regards,
    Marvellous Infosystems
'''
    send_email(sender=sender_email,receiver=receiver_email,app_password=password,subject=subj,body=body)

    print("Marvellous Email Send Successfully")

if __name__ == "__main__":
    main()