import pandas as pd
import sqlite3

# Load Excel data
file_path = 'index.xlsx'  # Update with your actual file path
df = pd.read_excel(file_path)

# Connect to the SQLite database
conn = sqlite3.connect('database')  # Update with your actual database path
cursor = conn.cursor()

# Insert a "PLACEHOLDER" value for each table to offset the IDs
cursor.execute("INSERT INTO composers (composers_name) VALUES ('PLACEHOLDER')")
cursor.execute("INSERT INTO genre (genre_name) VALUES ('PLACEHOLDER')")
cursor.execute("INSERT INTO instruments (instruments_name) VALUES ('PLACEHOLDER')")
cursor.execute("INSERT INTO vocals (vocals_name) VALUES ('PLACEHOLDER')")

# Commit the changes to generate the placeholder IDs
conn.commit()

# Insert data into composers table
composers = df['Composer'].dropna().unique()  # Get unique composers, drop any NaN values
for composer in composers:
    cursor.execute("INSERT INTO composers (composers_name) VALUES (?)", (composer,))

# Insert data into genre table
categories = df['Categories/Occasions'].dropna().unique()  # Get unique categories/occasions
for category in categories:
    cursor.execute("INSERT INTO genre (genre_name) VALUES (?)", (category,))

# Insert data into instruments table
instruments = df['Instrumental Type'].dropna().unique()  # Get unique instrumental types
for instrument in instruments:
    cursor.execute("INSERT INTO instruments (instruments_name) VALUES (?)", (instrument,))

# Insert data into vocals table
vocals = df['Vocal Types'].dropna().unique()  # Get unique vocal types
for vocal in vocals:
    cursor.execute("INSERT INTO vocals (vocals_name) VALUES (?)", (vocal,))

# Commit the changes
conn.commit()

# Close the connection
conn.close()

print("Tables populated successfully!")
