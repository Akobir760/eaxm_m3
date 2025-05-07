from filemanager import reader, writer, generate_id
from datetime import datetime


def add_course():
    course_id = generate_id(file_path="data/courses.csv")
    name = input("Enter course name: ")
    price = int(input("Enterr course price: "))
    created_at = datetime.now()
    course_data = [course_id,name,price,created_at]
    writer(file_path="data/courses.csv", data=course_data, mode="a")
    print("Course is added!")


def chenge_price():
    c_data = reader(file_path="data/courses.csv")
    id = int(input("Enter course's id: "))
    n_price = int(input("Enter new price: "))
    for data in c_data:
        if int(data[0]) == id:
            data[2] = n_price

    writer(file_path="data/courses.csv", data=c_data)
    print("Price is update!")



