import subprocess
import sqlite3
import os

# Define paths
WEB_SCRAPER_FOLDER = "path/to/webscraper"
SQL_FOLDER = "path/to/sql"
SQLITE_DB = "path/to/your_database.db"
POWER_BI_FOLDER = "path/to/powerbi"
POWER_BI_FILE = "path/to/your_powerbi.pbix"
SQL_SCRIPT = os.path.join(SQL_FOLDER, "your_script.sql")

# 1. Run web scraper script
print("Running web scraper...")
subprocess.run(["python", os.path.join(WEB_SCRAPER_FOLDER, "scraper.py")])

# 2. Run sorting script
print("Sorting data...")
subprocess.run(["python", os.path.join(WEB_SCRAPER_FOLDER, "sorter.py")])

# 3. Execute SQL script
print("Executing SQL script...")
with open(SQL_SCRIPT, "r") as file:
    sql_script = file.read()

conn = sqlite3.connect(SQLITE_DB)
cursor = conn.cursor()
cursor.executescript(sql_script)
conn.commit()
conn.close()
print("Database setup complete.")

# 4. Open Power BI visualization
print("Launching Power BI visualization...")
subprocess.run(["start", "", POWER_BI_FILE], shell=True)

print("Process completed successfully!")
