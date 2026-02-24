import sqlite3

# Connect to database (creates file if it doesn't exist)
conn = sqlite3.connect("internship.db")

# Create cursor
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    track TEXT NOT NULL,
    stipend INTEGER
)
""")

print("Table created successfully!")

# Insert your intern data
intern_data = [
    (1, "Sneha", "Data Science", 15000),
    (2, "Deepa", "Web Dev", 12000),
    (3, "Pavithra", "Data Science", 18000),
    (4, "Preeti", "Web Dev", 10000),
    (5, "Sanjana", "UI/UX", 14000)
]

# Insert without duplicate error
cursor.executemany("INSERT OR IGNORE INTO interns VALUES (?, ?, ?, ?)", intern_data)

# Save changes
conn.commit()
print("Data inserted successfully!")

# Fetch and display data
cursor.execute("SELECT name, track FROM interns")
rows = cursor.fetchall()

print("\nInterns List:")
for row in rows:
    print(row)

# Close connection
conn.close()