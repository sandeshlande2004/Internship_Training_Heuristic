import tkinter as tk
from database import update_student
from tkinter import messagebox
from database import validate_student_id

def validate_student_page():
    global validate_student_page
    validate_student_page = tk.Tk()
    validate_student_page.title('Validate Student')
    validate_student_page.geometry('300x200')
    
    id_label = tk.Label(validate_student_page, text='ID:', font=('bold', 14))
    id_label.place(x=10, y=50)
    id_entry = tk.Entry(validate_student_page, width=30)
    id_entry.place(x=50, y=50)
    
    validate_button = tk.Button(validate_student_page, text='Validate', width=25, height=2, bg='green', command=lambda: val_student(id_entry.get()))
    validate_button.place(x=10, y=100)
    
    validate_student_page.mainloop()
    
def val_student(id):
    if id == "":
        messagebox.showerror('Error', 'Please enter student ID')
    else:
        if validate_student_id(id):
            validate_student_page.destroy()
            show_update_student_page()
        else:
            messagebox.showerror('Error', 'Student not found')
            validate_student_page.destroy()
            return


def show_update_student_page():
    global root
    root = tk.Tk()
    root.title('Update Student')
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
    
    update_button = tk.Button(root, text='Update student', width=25, height=2, bg='green', command=lambda: new_student(id_entry.get(), name_entry.get(), age_entry.get(), course_entry.get(), contact_entry.get()))
    update_button.place(x=100, y=300)
    
    root.mainloop()

def new_student(id, name, age, course, contact):
    if id == "" or name == "" or age == "" or course == "" or contact == "":
        messagebox.showerror('Error', 'All fields are required')
        return
    else:
        update_student(id, name, age, course, contact)
        messagebox.showinfo('Success', 'Student updated successfully')
        root.destroy()

