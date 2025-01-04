import pandas as pd

# Word bank with replacements (you can expand this list as needed)
word_bank = {
    'choir': {'chor', 'Chor (de.)', 'Chor'},
    'Соло': {'Соло (1 голос)'},
}

def normalize_word(word):
    # Check each entry in the word bank
    for normalized, variations in word_bank.items():
        if word in variations:
            return normalized  # Return the normalized word
    return word  # Return the word unchanged if no match is found

def normalize_categories(categories):
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
