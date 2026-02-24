import sqlite3

# Step 1: Connect to SQLite database
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Step 2: Drop tables if they already exist (prevents UNIQUE constraint error)
cursor.execute("DROP TABLE IF EXISTS employees")
cursor.execute("DROP TABLE IF EXISTS departments")

# Step 3: Create tables
cursor.execute("""
CREATE TABLE departments (
    dept_id INTEGER PRIMARY KEY,
    dept_name TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY,
    emp_name TEXT NOT NULL,
    dept_id INTEGER,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
)
""")

# Step 4: Insert sample data
cursor.executemany("INSERT INTO departments VALUES (?, ?)", [
    (1, "HR"),
    (2, "IT"),
    (3, "Finance")
])

cursor.executemany("INSERT INTO employees VALUES (?, ?, ?)", [
    (101, "Sneha", 1),
    (102, "Ankita", 2),
    (103, "Preeti", 2),
    (104, "Sanjana", None)
])

conn.commit()

# Step 5: INNER JOIN
print("INNER JOIN Result:")
cursor.execute("""
SELECT employees.emp_name, departments.dept_name
FROM employees
INNER JOIN departments
ON employees.dept_id = departments.dept_id
""")

for row in cursor.fetchall():
    print(row)

# Step 6: LEFT JOIN
print("\nLEFT JOIN Result:")
cursor.execute("""
SELECT employees.emp_name, departments.dept_name
FROM employees
LEFT JOIN departments
ON employees.dept_id = departments.dept_id
""")

for row in cursor.fetchall():
    print(row)

# Step 7: Close connection
conn.close()