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
    with open(file=file_path, mode="w", newline="") as file:
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
    sender_email = "akobirortiqov@gmail.com"
    receiver_email = r_email
    password = "snnd frli cobd bhpe"  

    subject = "Sinov xabari"
    body = m_body

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Xabar muvaffaqiyatli yuborildi!")
        server.quit()
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")


def u_email_sender(s_email, app_p, m_body):
    sender_email = s_email
    receiver_email = "akobirortiqov@gmail.com"
    password = app_p  

    subject = "Sinov xabari"
    body = m_body

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Xabar muvaffaqiyatli yuborildi!")
        server.quit()
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")

