from app import db

# Connect to the database
connection = db.engine.connect()

# Query to check if the 'user' table exists
result = connection.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='user';")

# Fetch the result
table_exists = result.fetchone()

if table_exists:
    print("The 'user' table exists.")
else:
    print("The 'user' table does not exist.")
