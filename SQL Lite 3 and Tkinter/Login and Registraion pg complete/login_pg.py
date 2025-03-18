import tkinter as tk
from tkinter import messagebox
from db import verify_user
from registration_pg import show_register_page

def login_user():
    username = entry_login_username.get()
    password = entry_login_password.get()
    
    if verify_user(username, password):
        messagebox.showinfo("Success", "Login successful")
        entry_login_username.delete(0, tk.END)
        entry_login_password.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Invalid username or password")
        entry_login_username.delete(0, tk.END)
        entry_login_password.delete(0, tk.END)

root = tk.Tk()
root.title("Login Page")
root.geometry("400x300")

tk.Label(root, text="Username:", font=("Times new roman", 18)).pack()
entry_login_username = tk.Entry(root, font=("Times new roman", 18)) 
entry_login_username.pack()

tk.Label(root, text="Password:", font=("Times new roman", 18)).pack()
entry_login_password = tk.Entry(root, show="*", font=("Times new roman", 18))
entry_login_password.pack()

tk.Button(root, text="Login", command=login_user, font=("Times new roman", 18)).pack(pady=5)
tk.Button(root, text="Register", command=show_register_page, font=("Times new roman", 18)).pack()

root.mainloop()
