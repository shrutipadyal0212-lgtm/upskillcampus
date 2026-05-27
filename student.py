students = {}

while True:
    print("\n1.Add Student")
    print("2.View Students")
    print("3.Search Student")
    print("4.Delete Student")
    print("5.Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        students[roll] = name
        print("Student Added Successfully")

    elif choice == '2':
        print("\nStudent Records")
        for roll, name in students.items():
            print(roll, ":", name)

    elif choice == '3':
        roll = input("Enter Roll No: ")
        if roll in students:
            print("Name:", students[roll])
        else:
            print("Student Not Found")

    elif choice == '4':
        roll = input("Enter Roll No: ")
        if roll in students:
            del students[roll]
            print("Student Deleted")
        else:
            print("Student Not Found")

    elif choice == '5':
        break

    else:
        print("Invalid Choice")