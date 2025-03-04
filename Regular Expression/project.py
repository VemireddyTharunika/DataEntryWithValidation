import re
import smtplib

# Name validation
while True:
    pattern = re.compile(r'^[A-Za-z ]+$')
    name = input("Enter Name: ")
    if pattern.fullmatch(name):
        break
    else:
        print("Enter Name in the correct format.")

# DOB validation
while True:
    pattern = re.compile(r'^\d{2}-\d{2}-\d{4}$')
    dob = input("Enter Date of Birth (dd-mm-yyyy): ")
    if pattern.fullmatch(dob):
        break
    else:
        print("Enter DOB in the correct format.")

# Mobile number validation
while True:
    pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
    phone = input("Enter Mobile Number (xxx-xxx-xxxx): ")
    if pattern.fullmatch(phone):
        break
    else:
        print("Enter Mobile in the correct format.")

# Instagram ID (no strict validation needed)
insta = input("Enter Insta ID: ")

# Email validation (optional)
while True:
    email = input("Enter Email: ")
    if email == "":
        email = None
        break
    pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@gmail\.com$')
    if pattern.fullmatch(email):
        break
    else:
        print("Enter Email in the correct format.")

# If email is provided, send details via email
if email:
    sender_email = "tharunikavemireddy@gmail.com"
    password = "gxeb phei hmci emcy"  

    message = f"""\
Subject: User Details

Name: {name}
Date of Birth: {dob}
Mobile: {phone}
Instagram ID: {insta}
Email: {email}
"""

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, email, message)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Error:", e)
else:
    print("No email provided. Details were not sent.")
