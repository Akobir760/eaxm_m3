import csv
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



def reader(file_path):
    if os.path.exists(path=file_path):
        with open(file=file_path, mode="r", encoding="UTF-8") as file:
            return list(csv.reader(file))
        

def writer(file_path, data, mode ="w"):
    with open(file=file_path, mode=mode, newline="") as file:
        writer = csv.writer(file)
        if mode == "w":
            writer.writerows(data)
        elif mode == "a":
            writer.writerow(data)


def generate_id(file_path):
    file_data = reader(file_path=file_path)
    if len(file_data) == 0:
        return 1
    else:
        return int(file_data[-1][0]) + 1
    

def email_sender(r_email, m_body):
    sender_email = "sanjarbekwork@gmail.com"
    receiver_email = r_email
    password = "pqmk cvds dzdn gmll"

    subject = "Test Email"
    body = m_body

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)

    except Exception as e:
        print(f"Failed to send email. Error: {e}")


def is_active(file_path1):
    file_data = reader(file_path=file_path1)
    for user in file_data:
        if int(user[-1]) == 1:
            return user[0]
        

def log_out(file):
    file_data = reader(file_path=file)
    for user in file_data:
        if int(user[-1]) == 1:
            user[-1] = 0

    writer(file_path=file, data=file_data)

