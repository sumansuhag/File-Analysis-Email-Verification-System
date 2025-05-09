# -*- coding: utf-8 -*-
"""Email verification system

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TPb4C9nPnkB4SiydvyBbN3CRl5mXsrpk
"""

pip install smtplib email-validator

def send_email(receiver_email, otp):
    sender_email = "your_email@gmail.com"
    sender_password = "your_app_password"  # Use the App Password here

    message = f"Subject: Your OTP Code\n\nYour OTP code is: {otp}"

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

import smtplib
import random
import string

# Function to generate a random OTP
def generate_otp(length=6):
    digits = string.digits
    otp = ''.join(random.choice(digits) for _ in range(length))
    return otp

# Function to send OTP via email
def send_email(receiver_email, otp):
    sender_email = "your_email@example.com"
    sender_password = "your_password"

    message = f"Subject: Your OTP Code\n\nYour OTP code is: {otp}"

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

# Main function to handle OTP verification
def otp_verification():
    email = input("Enter your email: ")
    otp = generate_otp()
    send_email(email, otp)

    user_otp = input("Enter the OTP sent to your email: ")

    if user_otp == otp:
        print("OTP verified successfully!")
    else:
        print("Invalid OTP. Please try again.")

if __name__ == "__main__":
    otp_verification()