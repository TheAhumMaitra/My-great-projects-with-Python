def students_marks_tracker():
    # Dictionary to store students' marks
    students = {
        "John Smith": 100,
        "Alice Johnson": 95,
        "Bob Brown": 88
    }

    # Admin credentials
    Password_dict = {"Admin_Name": "1235"}  # Ensure passwords are stored as strings and view the admin name
    Name_list = ["Admin_Name"] #Admin Name List

    # Get admin credentials
    Name = input("Enter admin name: ") #Admin Name input
    Password = input("Enter password: ") #Admin Password input

    #Print home screen 
    print("Welcome to (School Name)\n\n")
    print("Enter details \n")

    # Check credentials
    if Name in Password_dict and Password == Password_dict[Name]:
        print(f"Hello Admin - {Name}")

        # Student search
        Search = input("Enter a student name: ")
        print("\nExample: 'John Smith' ")

        # Get student marks
        Find = students.get(Search, "Not found")

        if Find != "Not found":
            print(f"The student's previous year grand total is {Find}")
        else:
            print("Student not found.")
    else:
        print("Invalid credentials. Access denied.")

# Run the function
students_marks_tracker()
