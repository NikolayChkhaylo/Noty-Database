import pandas as pd

# Word bank with replacements (you can expand this list as needed)
word_bank = {
    'Хор': {'chor','choir', 'Chor (de.)', 'Chor','Choir SATB','SATB','Квартет', 'Chois SATB','Хор (укр.)','САТБ','Хор САТБ','для хора САТБ','СААТББ'},
    'Соло': {'Соло (1 голос)','Вокал - соло','Вокальное соло','Вокал соло'},
    'Скр. 1': {'Скр. 1/соло','скрипка','Скрипка'},
    'Вок. 3-о' : {'Вокал - трио','Трио','Вокал 3-о','Вокал 3-о - аккорды'},
    'Вок. 2-т' : {'Vocal duo','Вокал - 2-т','Вокальный 2-т','Вокал 2-т','Вокал - дуэт','Дуэт','дуэт','Тенор - Альт 2-т'},
    'Фортепиано' : {'фно','ф-но','Соло - ф-но','Хор + Фно','фоно','фо-но','фоно - укр.'},
    'Молодежный хор' : {'Хор - молодёжный хор','Молодёжный хор'},
    'Дух. 5-т' : {'Духовой 5-т'},
    'Муж. 3-о' : {'Муж. трио','Мужское трио'},
    'Симфонический оркестр' : {'Symphonie-Orchester'},
    'Мужской хор' : {'Man Choir','Муж. хор'},
    'Стр. 4-т' : {'Скр. 4-т'},
    'Дух. 6+' : {'Дух. 6-т'},
    'Дух. 4-т' : {'Дух. 4т - Е'},
    'Детский хор' : {'Вокал (детский хор)','Детский и смешанный хоры','Детский','Деский хор'},
    'Стр. 3-о' : {'Скр. 3-о'},
    'Вок. 4-т+' : {'Квартет или группа м.хора'},
    'Ансамбль' : {'Ensemble'},
    'Украинский вариант' : {'Український варіант','укр.вар.'},
}

def normalize_word(word):
    # Check each entry in the word bank
    for normalized, variations in word_bank.items():
        if word in variations:
            return normalized  # Return the normalized word
    return word  # Return the word unchanged if no match is found

def replace_dash_with_comma(text):
    # Replace a dash surrounded by spaces with a comma
    if isinstance(text, str):
        return text.replace(' - ', ',')
    return text

def normalize_categories(categories):
    # Replace dash with comma first
    categories = replace_dash_with_comma(categories)
    
    # Check if the category is a valid string
    if isinstance(categories, str):
        # Split the categories by commas and strip leading/trailing spaces
        words = [word.strip() for word in categories.split(',')]
        
        # Normalize each word using the `normalize_word` function
        normalized_words = [normalize_word(word) for word in words]
        
        # Join the normalized words back with commas
        return ', '.join(normalized_words)
    return categories  # Return unchanged if not a string

# Load the Excel file
file_path = 'songs_data.xlsx'
df = pd.read_excel(file_path)

# Normalize the 'Categories' column
df['Categories'] = df['Categories'].apply(normalize_categories)

# Save the modified DataFrame back to the Excel file
df.to_excel(file_path, index=False)

print(f"Normalization complete. The file {file_path} has been updated.")
