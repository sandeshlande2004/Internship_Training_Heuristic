import tkinter as tk
from database import add_student
from tkinter import messagebox

def show_add_student_page():
    global root
    root = tk.Tk()
    root.title('Add Student')
    root.geometry('400x400')
    root.configure(bg='light blue')
    
    id_label = tk.Label(root, text='ID:', font=('bold', 14), bg='light blue')
    id_label.place(x=50, y=50)
    id_entry = tk.Entry(root, width=30)
    id_entry.place(x=150, y=50)
    
    name_label = tk.Label(root, text='Name:', font=('bold', 14), bg='light blue')
    name_label.place(x=50, y=100)
    name_entry = tk.Entry(root, width=30)
    name_entry.place(x=150, y=100)
    
    age_label = tk.Label(root, text='Age:', font=('bold', 14), bg='light blue')
    age_label.place(x=50, y=150)
    age_entry = tk.Entry(root, width=30)
    age_entry.place(x=150, y=150)
    
    course_label = tk.Label(root, text='Course:', font=('bold', 14), bg='light blue')
    course_label.place(x=50, y=200)
    course_entry = tk.Entry(root, width=30)
    course_entry.place(x=150, y=200)
    
    contact_label = tk.Label(root, text='Contact:', font=('bold', 14), bg='light blue')
    contact_label.place(x=50, y=250)
    contact_entry = tk.Entry(root, width=30)
    contact_entry.place(x=150, y=250)
    
    add_button = tk.Button(root, text='Add student', width=25, height=2, bg='green',  command=lambda: new_student(id_entry.get(), name_entry.get(), age_entry.get(), course_entry.get(), contact_entry.get()))
    add_button.place(x=100, y=300)
    
    root.mainloop()

def new_student(id, name , age, course, contact):
    
    if id == "" or name == "" or age == "" or course == "" or contact == "":
        messagebox.showerror('Error', 'All fields are required')
        return
    
    if add_student(id, name, age, course, contact):
        messagebox.showinfo('Success', 'Student added successfully')
        root.destroy()
    else:
        messagebox.showerror('Error', 'Student not added')
        return
