import pandas as pd
import re

# Load the Excel file
songs_data_file = 'songs_data.xlsx'  # File name for the 'songs_data' file
songs_data_df = pd.read_excel(songs_data_file)

# Function to remove code words (e.g., c2, c3, etc.) and unwanted phrases
def clean_text(text):
    if pd.notna(text):  # Only process non-null cells
        # Remove code words like 'c2', 'c3', 'v2', 'i3', etc.
        #text = re.sub(r'\b[cvimwal]\d+\b', '', text)

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
        text = re.sub(r'Lyrics & Tune by:', '', text)
        text = re.sub(r'Instr.', '', text)
        text = re.sub(r'Arranged by', '', text)
        text = re.sub(r'Русс. текст', '', text)
        text = re.sub(r'Требуется русский/украинский перевод:', '', text)
        text = re.sub(r'Lyrics & Tune by::', '', text)
        text = re.sub(r'versions:', '', text)
        text = re.sub(r'Слова та музика:', '', text)
        text = re.sub(r'Разные авторы слов:', '', text)
        text = re.sub(r'Сл. и муз.:', '', text)
        text = re.sub(r'давно бы уже пора перевести на русский!', '', text)
        text = re.sub(r'Revision:', '', text)
        text = re.sub(r'(Titel)', '', text)
        text = re.sub(r'Eng:', '', text)
        text = re.sub(r'Пришлите пожалуйста!', '', text)
        text = re.sub(r'Из старого христианского журнала', '', text)
        text = re.sub(r'Tr. by:', '', text)
        text = re.sub(r'Сл. и муз.', '', text)
        text = re.sub(r'Arr.:', '', text)
        text = re.sub(r'пер.', '', text)
        text = re.sub(r'Аранж.:', '', text)
        text = re.sub(r'Перев.:', '', text)
        text = re.sub(r'Русский текст', '', text)
        text = re.sub(r'из рукописей', '', text)
        #text = re.sub(r'№', '', text)
        #text = re.sub(r':', '', text)
        text = re.sub(r'Перевод:', '', text)
        text = re.sub(r'Перевод', '', text)
        text = re.sub(r'Обр.', '', text)
        text = re.sub(r'аранж.', '', text)
        text = re.sub(r'Сл.і муз.', '', text)
        text = re.sub(r'Запись на слух.', '', text)
        text = re.sub(r'Аранж.', '', text)
        text = re.sub(r'Слова і музика', '', text)
        text = re.sub(r'Переклад', '', text)
        text = re.sub(r'Со скрипками', '', text)
        text = re.sub(r'текста и музыка:', '', text)
        text = re.sub(r'Слова та музіка:', '', text)
        #text = re.sub(r'аранж.', '', text)
        #text = re.sub(r'аранж.', '', text)
        #text = re.sub(r'аранж.', '', text)
        #text = re.sub(r'аранж.', '', text)
        #text = re.sub(r'аранж.', '', text)
        #text = re.sub(r'аранж.', '', text)
        #text = re.sub(r'аранж.', '', text)
        #text = re.sub(r'аранж.', '', text)
            
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
