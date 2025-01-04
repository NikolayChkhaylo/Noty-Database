import pandas as pd

# Load the Excel files
index_file = 'index.xlsx'  # File name for the 'index' file
songs_data_file = 'songs_data.xlsx'  # File name for the 'songs_data' file

# Read the data from the Excel files
index_df = pd.read_excel(index_file)
songs_data_df = pd.read_excel(songs_data_file)

# Adjust column names for the files
index_columns = ['Categories/Occasions', 'Vocal Types', 'Instrumental Type']  # Columns to process in the index file
songs_data_column = 'Categories'  # Column in the songs_data file containing categories to replace

# Iterate over each of the columns in the index file
for column, prefix in zip(index_columns, ['c', 'v', 'i']):  # Categories -> c, Vocal Types -> v, Instrumental Type -> i
    for idx, word in enumerate(index_df[column], start=2):  # Skip the header row (start=2)
        if pd.notna(word):  # Proceed only if the cell is not empty
            word = word.strip()  # Remove leading/trailing whitespace
            word_lower = word.lower()  # Convert to lowercase for case-insensitive matching

            # Iterate through each row in the songs_data file
            for row_idx, categories in songs_data_df[songs_data_column].items():
                if pd.notna(categories):  # Proceed only if the cell is not empty
                    # Split the categories in the cell by commas and strip any leading/trailing spaces
                    category_list = [category.strip() for category in categories.split(',')]

                    # Replace the matching word with the corresponding code (based on the prefix)
                    category_list = [f'{prefix}{idx}' if category.lower() == word_lower else category for category in category_list]

                    # Join the categories back into a comma-separated string
                    songs_data_df.at[row_idx, songs_data_column] = ', '.join(category_list)

            print(f"Replaced '{word}' with '{prefix}{idx}' in songs_data.")

# Save the updated 'songs_data' file (overwrite the original file)
songs_data_df.to_excel(songs_data_file, index=False)  # Overwrites original file

print("Process completed and the songs_data file has been updated.")
