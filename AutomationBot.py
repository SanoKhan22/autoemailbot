import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Email:
    def __init__(self, sender_email, recipient_email, subject, message):
        self.sender_email = sender_email
        self.recipient_email = recipient_email
        self.subject = subject
        self.message = message

    def display_email(self):  
        print("Sender Email:", self.sender_email)
        print("Recipient Email:", self.recipient_email)
        print("Subject:", self.subject)
        print("Message:", self.message)

class AutomatedEmail(Email):
    def __init__(self, sender_email, recipient_email, subject, message, schedule_time):
        super().__init__(sender_email, recipient_email, subject, message)
        self.schedule_time = schedule_time  

    def display_email(self):
        super().display_email()
        print("Scheduled Time:", self.schedule_time)

    def send_email(self):
        try:
            smtp_server = "smtp.gmail.com"
            smtp_port = 587
            sender_email = self.sender_email
            sender_password = "khannasar22"  

            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = self.recipient_email
            msg['Subject'] = self.subject
            msg.attach(MIMEText(self.message, 'plain', 'utf-8'))

            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
            server.quit()

            print(f"Email successfully sent to {self.recipient_email} at {self.schedule_time}")

        except Exception as e:
            print("Error sending email:", e)

email = Email("eusanokhan@gmail.com", "mahnoorpriv0098@gmail.com", "Hello", "This is a test email.")
email.display_email()

print("\n---\n")

automated_email = AutomatedEmail("eusanokhan@gmail.com", "mahnoorpriv0098@gmail.com", "Reminder", "Meeting at 2 PM", "8:25 PM")
automated_email.display_email()

print("\n---\n")

automated_email.send_email()
