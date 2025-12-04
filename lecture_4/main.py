import sqlite3 as sql
import time
conn_db = sql.Connection("school.db")

cursor = conn_db.cursor()
def measure(query, description):
    start = time.perf_counter()
    cursor.execute(query).fetchall()
    end = time.perf_counter()
    print(f"{description}: {end - start:.6f} сек")

query1 = """select g.grade from grades g
            join students s on s.id = g.student_id
            where s.full_name = 'Alice Johnson'"""

query2 = """select s.full_name, avg(grade) from grades g
            join students s on s.id = g.student_id
            group by s.full_name"""

query3 = """select full_name from students where birth_year > 2004"""

print("=== Без индексов ===")
measure(query1, "Оценки Alice Johnson")
measure(query2, "Средний балл по студентам")
measure(query3, "Студенты после 2004")

# 5. Добавляем индексы
cursor.execute("create index students_full_name on students(full_name);")



print("\n=== С индексами ===")
measure(query1, "Оценки Alice Johnson")
measure(query2, "Средний балл по студентам")
measure(query3, "Студенты после 2004")

conn_db.close()
