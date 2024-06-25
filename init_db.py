import sqlite3

# Initialize the database
connection = sqlite3.connect('security.db')

# Create tables
with open('schema.sql') as f:
    connection.executescript(f.read())

connection.commit()
connection.close()
