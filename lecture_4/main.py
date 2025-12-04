import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute('''
create index students_full_name on students(full_name);



''')
s = cursor.fetchall()
conn.commit()
print(s)
conn.close()
