import numpy as np
import pandas as pd

FILE_NAME = "student_data.csv"

# function to calculate grade
def calculate_grade(percentage):
   if percentage >= 80 and percentage <= 100:
           return "A"
   elif percentage >= 70 and percentage < 80:
           return "B"
   elif percentage >= 60 and percentage < 70:
           return "C"
   elif percentage >= 40 and percentage < 60:
           return "D"
   else:
           return "F"

# function to add a student
def add_student():
    print("\n---- ADD STUDENT ----")

    # student details
    name = input("Enter Student Name : ")
    roll_no = input("Enter roll number : ")

# subject marks
    python_marks = float(input("Enter Python marks : "))
    sql_marks = float(input("Enter SQL marks : "))
    react_marks = float(input("Enter React marks :"))
    DS_marks = float(input("Enter Data Structure marks :"))
    ML_marks = float(input("Enter Machine Learning marks :"))

# store marks
    marks = np.array([
        python_marks,
        sql_marks,
        react_marks,
        DS_marks,
        ML_marks
    ])

# calculate total & percentage
    total = np.sum(marks)
    percentage = np.mean(marks)


# calculate grade
    grade = calculate_grade(percentage)

    # check whether student passed all subjects
    if np.all(marks >= 40):
        result = "Pass"
    else:
     result = "Fail"

    # for new student create a pandas table
    new_student = pd.DataFrame(
     [{
         "Name" : name,
         "Roll No" : roll_no,
         "Python" : python_marks,
         "SQL" : sql_marks,
         "React" : react_marks,
         "Data Structure" : DS_marks,
         "Machine Learning" : ML_marks,
         "Total" : total,
         "Percentage" : round(percentage, 2),
         "Grade" : grade,
         "Result" : result
     }]
)

    # Read old data and add new student
    try:
     old_data = pd.read_csv(FILE_NAME)

     updated_data = pd.concat([old_data,new_student],
                             ignore_index=True)
    
# create new data if csv is missing or empty
    except(FileNotFoundError, pd.errors.EmptyDataError):
        updated_data = new_student

# save all student records in csv file
    updated_data.to_csv(FILE_NAME, index=False)

# show success message
    print("\nStudent record saved successfully!😄")

# function to view all students
def view_students():
    print("\n----VIEW ALL STUDENT RECORDS----")

    try:
          # read student records from csv
          students = pd.read_csv(FILE_NAME)
    
          if students.empty:
             print("\nNo student record found.")
    
          else:
             print("\n" + "=" * 50)
             print(" All student records")
             print("=" * 50)
    
             print(students.to_string(index=False))
    
    except(FileNotFoundError, pd.errors.EmptyDataError):
            print("\nNo student record found.")


# function to update a student
def update_student():
     print("\n----UPDATE STUDENT RECORD----")

     try:
        students = pd.read_csv(FILE_NAME)

        roll_no = input("Enter Roll Number to update: ")

        # Check whether the roll number exists
        if roll_no not in students["Roll No"].astype(str).values:
            print("Student not found.")
            return

        # Take new marks
        python_marks = float(input("Enter new Python marks: "))
        sql_marks = float(input("Enter new SQL marks: "))
        react_marks = float(input("Enter new React marks: "))
        ds_marks = float(input("Enter new Data Structure marks: "))
        ml_marks = float(input("Enter new Machine Learning marks: "))

        # Store marks in NumPy array
        marks = np.array([
            python_marks,
            sql_marks,
            react_marks,
            ds_marks,
            ml_marks
        ])

        # Recalculate result
        total = np.sum(marks)
        percentage = np.mean(marks)
        grade = calculate_grade(percentage)

        if np.all(marks >= 40):
            result = "Pass"
        else:
            result = "Fail"

        # Find the student
        student_index = students[
            students["Roll No"].astype(str) == roll_no
        ].index

        # Update marks
        students.loc[student_index, "Python"] = python_marks
        students.loc[student_index, "SQL"] = sql_marks
        students.loc[student_index, "React"] = react_marks
        students.loc[student_index, "Data Structure"] = ds_marks
        students.loc[student_index, "Machine Learning"] = ml_marks
        students.loc[student_index, "Total"] = total
        students.loc[student_index, "Percentage"] = round(
            percentage, 2
        )
        students.loc[student_index, "Grade"] = grade
        students.loc[student_index, "Result"] = result

        # Save updated data
        students.to_csv(FILE_NAME, index=False)

        print("\nStudent record updated successfully! ✅")

     except (FileNotFoundError, pd.errors.EmptyDataError):
        print("No student records found.")

# Function to delete a student
def delete_student():

    print("\n----- DELETE STUDENT -----")

    try:
        students = pd.read_csv(FILE_NAME)

        roll_no = input("Enter Roll Number to delete: ")

        # Check whether student exists
        if roll_no not in students["Roll No"].astype(str).values:
            print("Student not found.")
            return

        # Remove student
        students = students[
            students["Roll No"].astype(str) != roll_no
        ]

        # Save remaining students
        students.to_csv(FILE_NAME, index=False)

        print("\nStudent record deleted successfully! 🗑️")

    except (FileNotFoundError, pd.errors.EmptyDataError):
        print("No student records found.")

# Main program loop
while True:

    print("\n" + "=" * 50)
    print("       STUDENT RESULT ANALYZER")
    print("=" * 50)

    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("\nThank you for using Student Result Analyzer! 👋")
        break

    else:
        print("\nInvalid choice! Please enter a number from 1 to 5.")