from filemanager import reader, writer, generate_id, email_sender
from datetime import datetime




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
        message_body = "Tasdiqlash kodi: 1234"
        email_sender(r_email=email, m_body=message_body)

        verification_code = int(input("Enter verification code (we send is to your email): "))
        
        while verification_code != 1234:
            verification_code = int(input("Enter verification code (we send is to your email): "))

        full_name = input("Enter your fullname: ")

        created_at = datetime.now()
        data = [id,email,full_name,created_at]
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
            
        message_body = "Saytda ro'yxatdan o'tish uchun tasdiqlash kodi: 2345"
        
        email_sender(r_email=email, m_body=message_body)
        verification_code = int(input("Enter verification code (we send it to your email):"))
        while verification_code != 2345:
            verification_code = int(input("Enter verification code (we send is to your email): "))

        id = generate_id("data/teachers.csv")
        fullname = input("Enter your fullname: ")
        created_at = datetime.now()
        t_data = [id,email,fullname,created_at]

        writer(file_path="data/teachers.csv", data=t_data, mode="a")
        print("Saytimizda o'qituvchi sifatida muvoffaqiyatli ro'yxatdan o'tdingiz!")




def sign_in():
    u_data = reader(file_path="data/users.csv")
    t_data = reader(file_path="data/teachers.csv")
    email = input("Enter your email: ")
    for data in u_data:
        if data[1] == email:
            return "user"
    for t1_data in t_data:
        if t1_data[1] == email:
            return "teacher"

    