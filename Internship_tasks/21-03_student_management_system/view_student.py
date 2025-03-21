import sqlite3
import tkinter as tk
from tkinter import ttk
import database

def show_view_student_page():
    def view_students():
        for row in student_table.get_children():
            student_table.delete(row)
        conn = sqlite3.connect("student_database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students_db")
        for row in cursor.fetchall():
            student_table.insert("", tk.END, values=row)
        conn.close()


    root = tk.Tk()
    root.title("View Students")
    root.geometry("1050x300")

    columns = ("ID", "Name", "Age", "Course", "Contact")
    student_table = ttk.Treeview(root, columns=columns, show="headings")
    for col in columns:
        student_table.heading(col, text=col)
    student_table.pack(expand=True, fill="both")

    view_students()
    root.mainloop()
