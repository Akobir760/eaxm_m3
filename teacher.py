from filemanager import reader, writer, generate_id, is_active
from datetime import datetime


def add_course():
    course_id = generate_id(file_path="data/courses.csv")
    name = input("Enter course name: ")
    price = int(input("Enter course price: "))
    created_at = datetime.now()
    t_id = is_active(file_path1="data/teachers.csv")
    course_data = [course_id,name,price,t_id,created_at]
    writer(file_path="data/courses.csv", data=course_data, mode="a")
    print("Course is added!")


def change_price():
    c_data = reader(file_path="data/courses.csv")
    id = int(input("Enter course's id: "))
    n_price = int(input("Enter new price: "))
    for data in c_data:
        if int(data[0]) == id:
            data[2] = n_price

    writer(file_path="data/courses.csv", data=c_data)
    print("Price is update!")


def course_users():
    u_file = reader(file_path="data/users.csv")
    c_id = int(input("Enter course id: "))
    for row in u_file:
        if int(row[4]) == c_id:
            print(f"User id: {row[0]}, Full name: {row[3]}, Email: {row[1]}, Registered at: {row[-1]}")




def see_all_messages():
    m_file = reader(file_path="data/messages.csv")
    active_user = is_active(file_path1="data/teachers.csv")

    for row in m_file:
        if row[2] == active_user:
            print(f" From {row[1]}: {row[3]}")
            row[-2] = 1
    writer(file_path="data/messages.csv", data=m_file)


def see_new_messages():
    f_data = reader(file_path="data/messages.csv")
    active_user = is_active(file_path1="data/teachers.csv")

    for row in f_data:
        if row[2] == active_user and  int(row[-2]) == 0:
            print(f" From {row[1]}: {row[3]}")
            row[-2] == 1
    writer(file_path="data/messages.csv", data=f_data)



def see_all_users():
    u_file = reader(file_path="data/users.csv")
    for row in u_file:
        print(f"User id: {row[0]}, Gmail: {row[1]}, Full name: {row[3]}, Course id: {row[4]}, Registered at: {row[5]}")



