import tkinter as tk

window = tk.Tk()

window.title("Student Result Analyzer")

window.geometry("700x500")

heading = tk.Label(window, text="STUDENT RESULT ANALYZER",font=("Arial", 20, "bold"))
heading.pack(pady=30)

message = tk.Label(window,text="Welcome to the Student Result Analyzer",font=("Arial", 14))
message.pack(pady=20)

window.mainloop()
