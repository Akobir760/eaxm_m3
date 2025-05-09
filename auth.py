from filemanager import reader, writer, generate_id, email_sender
from datetime import datetime
from random import randint
import threading




def user_reg():
    f_data = reader(file_path="data/users.csv")
    user_data = reader(file_path="data/users.csv")
    email = input("Enter your email: ")
    for u_data in f_data:
        for user_d in user_data: 
            if u_data[1] == email or user_d[1] == email:
                print("This email already exists!")
                break 
    else:

        id = generate_id(file_path="data/users.csv")
        random_code = randint(1000, 9999)
        message_body = f"Tasdiqlash kodi: {random_code}"
        threading.Thread(target=email_sender, args=(email, message_body)).start()

        verification_code = int(input("Enter verification code (we send is to your email): "))
        
        while verification_code != random_code:
            verification_code = int(input("Enter verification code (we send is to your email): "))

        full_name = input("Enter your fullname: ")
        active = 0
        created_at = datetime.now()
        data = [id,email,full_name,created_at,active]
        writer(file_path="data/users.csv", data=data, mode="a")
        print("Saytimizda muvoffaqiyatli ro'yxatdan o'tdingiz!")
        
            


def teach_reg():
    f_data = reader(file_path="data/users.csv")
    user_data = reader(file_path="data/users.csv")
    email = input("Enter your email: ")
    for u_data in f_data:
        for user_d in user_data: 
            if u_data[1] == email or user_d[1] == email:
                print("This email already exists!")
                break 
    else:
        random_code = randint(1000, 9999)
        message_body = f"Saytda ro'yxatdan o'tish uchun tasdiqlash kodi: {random_code}"
        
        threading.Thread(target=email_sender, args=(email, message_body)).start()
        verification_code = int(input("Enter verification code (we send it to your email):"))
        while verification_code != random_code:
            verification_code = input("Enter verification code (we send is to your email): ")

        id = generate_id("data/teachers.csv")
        fullname = input("Enter your fullname: ")
        created_at = datetime.now()
        active = 0
        t_data = [id,email,fullname,created_at,active]

        writer(file_path="data/teachers.csv", data=t_data, mode="a")
        print("Saytimizda o'qituvchi sifatida muvoffaqiyatli ro'yxatdan o'tdingiz!")




def sign_in():
    u_data = reader(file_path="data/users.csv")
    t_data = reader(file_path="data/teachers.csv")
    email = input("Enter your email: ")
    for data in u_data:
        if data[1] == email:
            data[-1] = 1
            writer(file_path="data/users.csv", data=u_data)
            return "user"
    for t1_data in t_data:
        if t1_data[1] == email:
            t1_data[-1] = 1
            writer(file_path="data/teachers.csv", data=t_data)
            return "teacher"
        




    