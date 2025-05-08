from filemanager import reader, writer,  generate_id
from datetime import datetime

def sent_message():
    pass
#     u_id = int(input("Enter your id: "))
#     u_mess = input("Enter your message: ")
#     file_data = reader("data/users.csv")

#     m_id = generate_id(file_path="data/messages.csv")
#     sented_at = datetime.now()
#     for data in file_data:
#         if int(data[0]) == u_id:
#             u_email_sender(s_email=data[1], app_p=data[2], m_body=u_mess)
#             m_data = [m_id,data[1],data[0],u_mess,0,sented_at]
#             writer(file_path="data/messages.csv", data=m_data, mode="a")


def see_my_course():
    c_file = reader(file_path="data/courses.csv")
    u_file = reader(file_path="data/users.csv")
    u_id = int(input("Enter your id: "))
    for user in u_file:
        if int(user[0]) == u_id:
            for course in c_file:
                if int(user[4]) == int(course[0]):
                    print(f"Course name: {course[1]}, Price: {course[2]}")



def buy_course():
    file_id = generate_id(file_path="data/payments.csv")
    u_id = int(input("Enter your id: "))
    c_id = int(input("Enter course id: "))
    karta = int(input("Enter your credit card number: "))
    
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


def my_payments():
    u_id = int(input("Enter your id: "))
    file_data = reader(file_path="data/payments.csv")
    for data in file_data:
        if int(data[1]) == u_id:
            print(f"Course id: {data[2]}, Value: {data[3]}, Payed at {data[-1]}")
    


