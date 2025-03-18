import tkinter as tk
from tkinter import messagebox
from db import register_user

def new_user():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == "" or password == "":
        messagebox.showerror("Error", "All fields are required")
        return
    
    if register_user(username, password):
        messagebox.showinfo("Success", "Registration successful")
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        root.destroy()
    else:
        messagebox.showerror("Error", "Username already exists")
        

def show_register_page():
    global root, username_entry, password_entry
    root = tk.Tk()
    root.title("Register")
    root.geometry("400x250")
    

    tk.Label(root, text="New Username:", font=("Times new roman", 18)).pack()
    username_entry = tk.Entry(root, font=("Timesmnew roman", 18))
    username_entry.pack()

    tk.Label(root, text="New Password:", font=("Times new roman", 18)).pack()
    password_entry = tk.Entry(root, show="*", font=("Times new roman", 18))
    password_entry.pack()

    tk.Button(root, text="Register", command=new_user, font=("Times new roman", 18)).pack(pady=5)
    root.mainloop()
    
