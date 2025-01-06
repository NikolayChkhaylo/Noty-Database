import pandas as pd
import re

# Load the Excel file
songs_data_file = 'songs_data.xlsx'  # File name for the 'songs_data' file
songs_data_df = pd.read_excel(songs_data_file)

# Function to remove code words (e.g., c2, c3, etc.) and unwanted phrases
def clean_text(text):
    if pd.notna(text):  # Only process non-null cells
        # Remove code words like 'c2', 'c3', 'v2', 'i3', etc.
        text = re.sub(r'\b[cvimwal]\d+\b', '', text)

        # Remove specific phrases (Слова и музыка and Words and music by)
        text = re.sub(r'Слова и музыка', '', text)
        text = re.sub(r'Words and music by', '', text)
        text = re.sub(r'Original', '', text)
        text = re.sub(r'Words & Music by', '', text)
        text = re.sub(r'Deutsch:', '', text)
        text = re.sub(r'Original version', '', text)
        text = re.sub(r'Anon', '', text)
        text = re.sub(r'Рус. текст:', '', text)
        text = re.sub(r'sample', '', text)
        text = re.sub(r'Melodie und Satz', '', text)
        text = re.sub(r'Translation', '', text)
        text = re.sub(r'Trans.', '', text)
        text = re.sub(r'\*{3}', '', text)
        text = re.sub(r'Рус. текст', '', text)
        text = re.sub(r'Choir + trio', '', text)
        text = re.sub(r'\?{3}', '', text)
        text = re.sub(r'Муз. и слова', '', text)
        text = re.sub(r'Слова и мелодия', '', text)
        text = re.sub(r'Сл. і муз.', '', text)
        text = re.sub(r'Слова і музика:', '', text)
        text = re.sub(r'Text și muzică', '', text)
        text = re.sub(r'текст:', '', text)
        text = re.sub(r'Укр. текст', '', text)
        text = re.sub(r'ELyrics & Tune by:', '', text)
        text = re.sub(r'Instr.', '', text)
        text = re.sub(r'Arranged by', '', text)
        #text = re.sub(r'Eng:', '', text)
        #text = re.sub(r'Eng:', '', text)
        #text = re.sub(r'Eng:', '', text)
        #text = re.sub(r'Eng:', '', text)
        #text = re.sub(r'Eng:', '', text)
        #text = re.sub(r'Eng:', '', text)
        #text = re.sub(r'Eng:', '', text)
        # Remove any extra spaces after the removal
        text = re.sub(r'\s+', ' ', text).strip()

    return text

# Apply the cleaning function to the relevant column (adjust the column name if needed)
songs_data_column = 'Categories'  # The column to clean

# Iterate through each row and clean the data
for row_idx, categories in songs_data_df[songs_data_column].items():
    songs_data_df.at[row_idx, songs_data_column] = clean_text(categories)

# Save the updated 'songs_data' file (overwrite the original file)
songs_data_df.to_excel(songs_data_file, index=False)  # Overwrites original file

print("Process completed and the songs_data file has been cleaned and overwritten.")
