import tkinter as tk
root = tk.Tk()
root.title("Login Page")
root.geometry("500x500")
root.configure(bg="light blue")

lb1 = tk.Label(root, text="Enter Username", font=("Arial", 18))
lb1.place(x=160, y=30)
t1 = tk.Entry(root,textvariable="uname",font=("Arial", 18))
t1.place(x=120, y=80)

lb2 = tk.Label(root, text="Enter Password", font=("Arial", 18))
lb2.place(x=160, y=150)
t2 = tk.Entry(root,textvariable="password",font=("Arial", 18))
t2.place(x=120, y=200)

btn1 = tk.Button(root, text="Login", font=("times new roman", 18),width=8, height=2, bg="green", fg="white")
btn1.place(x=100, y=300)

btn2 = tk.Button(root, text="Register", font=("times new roman", 18),width=8, height=2, bg="blue", fg="white")
btn2.place(x=250, y=300)

root.mainloop()

