import tkinter as tk
from add_student import show_add_student_page
from delete_student import show_delete_student_page
from search_student import show_search_student_page
from update_student import validate_student_page
from view_student import show_view_student_page
from database import export_to_csv

root = tk.Tk()
root.title('Student Management System')
root.geometry('550x450')

add_student_button = tk.Button(root, text='Add student', width=25, height=4, bg='light blue', command=show_add_student_page)
add_student_button.place(x=50, y=20)

view_student_button = tk.Button(root, text='View student', width=25, height=4, bg='light blue', command=show_view_student_page)
view_student_button.place(x=300, y=20)

update_student_button = tk.Button(root, text='Update student', width=25, height=4, bg='light blue', command=validate_student_page)
update_student_button.place(x=50, y=150)

delete_student_button = tk.Button(root, text='Delete student', width=25, height=4, bg='light blue', command=show_delete_student_page)
delete_student_button.place(x=300, y=150)

search_student_button = tk.Button(root, text='Search student', width=25, height=4, bg='light blue', command=show_search_student_page)
search_student_button.place(x=50, y=280)

exit_button = tk.Button(root, text='Exit', width=25, height=4, bg='red', command=root.quit)
exit_button.place(x=300, y=280)

def update_theme():
    if theme_var.get() == "dark":
        root.config(bg='black')
        dark_radio.config(bg='black', fg='white', activebackground='gray', activeforeground='white')
        light_radio.config(bg='black', fg='white', activebackground='gray', activeforeground='white')
    else:
        root.config(bg='white')
        dark_radio.config(bg='white', fg='black', activebackground='lightgray', activeforeground='black')
        light_radio.config(bg='white', fg='black', activebackground='lightgray', activeforeground='black')
        
theme_var = tk.StringVar(value="light")

dark_radio = tk.Radiobutton(root, text="Dark Mode", variable=theme_var, value="dark", command=update_theme)
light_radio = tk.Radiobutton(root, text="Light Mode", variable=theme_var, value="light", command=update_theme)

dark_radio.place(x=100,y=380)
light_radio.place(x=100,y=410)


export_csv_btn = tk.Button(root, text='Export to CSV', width=25, height=2, bg='orange',command=export_to_csv)
export_csv_btn.place(x=300, y=390)

root.mainloop()