def add_student():
    name = input("Enter student name:");
    roll_no = int(input("Enter roll number:"))
    branch = input("Enter branch:")
    marks = float(input("Enter marks:"))
    print("\nStudent Details")
    print("Name:", name)
    print("Roll Number:", roll_no)
    print("Branch:", branch)
    print("Marks:", marks)
                       
while True:
    print("\n==== STUDENT MANAGEMENT SYSTEM ====")
    print("1. Add Student")
    print("2. Exit")
    choice = input("Enter your choice:")
    if choice == "1":
       add_student()
    elif choice =="2":
        print("Thank you!")
        break
    else:
        print("Invalid choice")
