from filemanager import reader, writer, generate_id, email_sender
from datetime import datetime

t_username = "teacher"
t_password = "teacher"


def user_reg():
    f_data = reader(file_path="data/users.csv")
    email = input("Enter your email: ")
    for u_data in f_data:
        if u_data[1] == email:
            print("This email already exists!")
            break 
    else:

        id = generate_id(file_path="data/users.csv")
        password= input("Enter your app password: ")
        full_name = input("Enter your fullname: ")
        course_id = int(input("Enter course id: "))
        created_at = datetime.now()
        message_body = "Saytimizda muvoffaqiyatli ro'yxatdan o'tdingiz!"
        data = [id,email,password,full_name,course_id,created_at]
        writer(file_path="data/users.csv", data=data, mode="a")
        print("Saytimizda muvoffaqiyatli ro'yxatdan o'tdingiz!")
        email_sender(r_email=email, m_body=message_body)


def teach_reg():
    username = input("Enter username: ")
    password = input("Enter passwod: ")
    t_file = reader(file_path="data/teachers.csv")
    if username == t_username and password == t_password:
        email = input("Enter your email: ")
        for row in t_file:
            if row[1] == email:
                print("This email already exists!")
                break
        else:
                
            id = generate_id("data/teachers.csv")
            e_password = input("Enter your app password: ")
            fullname = input("Enter your fullname: ")
            created_at = datetime.now()
            t_data = [id,email,e_password,fullname,created_at]
            message_body = "Saytimizda o'qituvchi sifatida muvoffaqiyatli ro'yxatdan o'tdingiz!"

            writer(file_path="data/teachers.csv", data=t_data, mode="a")
            print("Saytimizda o'qituvchi sifatida muvoffaqiyatli ro'yxatdan o'tdingiz!")
            email_sender(r_email=email, m_body=message_body)

    else:
        print("Invalid username or passwors!")


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

    