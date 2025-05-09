from teacher import add_course, change_price, course_users, see_all_users, see_all_messages, see_new_messages
from auth import user_reg, teach_reg, sign_in
from filemanager import  reader, log_out
from user import see_my_course, sent_message, buy_course, my_payments


def main():
    print("""
1. Register teacher
2. Register user
3. Sign in""")
    choice = int(input("Enter your choice number: "))
    if choice == 1:
        teach_reg()
        return main()
    elif choice == 2:
        user_reg()
        return main()
    elif choice == 3:
        res = sign_in()
        if res == "teacher":
            return teacher_menu()
        
        elif res == "user":
            return user_menu()
        else:
            print("You need to register!")
            return main()
    else:
        print("Invalid choice!")
        return main()
    

m_file = reader(file_path="data/messages.csv")


def teacher_menu():
    
    print(f"""
1. Add new course
2. Change course's price
3. See course's users
4. See all messages ({len(m_file)})
5. See new messages 
6. Exit""")
    choice = int(input("Enter your choice number: "))
    if choice == 1:
        add_course()
    elif choice == 2:
        change_price()
    elif choice == 3:
        course_users()
    elif choice == 4:
        see_all_messages()
    elif choice == 5:
        see_new_messages()
    elif choice == 6:
        print("Exiting...")
        log_out(file="data/teachers.csv")
        return main() 
    else:
        print("Invalid choice!")
    return teacher_menu()


def user_menu():
    print("""
1. Buy course
2. See my courses
3. Sent message
4. My payments
5. Exit""")
    u_choice = int(input("Enter your  choice number: "))
    if u_choice == 1:
        buy_course()
    elif u_choice == 2:
        see_my_course()
    elif u_choice == 3:
        sent_message()
    elif u_choice == 4:
        my_payments()
    elif u_choice == 5:
        print("Exiting...")
        log_out(file="data/users.csv")
        return main()
    else:
        print("Invalid choice!")
    return user_menu()    


if __name__ == "__main__":
    log_out(file="data/users.csv")
    log_out(file="data/teachers.csv")
    main()