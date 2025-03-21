import sqlite3
from tkinter import messagebox
import csv

def create_database():
    conn = sqlite3.connect('student_database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students_db(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        course TEXT NOT NULL,
        contact TEXT NOT NULL
    )''')
    conn.commit()
    conn.close()

def add_student(id, name, age, course, contact):
    conn = sqlite3.connect('student_database.db')
    c = conn.cursor()
    c.execute('''INSERT INTO students_db(id, name, age, course, contact) VALUES(?, ?, ?, ?, ?)''', (id, name, age, course, contact))
    conn.commit()
    conn.close()
    return True


def update_student(id, name, age, course, contact):
    conn = sqlite3.connect('student_database.db')
    c = conn.cursor()
    c.execute('''UPDATE students_db SET name = ?, age = ?, course = ?, contact = ? WHERE id = ?''', (name, age, course, contact, id))
    conn.commit()
    conn.close()
    return True

def delete_student(name):
    conn = sqlite3.connect('student_database.db')
    c = conn.cursor()
    c.execute('''DELETE FROM students_db WHERE name = ?''', (name,))
    conn.commit()
    conn.close()

def search_student(name):
    conn = sqlite3.connect('student_database.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM students_db where name = ?''', (name,))
    return c.fetchall()

def validate_student_id(id):
    conn = sqlite3.connect('student_database.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM students_db WHERE id = ?''', (id,))
    return c.fetchall()

def validate_student_name(name):
    conn = sqlite3.connect('student_database.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM students_db WHERE name = ?''', (name,))
    return c.fetchall()

def export_to_csv():
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Age", "Course", "Contact"])
        conn = sqlite3.connect("student_database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students_db")
        for row in cursor.fetchall():
            writer.writerow(row)
        conn.close()
    messagebox.showinfo("Success", "Data exported successfully!")

create_database()



