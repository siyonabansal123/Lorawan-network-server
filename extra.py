import sqlite3

# Connect to the SQLite database (you can replace 'your_database.db' with your actual database file)
conn = sqlite3.connect('all_data.db')
cursor = conn.cursor()

# Create the "gateways" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS gateways (
        name TEXT NOT NULL,
        mac_address TEXT UNIQUE NOT NULL,
        location TEXT NOT NULL
    )
''')

# # Drop the "gateways" table if it exists
# cursor.execute('DROP TABLE IF EXISTS gateways')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Table 'gateways' created successfully.")
