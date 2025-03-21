import tkinter as tk
from database import delete_student
from tkinter import messagebox
from database import validate_student_name

def show_delete_student_page():
    global root
    root = tk.Tk()
    root.title('Delete Student')
    root.geometry('400x400')
    root.configure(bg='light blue')
    
    name_label = tk.Label(root, text='Name:', font=('bold', 14), bg='light blue')
    name_label.place(x=50, y=50)
    name_entry = tk.Entry(root, width=30)
    name_entry.place(x=150, y=50)
    
    delete_button = tk.Button(root, text='Delete student', width=25, height=2, bg='green', command=lambda: new_student(name_entry.get()))
    delete_button.place(x=100, y=100)
    
    root.mainloop()

def new_student(name):
    if name == "":
        messagebox.showerror("Error", "Please enter student Name")
        return
    else:
        if validate_student_name(name):
            delete_student(name)
            messagebox.showinfo('Success', 'Student deleted successfully')
            root.destroy()
        else:
            messagebox.showerror('Error', 'Student not found')
            root.destroy()
            return