import tkinter as tk

window = tk.Tk()

window.title("Student Result Analyzer")

window.geometry("700x500")

# main heading
heading = tk.Label(window, text="STUDENT RESULT ANALYZER",font=("Arial", 20, "bold"))
heading.pack(pady=30)

# create a frame for input fields
form_frame = tk.Frame(window)
form_frame.pack(pady=10)

# student name
name_label = tk.Label(form_frame, text="Student Name :",font=("Arial",12))
name_label.grid(row=0,column=0,padx=10,pady=8,sticky="w")

name_entry = tk.Entry(form_frame,width=30,font=("Arial",12))
name_entry.grid(row=0,column=1,padx=10,pady=8)

# Roll Number


