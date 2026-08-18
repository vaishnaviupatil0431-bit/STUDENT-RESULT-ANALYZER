import numpy as np
import pandas as pd

FILE_NAME = "student_data.csv"

# Calculate Grade
def calculate_grade(percentage):
    if percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"

# Calculate Result

def calculate_result(marks):
    marks = np.array(marks)

    total = np.sum(marks)
    percentage = np.mean(marks)
    grade = calculate_grade(percentage)

    if np.all(marks >= 40):
        result = "Pass"
    else:
        result = "Fail"

    return total, percentage, grade, result

# Add Student

def add_student(name, roll_no, marks):

    total, percentage, grade, result = calculate_result(marks)

    new_student = pd.DataFrame([{
        "Name": name,
        "Roll No": roll_no,
        "Python": marks[0],
        "SQL": marks[1],
        "React": marks[2],
        "Data Structure": marks[3],
        "Machine Learning": marks[4],
        "Total": total,
        "Percentage": round(percentage, 2),
        "Grade": grade,
        "Result": result
    }])

    try:
        old_data = pd.read_csv(FILE_NAME)

        # Check duplicate roll number
        if roll_no in old_data["Roll No"].astype(str).values:
            return False, "Roll number already exists!"

        updated_data = pd.concat(
            [old_data, new_student],
            ignore_index=True
        )

    except (FileNotFoundError, pd.errors.EmptyDataError):
        updated_data = new_student

    updated_data.to_csv(FILE_NAME, index=False)

    return True, "Student added successfully!"

# View Students

def get_students():

    try:
        students = pd.read_csv(FILE_NAME)

        if students.empty:
            return None

        return students

    except (FileNotFoundError, pd.errors.EmptyDataError):
        return None

# Update Student

def update_student(roll_no, marks):

    try:
        students = pd.read_csv(FILE_NAME)

        student_index = students[
            students["Roll No"].astype(str) == str(roll_no)
        ].index

        if len(student_index) == 0:
            return False, "Student not found!"

        total, percentage, grade, result = calculate_result(marks)

        students.loc[student_index, "Python"] = marks[0]
        students.loc[student_index, "SQL"] = marks[1]
        students.loc[student_index, "React"] = marks[2]
        students.loc[student_index, "Data Structure"] = marks[3]
        students.loc[student_index, "Machine Learning"] = marks[4]

        students.loc[student_index, "Total"] = total
        students.loc[student_index, "Percentage"] = round(percentage, 2)
        students.loc[student_index, "Grade"] = grade
        students.loc[student_index, "Result"] = result

        students.to_csv(FILE_NAME, index=False)

        return True, "Student updated successfully!"

    except (FileNotFoundError, pd.errors.EmptyDataError):
        return False, "No student records found."

# Delete Student

def delete_student(roll_no):

    try:
        students = pd.read_csv(FILE_NAME)

        if roll_no not in students["Roll No"].astype(str).values:
            return False, "Student not found!"

        students = students[
            students["Roll No"].astype(str) != str(roll_no)
        ]

        students.to_csv(FILE_NAME, index=False)

        return True, "Student deleted successfully!"

    except (FileNotFoundError, pd.errors.EmptyDataError):
        return False, "No student records found."