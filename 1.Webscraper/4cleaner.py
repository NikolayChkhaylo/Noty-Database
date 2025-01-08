import pandas as pd

# Load the Excel file
file_path = 'songs_data.xlsx'  # Update with your actual file path
df = pd.read_excel(file_path)  # Use pd.read_excel() for Excel files

# Function to clean up stray semicolons and remove colons from the 'Categories' column
def clean_categories(value):
    # Check if the value is empty or NaN (and return it unchanged)
    if pd.isna(value) or value == '':
        return ''  # Return an empty string for NaN or empty values
    
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

# Apply the cleaning function to the 'Categories' column
df['Categories'] = df['Categories'].apply(lambda x: clean_categories(x))

# Save the updated Excel file (overwrite the original file)
df.to_excel(file_path, index=False)  # Overwrite the original file

print(f"Cleaned data has been saved to '{file_path}'.")
