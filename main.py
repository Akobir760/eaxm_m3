from auth import user_reg, teach_reg, sign_in


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
    

def teacher_menu():
    print("""
1. Add new course
2. Change course
3. See course's users
4. See messages
5. Exit""")
    choice = int(input("Enter your choice number: "))
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        print("Exiting...")
        return main() 
    else:
        print("Invalid choice!")
    return teacher_menu()


def user_menu():
    pass


if __name__ == "__main__":
    main()