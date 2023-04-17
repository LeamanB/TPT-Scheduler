import sqlite3

# Check if the 'active' column exists in the 'Trainer' table
conn = sqlite3.connect('../database.sqlite')
cursor = conn.cursor()
cursor.execute("PRAGMA table_info('Trainer')")
table_info = cursor.fetchall()
column_names = [row[1] for row in table_info]
if 'active' not in column_names:
    # If the 'active' column does not exist, add it to the 'Trainer' table
    cursor.execute("ALTER TABLE Trainer ADD COLUMN active BOOLEAN DEFAULT 1")
    conn.commit()
    print("Migration successful: added 'active' column to 'Trainer' table")
else:
    print("Migration skipped: 'active' column already exists in 'Trainer' table")


