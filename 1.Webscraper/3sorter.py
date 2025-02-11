import pandas as pd

# Load the Excel files
index_file = 'index.xlsx'  # File name for the 'index' file
songs_data_file = 'songs_data.xlsx'  # File name for the 'songs_data' file

# Read the data from the Excel files
index_df = pd.read_excel(index_file)
songs_data_df = pd.read_excel(songs_data_file)

# Define the columns to process and their corresponding prefixes
index_columns = ['Categories/Occasions', 'Vocal Types', 'Instrumental Type', 'Misc.', 'Composer', 'Album', 'Language']
prefixes = ['c', 'v', 'i', 'm', 'w', 'a', 'l']

# Build a lookup dictionary for fast replacement
lookup = {}
for column, prefix in zip(index_columns, prefixes):
    for idx, word in enumerate(index_df[column], start=2):  # Start indexing at 2
        if pd.notna(word):  # Skip empty cells
            lookup[word.strip().lower()] = f'{prefix}{idx}'  # Map lowercase word to code

# Normalize and replace categories in the songs_data file
def replace_categories(categories):
    if pd.notna(categories):
        # Split categories, map them using the lookup, and join back into a string
        return ', '.join([lookup.get(cat.strip().lower(), cat.strip()) for cat in categories.split(',')])
    return categories

# Apply the replacement to the Categories column
songs_data_df['Categories'] = songs_data_df['Categories'].apply(replace_categories)

# Save the updated songs_data file (overwrite the original file)
songs_data_df.to_excel(songs_data_file, index=False)

print("Process completed and the songs_data file has been updated.")
