import sqlite3

conn = sqlite3.connect("login_page.db")
print("Opened database successfully")

# Creating table in the database
# conn.execute('''CREATE TABLE login_details
#             (S_NO INTEGER PRIMARY KEY AUTOINCREMENT,
#             username TEXT NOT NULL, 
#             password TEXT NOT NULL)''')
# print("Table created successfully")

# Inserting data into the table
# conn.execute('''INSERT INTO login_details (S_NO, username, password)
#             VALUES (1, 'Sachin', 'god@100')''')

# conn.execute('''INSERT INTO login_details (S_NO, username, password)
#             VALUES (2, 'Rahul', 'rahul@100')''')

# conn.execute('''INSERT INTO login_details (S_NO, username, password)
#             VALUES (3, 'Rohit', 'rohit@100')''')

# conn.execute('''INSERT INTO login_details (username, password)
#             VALUES ('Virat', 'virat@100')''')

conn.commit()
print("Records created successfully")

# Fetching data from the table or to show table data
login_data = conn.execute("SELECT * FROM login_details")
for row in login_data:
    print(row)
    
# Updating the data in the table
conn.execute('''UPDATE login_details SET password = 'god@200' WHERE S_NO = 1''')
print("Updated successfully")

# Deleting the data from the table
conn.execute('''DELETE FROM login_details WHERE S_NO = 2''')
print("Deleted successfully")

conn.close()