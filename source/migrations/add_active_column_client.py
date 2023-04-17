import sqlite3

# Check if the 'active' column exists in the 'Client' table
conn = sqlite3.connect('../database.sqlite')
cursor = conn.cursor()
cursor.execute("PRAGMA table_info('Client')")
table_info = cursor.fetchall()
column_names = [row[1] for row in table_info]
if 'active' not in column_names:
    # If the 'active' column does not exist, add it to the 'Client' table
    cursor.execute("ALTER TABLE Client ADD COLUMN active BOOLEAN DEFAULT 1")
    conn.commit()
    print("Migration successful: added 'active' column to 'Client' table")
else:
    print("Migration skipped: 'active' column already exists in 'Client' table")


