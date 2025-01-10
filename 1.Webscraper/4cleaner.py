import pandas as pd
import re

# Load the Excel file
file_path = 'songs_data.xlsx'  # Update with your actual file path
df = pd.read_excel(file_path)  # Use pd.read_excel() for Excel files

# Function to clean up stray semicolons, remove colons, replace slashes with commas, and remove leading number phrases
def clean_categories(value):
    # Check if the value is empty or NaN (and return it unchanged)
    if pd.isna(value) or value == '':
        return ''  # Return an empty string for NaN or empty values
    
    # Replace slashes with commas
    value = value.replace('/', ',')

    # Remove leading number phrases like '№030'
    value = re.sub(r'^№\d+', '', value).strip()

    # Split the string by commas to handle each part
    parts = value.split(',')
    cleaned_parts = []

    for part in parts:
        # Strip any leading/trailing spaces
        part = part.strip()

        # Skip empty values or stray colons
        if part == '' or part == ':':
            continue
        else:
            cleaned_parts.append(part)

    # Join the cleaned parts back with commas
    return ','.join(cleaned_parts)

# Apply the cleaning function to the 'Categories' column only where values are not NaN
df['Categories'] = df['Categories'].apply(lambda x: clean_categories(x) if pd.notna(x) else '')

# Save the updated Excel file (overwrite the original file)
df.to_excel(file_path, index=False)  # Overwrite the original file

print(f"Cleaned data has been saved to '{file_path}'.")
