import tkinter as tk
from database import search_student
from tkinter import messagebox

def show_search_student_page():
    global root
    root = tk.Tk()
    root.title('Search Student')
    root.geometry('400x400')
    root.configure(bg='light blue')
    
    name_label = tk.Label(root, text='Name:', font=('bold', 14), bg='light blue')
    name_label.place(x=50, y=50)
    name_entry = tk.Entry(root, width=30)
    name_entry.place(x=150, y=50)
    
    search_button = tk.Button(root, text='Search student', width=25, height=2, bg='green', command=lambda: new_student(name_entry.get()))
    search_button.place(x=100, y=100)
    
    root.mainloop()
    
def new_student(name):
    student = search_student(name)
    if student:
        messagebox.showinfo('Student found', student)
        root.destroy()
    else:
        messagebox.showerror('Error', 'Student not found')
        return
    