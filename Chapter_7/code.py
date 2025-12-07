# Write the steps to connect to an SQLite database and insert a row into a 
# table. 
import sqlite3
conn = sqlite3.connect('database.db') 
cursor = conn.cursor() 
cursor.execute("INSERT INTO users VALUES (?, ?)", (user_id, name)) 
conn.commit() 
conn.close() 


# Problem 1 : Basic SQLite CRUD 
import sqlite3 
conn = sqlite3.connect('school.db') 
cursor = conn.cursor() 
cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS students ( 
        id INTEGER PRIMARY KEY, 
        name TEXT, 
        grade REAL 
    ) 
''') 
students_data = [ 
    (1, 'Ali', 85.5), 
    (2, 'Sara', 92.0), 
    (3, 'Mohamed', 78.3) 
] 
cursor.execute("DELETE FROM students") 
cursor.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'students'") 
conn.commit() 
cursor.executemany("INSERT INTO students VALUES (?, ?, ?)", students_data) 
conn.commit() 
print("Retrieved Records:") 
cursor.execute("SELECT * FROM students") 
all_records = cursor.fetchall() 
for record in all_records: 
    print(record) 
conn.close()




# Problem 2 :- Parameterized Queries 
import sqlite3 
conn = sqlite3.connect('school.db') 
cursor = conn.cursor()     
name = input("Enter name: ") 
grade = float(input("Enter grade: ")) 
cursor.execute("SELECT MAX(id) FROM students") 
max_id = cursor.fetchone()[0] 
new_id = (max_id if max_id is not None else 0) + 1  
cursor.execute("INSERT INTO students (id, name, grade) VALUES (?, ?, ?)",  
(new_id, name, grade)) 
conn.commit()     
cursor.execute("SELECT * FROM students") 
updated_records = cursor.fetchall() 
for record in updated_records: 
    print(record) 
conn.close()