import re
import pandas as pd

# Word bank with replacements
word_bank = {
    'Хор': {'chor', 'choir', 'chor (de.)', 'chor', 'Choir SATB', 'SATB', 'Квартет', 'Chois SATB', 'Хор (укр.)', 'САТБ', 'Хор САТБ', 'для хора САТБ', 'СААТББ','Хор САБ/САТБ'},
    'Хор, Акапела': {'Хор а капелла'},
    'Хор + трио': {'Choir + trio'},
    'Молодежный хор': {'Хор - молодёжный хор', 'Молодёжный хор','Хор молодежный'},
    'Мужской хор': {'Man Choir', 'Муж. хор'},
    'Муж. 3-о': {'Муж. трио', 'Мужское трио'},
    '3-o English': {'3-o - English'},
    '3-о Русский': {'3-о - Русский'},
    'Детский хор': {'Вокал (детский хор)', 'Детский и смешанный хоры', 'Детский', 'Деский хор'},
    'Соло': {'Соло (1 голос)', 'Вокал - соло', 'Вокальное соло', 'Вокал соло'},
    'Вок. 2-т': {'Vocal duo', 'Вокал - 2-т', 'Вокальный 2-т', 'Вокал 2-т', 'Вокал - дуэт', 'дуэт', 'Тенор - Альт 2-т'},
    'Вок. 3-о': {'Вокал - трио', 'Трио', 'Вокал 3-о', 'Вокал 3-о - аккорды','Ансамбль 3-о'},
    'Вок. 4-т+': {'Квартет или группа м.хора'},
    'Скр. 1': {'Скр. 1/соло', 'скрипка'},
    'Стр. 2-т': {'2 скр','Скр. 2-т'},
    'Стр. 3-о': {'Скр. 3-о'},
    'Стр. 4-т': {'Скр. 4-т','Струнный квартет'},
    'Дух. 4-т': {'Дух. 4т - Е'},
    'Дух. 5-т': {'Духовой 5-т'},
    'Дух. 6+': {'Дух. 6-т','Духовой 6т','Духовой 6','Духовой 6-т'},
    'Дух. 7-т': {'Духовой 7'},
    'Трубы 2-т': {'Труба 2-т'},
    'Фортепиано': {'фно', 'ф-но', 'Соло - ф-но', 'Хор + Фно', 'фоно', 'фо-но', 'фоно - укр.','Фортепианный акк.','Ф-но акк.'},
    'Симфонический оркестр': {'Symphonie-Orchester'},  
    'Ансамбль': {'Ensemble','Ansamble','Для ансамбля','Народный ансамбль'},
    'Духовой оркестр': {'Духовой','Духовой малый','Малый духовой оркестр','Средний духовой оркестр','Духовой ансамбль'},
    'Украинский вариант': {'Український варіант', 'укр.вар.','укр. вариант'},
    'Українські слова': {'Украинский текст'},
    'Аккордеон, Баян': {'АККОРДЕОН-БАЯН'},
    'Несколько разных мелодий:': {'Разные мелодии', 'version'},
    'Смешанный ансамбль': {'Ансамбль смешанный','Смеш. ансамбль'},
    '': {'Том 3'},
    'Муж. хор, дух. 4-т': {'Муж. хор + дух. 4-т'},
    'Бандура': {'бандури'},
    'Домра': {'Домры'},
    'Хор и аккомпанемент': {'Хор с аккомпанементом'},
    'Соло, скр. 2-т': {'Соло + скр. 2-т'},
    'Хор, скр. 4-т': {'Хор + скр. 4-т'},
    'Камерный ансамбль': {'камерный анс.'},
    'Смешанный хор, ф-но': {'Смешанный хор + ф-но'},
    'Соло, Фортепиано': {' Соло и фоно','Соло и фортепиано'},
    'Дух. 2-т, Фортепиано': {'Дух. 2-т + фно'},
    'Смешанный оркестр': {'Большой смеш. оркестр, Малый смеш. оркестр,'},
    'Разные варианты': {'2 мелодии','versions'},
    'Стр. 2-т, Фортепиано': {'2 скр фно'},
}

# Preprocess word bank to make it case-insensitive
processed_word_bank = {k: {v.lower() for v in vs} for k, vs in word_bank.items()}

# Function to normalize a single word
def normalize_word(word):
    word_lower = word.lower()
    for normalized, variations in processed_word_bank.items():
        if word_lower in variations:
            return normalized
    return word

# Vectorized normalization function
def normalize_categories(categories, albums_in_index):
    if pd.isna(categories):
        return categories

    # Remove numbers and clean album names
    for album in albums_in_index:
        if album.lower() in categories.lower():
            categories = re.sub(r'№\d+| - \d+|-\d+|\(\d+\)', '', categories)

    # Replace dash with comma
    categories = categories.replace(' - ', ',')

    # Normalize words
    categories = ','.join([normalize_word(word.strip()) for word in categories.split(',')])
    return categories

# Load album names
index_file_path = 'index.xlsx'
albums_in_index = pd.read_excel(index_file_path)['Album'][1:].dropna().str.lower().tolist()

# Load data
file_path = 'songs_data.xlsx'
df = pd.read_excel(file_path)

# Normalize categories column
df['Categories'] = df['Categories'].apply(lambda x: normalize_categories(x, albums_in_index))

# Save back
df.to_excel(file_path, index=False)

print(f"Normalization complete. Updated file saved as {file_path}.")
