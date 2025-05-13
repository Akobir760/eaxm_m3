from filemanager import reader, writer,  generate_id, is_active, email_sender
from datetime import datetime
import threading
def sent_message():
    
    u_id = is_active(file_path1="data/users.csv")

    file_data = reader("data/users.csv")
    teacher_file = reader(file_path="data/teachers.csv")

    """teacher idni user qaysi kursni sotib olganiga qarab aniqlamoqchi edim,
    ammo user 2 ta kurs sotib olgan bo'lsa va ularga 2 ta teacher dars o'tadigan bo'lsa
    xabar boshqa teacherga yoki ikkalasiga ham borishi mumkin shuning uchun userdan so'radim!"""

    courses_list = []
    t_file = reader(file_path="data/teachers.csv")
    c_file = reader(file_path="data/courses.csv")
    p_file = reader(file_path="data/payments.csv")
    u_id = is_active(file_path1="data/users.csv")
    for user in p_file:
        if user[1] == u_id:
            for course in c_file:
                if course[1] not in [c[1] for c in courses_list] and int(user[2]) == int(course[0]):
                    courses_list.append(course)

    for course in courses_list:
        for teacher in t_file:
            if course[3] == teacher[0]:
                print(f"Teacher id: {teacher[0]}, Teacher name: {teacher[2]}, Course name: {course[1]}")

    teacher_id = input("Enter receiver teacher id: ")
    u_mess = input("Enter your message: ")

    for teacher in teacher_file:
        if teacher[0] == teacher_id:
            m_id = generate_id(file_path="data/messages.csv")
            sended_at = datetime.now()
            for data in file_data:
                if data[0] == u_id:
                    threading.Thread(target=email_sender, args=(teacher[1],u_mess )).start()
                    m_data = [m_id,data[1],teacher_id,u_mess,0,sended_at]
                    writer(file_path="data/messages.csv", data=m_data, mode="a")
                    print("Message is send!")
        break
    else:
        print("Invalid teacher id!")


def see_my_course():
    courses_list = []
    c_file = reader(file_path="data/courses.csv")
    p_file = reader(file_path="data/payments.csv")
    u_id = is_active(file_path1="data/users.csv")
    for user in p_file:
        if user[1] == u_id:
            for course in c_file:
                if course[1] not in [c[1] for c in courses_list] and int(user[2]) == int(course[0]):
                    courses_list.append(course)
    
    for c in courses_list:
        print(f"Course name: {c[1]}, Price: {c[2]}")
    
    courses_list.clear()



def buy_course():
    try:
        file_id = generate_id(file_path="data/payments.csv")
        u_id = is_active(file_path1="data/users.csv")
        teachers = reader(file_path="data/teachers.csv")
        c_file = reader(file_path="data/courses.csv")
        for course in c_file:
            for teacher in teachers:
                if course[3] == teacher[0]:
                    print(f"Course id: {course[0]}, Name: {course[1]}, Price: {course[2]}, Teacher name: {teacher[2]}")

        c_id = int(input("Enter course id: "))
        karta = int(input("Enter your credit card number: "))
        valid = input("Enter card validity period: ")

        while len(str(karta)) != 16:
            print("Invalid card!")
            return buy_course()
        
        
        u_file = reader(file_path="data/users.csv")
        for user in u_file:
            if user[0] == u_id:
                user[4] = c_id
        
        writer(file_path="data/users.csv", data=u_file)
        
        value = int(input("Enter payment value: "))
        payed_at = datetime.now()
        payment_data = [file_id,u_id,c_id,value,payed_at]
        writer(file_path="data/payments.csv", data=payment_data, mode="a")
        print("Thanks for payment!")
    except BaseException as exc:
        print(exc)

def my_payments():
    u_id = is_active(file_path1="data/users.csv")
    file_data = reader(file_path="data/payments.csv")
    for data in file_data:
        if data[1] == u_id:
            print(f"Course id: {data[2]}, Value: {data[3]}, Payed at {data[-1]}")
    


