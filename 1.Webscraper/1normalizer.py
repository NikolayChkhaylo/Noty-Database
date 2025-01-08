import re
import pandas as pd

# Word bank with replacements (you can expand this list as needed)
word_bank = {
    'Хор': {'chor', 'choir', 'chor (de.)', 'chor', 'Choir SATB', 'SATB', 'Квартет', 'Chois SATB', 'Хор (укр.)', 'САТБ', 'Хор САТБ', 'для хора САТБ', 'СААТББ'},
    'Хор, Акапела': {'Хор а капелла'},
    'Молодежный хор': {'Хор - молодёжный хор', 'Молодёжный хор','Хор молодежный'},
    'Мужской хор': {'Man Choir', 'Муж. хор'},
    'Муж. 3-о': {'Муж. трио', 'Мужское трио'},
    '3-o English': {'3-o - English'},
    '3-о Русский': {'3-о - Русский'},
    'Детский хор': {'Вокал (детский хор)', 'Детский и смешанный хоры', 'Детский', 'Деский хор'},
    

    'Соло': {'Соло (1 голос)', 'Вокал - соло', 'Вокальное соло', 'Вокал соло'},
    'Вок. 2-т': {'Vocal duo', 'Вокал - 2-т', 'Вокальный 2-т', 'Вокал 2-т', 'Вокал - дуэт', 'дуэт', 'Тенор - Альт 2-т'},
    'Вок. 3-о': {'Вокал - трио', 'Трио', 'Вокал 3-о', 'Вокал 3-о - аккорды'},
    
    'Вок. 4-т+': {'Квартет или группа м.хора'},
    
    'Скр. 1': {'Скр. 1/соло', 'скрипка'},
    'Стр. 2-т': {'2 скр','Скр. 2-т'},
    'Стр. 3-о': {'Скр. 3-о'},
    'Стр. 4-т': {'Скр. 4-т'},


    'Дух. 4-т': {'Дух. 4т - Е'},
    'Дух. 5-т': {'Духовой 5-т'},
    'Дух. 6+': {'Дух. 6-т'},

    'Фортепиано': {'фно', 'ф-но', 'Соло - ф-но', 'Хор + Фно', 'фоно', 'фо-но', 'фоно - укр.','Фортепианный акк.','Ф-но акк.'},
    'Симфонический оркестр': {'Symphonie-Orchester'},

    
    'Ансамбль': {'Ensemble','Ansamble'},
    'Украинский вариант': {'Український варіант', 'укр.вар.','укр. вариант'},
    'Духовой оркестр': {'Духовой','Духовой малый'},
    'Українські слова': {'Украинский текст'},
    'Хор + трио': {'Choir + trio'},
    'Аккордеон, Баян': {'АККОРДЕОН-БАЯН'},
    
    'Несколько разных мелодий:': {'Разные мелодии', 'version'},
    'Смешанный ансамбль': {'Ансамбль смешанный'},
    #'': {''},
    #'': {''},
    #'': {''},
    #'': {''},
    #'': {''},
    #'': {''},
    #'': {''},
    #'': {''},
    #'': {''},
    #'': {''},
    #'': {''},
    #'': {''},
}

def normalize_word(word):
    """Normalize a single word based on the word bank, ignoring case."""
    word_lower = word.lower()  # Convert word to lowercase for case-insensitive matching
    for normalized, variations in word_bank.items():
        # Use lowercase matching but return the original normalized word
        if word_lower in (w.lower() for w in variations):
            return normalized
    return word  # Return the word unchanged if no match is found


def replace_dash_with_comma(text):
    """Replace a dash surrounded by spaces with a comma."""
    if isinstance(text, str):
        return text.replace(' - ', ',')
    return text

def remove_number_from_album_name(text, albums_in_index):
    """Remove '№' and number, also remove any number after a space, keeping the album name and comma intact for specific albums."""
    if isinstance(text, str):
        # Only perform this for albums that exist in the 'Album' column of the index file
        for album in albums_in_index:
            # Check case-insensitively if the album is in the text
            if album.lower() in text.lower():
                # Remove '№' and the number that follows it (e.g., '№229')
                text = re.sub(r'№\d+', '', text)

                # Remove any number after the dash (e.g., ' - 212')
                text = re.sub(r' - \d+', '', text)
                text = re.sub(r'-\d+', '', text)  # Handle the case where no space before the number

                # Remove any number after a space (e.g., 'ПВ 1431')
                text = re.sub(r' \d+', '', text)

                # Remove numbers in parentheses (e.g., '(537)')
                text = re.sub(r'\(\d+\)', '', text)

                

                # Ensure the comma remains intact and there are no extra spaces at the end
                if text.endswith(','):
                    text = text.strip()

    return text

def normalize_categories(categories, albums_in_index):
    """Normalize the categories with double normalization."""
    if isinstance(categories, str):
        # Remove the number from album names first (only for albums in the index)
        categories = remove_number_from_album_name(categories, albums_in_index)

        # First normalization (without dash replacement)
        words = [normalize_word(word.strip()) for word in categories.split(',')]
        normalized_text = ', '.join(words)

        # Replace dash with comma
        normalized_text = replace_dash_with_comma(normalized_text)

        # Second normalization (after dash replacement)
        words = [normalize_word(word.strip()) for word in normalized_text.split(',')]
        return ', '.join(words)

    return categories  # Return unchanged if not a string

# Load the index Excel file to get the album names
index_file_path = 'index.xlsx'
index_df = pd.read_excel(index_file_path)

# Extract album names from the 'Album' column starting from the 2nd row
albums_in_index = index_df['Album'][1:].dropna().tolist()  # Get all album names, excluding the first row

# Load the songs_data Excel file
file_path = 'songs_data.xlsx'
df = pd.read_excel(file_path)

# Normalize the 'Categories' column
df['Categories'] = df['Categories'].apply(lambda x: normalize_categories(x, albums_in_index))

# Save the modified DataFrame back to the Excel file
df.to_excel(file_path, index=False)

print(f"Normalization complete. The file {file_path} has been updated.")
