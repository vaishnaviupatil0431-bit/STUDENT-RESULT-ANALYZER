import numpy as np
from numpy import ma
import pandas as pd

FILE_NAME = "student_data.csv"

print("=" * 50)
print("  STUDENT RESULT ANALYZER")
print("=" * 50)

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
if percentage >= 80 and percentage <= 100:
    grade = "A"
elif percentage >= 70 and percentage < 80:
    grade = "B"
elif percentage >= 60 and percentage < 70:
    grade = "C"
elif percentage >= 40 and percentage < 60:
    grade = "D"
else:
    grade = "F"

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

# display final result
print("\n" + "=" * 50)
print("  Student Result")
print("=" * 50)

# display student details and result
print(f"Name : {name}")
print(f"Roll No : {roll_no}")
print(f"Total Marks : {total}")
print(f"Percentage : {round(percentage, 2)}")
print(f"Grade : {grade}")
print(f"Result : {result}")

# show success message
print("\nStudent record saved successfully!😄")