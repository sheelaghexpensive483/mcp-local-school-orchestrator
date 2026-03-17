import sqlite3

def init_db():
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students 
                      (id INTEGER PRIMARY KEY, name TEXT, grade INTEGER, gpa REAL)''')
    students = [(1, 'Alice Smith', 10, 3.9), (2, 'Bob Jones', 10, 3.2), (3, 'Charlie Brown', 11, 3.7)]
    cursor.executemany("INSERT OR IGNORE INTO students VALUES (?,?,?,?)", students)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("✅ School database initialized.")