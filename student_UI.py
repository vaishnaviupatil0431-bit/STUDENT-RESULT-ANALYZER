import tkinter as tk
from tkinter import messagebox, ttk

from main import (
    add_student,
    get_students,
    update_student,
    delete_student
)

# MAIN WINDOW

window = tk.Tk()

window.title("Student Result Analyzer")
window.geometry("1100x750")

window.resizable(False, False)

# HEADING

heading = tk.Label(
    window,
    text="STUDENT RESULT ANALYZER",
    font=("Arial", 24, "bold")
)

heading.pack(pady=20)

# FORM FRAME

form_frame = tk.Frame(window)

form_frame.pack(pady=5)

# STUDENT NAME

tk.Label(
    form_frame,
    text="Student Name:",
    font=("Arial", 12)
).grid(row=0, column=0, padx=10, pady=8, sticky="w")

name_entry = tk.Entry(
    form_frame,
    width=25,
    font=("Arial", 12)
)

name_entry.grid(row=0, column=1, padx=10, pady=8)

# ROLL NUMBER

tk.Label(
    form_frame,
    text="Roll Number:",
    font=("Arial", 12)
).grid(row=0, column=2, padx=10, pady=8, sticky="w")

roll_entry = tk.Entry(
    form_frame,
    width=25,
    font=("Arial", 12)
)

roll_entry.grid(row=0, column=3, padx=10, pady=8)

# PYTHON MARKS

tk.Label(
    form_frame,
    text="Python:",
    font=("Arial", 12)
).grid(row=1, column=0, padx=10, pady=8, sticky="w")

python_entry = tk.Entry(
    form_frame,
    width=25,
    font=("Arial", 12)
)

python_entry.grid(row=1, column=1, padx=10, pady=8)

# SQL MARKS

tk.Label(
    form_frame,
    text="SQL:",
    font=("Arial", 12)
).grid(row=1, column=2, padx=10, pady=8, sticky="w")

sql_entry = tk.Entry(
    form_frame,
    width=25,
    font=("Arial", 12)
)

sql_entry.grid(row=1, column=3, padx=10, pady=8)

# REACT MARKS

tk.Label(
    form_frame,
    text="React:",
    font=("Arial", 12)
).grid(row=2, column=0, padx=10, pady=8, sticky="w")

react_entry = tk.Entry(
    form_frame,
    width=25,
    font=("Arial", 12)
)

react_entry.grid(row=2, column=1, padx=10, pady=8)

# DATA STRUCTURE

tk.Label(
    form_frame,
    text="Data Structure:",
    font=("Arial", 12)
).grid(row=2, column=2, padx=10, pady=8, sticky="w")

ds_entry = tk.Entry(
    form_frame,
    width=25,
    font=("Arial", 12)
)

ds_entry.grid(row=2, column=3, padx=10, pady=8)

# MACHINE LEARNING

tk.Label(
    form_frame,
    text="Machine Learning:",
    font=("Arial", 12)
).grid(row=3, column=0, padx=10, pady=8, sticky="w")

ml_entry = tk.Entry(
    form_frame,
    width=25,
    font=("Arial", 12)
)

ml_entry.grid(row=3, column=1, padx=10, pady=8)

# GET MARKS

def get_marks():

    try:

        marks = [
            float(python_entry.get()),
            float(sql_entry.get()),
            float(react_entry.get()),
            float(ds_entry.get()),
            float(ml_entry.get())
        ]

        # Check marks range
        for mark in marks:
            if mark < 0 or mark > 100:
                messagebox.showerror(
                    "Invalid Marks",
                    "Marks must be between 0 and 100."
                )
                return None

        return marks

    except ValueError:

        messagebox.showerror(
            "Invalid Input",
            "Please enter valid marks."
        )

        return None

# CLEAR FIELDS

def clear_fields():

    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)

    python_entry.delete(0, tk.END)
    sql_entry.delete(0, tk.END)
    react_entry.delete(0, tk.END)
    ds_entry.delete(0, tk.END)
    ml_entry.delete(0, tk.END)

# ADD STUDENT BUTTON

def add_student_gui():

    name = name_entry.get().strip()
    roll_no = roll_entry.get().strip()

    if name == "" or roll_no == "":
        messagebox.showwarning(
            "Missing Information",
            "Please enter student name and roll number."
        )
        return

    marks = get_marks()

    if marks is None:
        return

    success, message = add_student(
        name,
        roll_no,
        marks
    )

    if success:

        messagebox.showinfo(
            "Success",
            message
        )

        clear_fields()
        view_students_gui()

    else:

        messagebox.showerror(
            "Error",
            message
        )

# VIEW STUDENTS

def view_students_gui():

    # Remove old records
    for item in student_table.get_children():
        student_table.delete(item)

    students = get_students()

    if students is None:
        return

    for _, student in students.iterrows():

        student_table.insert(
            "",
            tk.END,
            values=(
                student["Name"],
                student["Roll No"],
                student["Python"],
                student["SQL"],
                student["React"],
                student["Data Structure"],
                student["Machine Learning"],
                student["Total"],
                student["Percentage"],
                student["Grade"],
                student["Result"]
            )
        )

# SELECT STUDENT FROM TABLE

def select_student(event):

    selected = student_table.focus()

    if not selected:
        return

    values = student_table.item(
        selected,
        "values"
    )

    if not values:
        return

    clear_fields()

    name_entry.insert(0, values[0])
    roll_entry.insert(0, values[1])

    python_entry.insert(0, values[2])
    sql_entry.insert(0, values[3])
    react_entry.insert(0, values[4])
    ds_entry.insert(0, values[5])
    ml_entry.insert(0, values[6])


# ==========================================
# UPDATE STUDENT
# ==========================================

def update_student_gui():

    roll_no = roll_entry.get().strip()

    if roll_no == "":
        messagebox.showwarning(
            "Missing Information",
            "Please enter roll number."
        )
        return

    marks = get_marks()

    if marks is None:
        return

    success, message = update_student(
        roll_no,
        marks
    )

    if success:

        messagebox.showinfo(
            "Success",
            message
        )

        clear_fields()
        view_students_gui()

    else:

        messagebox.showerror(
            "Error",
            message
        )


# ==========================================
# DELETE STUDENT
# ==========================================

def delete_student_gui():

    roll_no = roll_entry.get().strip()

    if roll_no == "":
        messagebox.showwarning(
            "Missing Information",
            "Enter roll number to delete."
        )
        return

    confirm = messagebox.askyesno(
        "Confirm Delete",
        "Are you sure you want to delete this student?"
    )

    if not confirm:
        return

    success, message = delete_student(
        roll_no
    )

    if success:

        messagebox.showinfo(
            "Success",
            message
        )

        clear_fields()
        view_students_gui()

    else:

        messagebox.showerror(
            "Error",
            message
        )


# ==========================================
# BUTTON FRAME
# ==========================================

button_frame = tk.Frame(window)

button_frame.pack(pady=15)


# ADD BUTTON

add_button = tk.Button(
    button_frame,
    text="ADD STUDENT",
    font=("Arial", 11, "bold"),
    width=15,
    command=add_student_gui
)

add_button.grid(
    row=0,
    column=0,
    padx=8
)


# VIEW BUTTON

view_button = tk.Button(
    button_frame,
    text="VIEW STUDENTS",
    font=("Arial", 11, "bold"),
    width=15,
    command=view_students_gui
)

view_button.grid(
    row=0,
    column=1,
    padx=8
)


# UPDATE BUTTON

update_button = tk.Button(
    button_frame,
    text="UPDATE",
    font=("Arial", 11, "bold"),
    width=15,
    command=update_student_gui
)

update_button.grid(
    row=0,
    column=2,
    padx=8
)


# DELETE BUTTON

delete_button = tk.Button(
    button_frame,
    text="DELETE",
    font=("Arial", 11, "bold"),
    width=15,
    command=delete_student_gui
)

delete_button.grid(
    row=0,
    column=3,
    padx=8
)


# CLEAR BUTTON

clear_button = tk.Button(
    button_frame,
    text="CLEAR",
    font=("Arial", 11, "bold"),
    width=15,
    command=clear_fields
)

clear_button.grid(
    row=0,
    column=4,
    padx=8
)

# TABLE FRAME

table_frame = tk.Frame(window)

table_frame.pack(
    padx=10,
    pady=10,
    fill="both",
    expand=True
)

# TABLE

columns = (
    "Name",
    "Roll No",
    "Python",
    "SQL",
    "React",
    "Data Structure",
    "Machine Learning",
    "Total",
    "Percentage",
    "Grade",
    "Result"
)

student_table = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings",
    height=12
)

# TABLE HEADINGS

for column in columns:

    student_table.heading(
        column,
        text=column
    )

    student_table.column(
        column,
        width=100,
        anchor="center"
    )


# Name column

student_table.column(
    "Name",
    width=130
)

student_table.column(
    "Data Structure",
    width=120
)

student_table.column(
    "Machine Learning",
    width=130
)

# SCROLLBAR

scrollbar = ttk.Scrollbar(
    table_frame,
    orient="horizontal",
    command=student_table.xview
)

student_table.configure(
    xscrollcommand=scrollbar.set
)


student_table.pack(
    fill="both",
    expand=True
)

scrollbar.pack(
    fill="x"
)

# CLICK TABLE ROW

student_table.bind(
    "<ButtonRelease-1>",
    select_student
)

# LOAD EXISTING DATA

view_students_gui()

# START GUI

window.mainloop()