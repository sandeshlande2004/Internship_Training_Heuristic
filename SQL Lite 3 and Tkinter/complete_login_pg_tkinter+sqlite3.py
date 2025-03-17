# Description: This is a complete login page with tkinter and sql lite3. It has a registration and login page. The user can register and login using this page.
#----------------------------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------LOGIN PAGE WITH TKINTER AND SQLLITE3--------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------------------#

import sqlite3
import tkinter as tk
from tkinter import messagebox

conn = sqlite3.connect('user_detail.db')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE,
                password TEXT)''')

conn.commit()

def register():
    email = email_entry.get()
    password = password_entry.get()
    
    if email and password:
        try:
            c.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
            conn.commit()
            messagebox.showinfo("Success", "Registration Completed!")
            email_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Email already registered.\nPlease try again.")
            email_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            
    else:
        messagebox.showwarning("Warning", "Please fill in all fields.")
        email_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

def login():
    email = email_entry.get()
    password = password_entry.get()
    
    c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    user = c.fetchone()
    
    if user:
        messagebox.showinfo("Success", "Login successful!")
        email_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Invalid email or password.")
        email_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Login Page")
root.geometry("500x500")
root.configure(bg="light blue")

lb1 = tk.Label(root, text="Enter Username:", font=("Arial", 18))
lb1.place(x=160, y=30)
email_entry = tk.Entry(root,textvariable="uname",font=("Arial", 18))
email_entry.place(x=120, y=80)

lb2 = tk.Label(root, text="Enter Password:", font=("Arial", 18))
lb2.place(x=160, y=150)
password_entry = tk.Entry(root,textvariable="password",font=("Arial", 18), show="*")
password_entry.place(x=120, y=200)

loginbutton = tk.Button(root, text="Login", font=("times new roman", 18),width=8, height=2, bg="green", fg="white", command=login)
loginbutton.place(x=100, y=300)

registerbutton = tk.Button(root, text="Register", font=("times new roman", 18),width=8, height=2, bg="blue", fg="white", command=register)
registerbutton.place(x=250, y=300)

root.mainloop()

conn.close()
        
