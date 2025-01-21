import sqlite3
import pandas as pd

# Load the songs data Excel file
songs_data_df = pd.read_excel('songs_data.xlsx')

# Connect to the SQLite database
conn = sqlite3.connect('database')
cursor = conn.cursor()

# Insert a placeholder for the first song manually before processing
placeholder_song_name = 'Placeholder Song'
placeholder_link = 'http://example.com/placeholder'

cursor.execute("INSERT INTO songs (song_name, link) VALUES (?, ?)", (placeholder_song_name, placeholder_link))
placeholder_song_id = cursor.lastrowid  # Get the ID of the placeholder song

# Commit the placeholder song
conn.commit()

# Process each row in the first 100 rows
for index, row in songs_data_df.iterrows():
    song_name = row['Title']
    link = row['Download Links']
    
    # Ensure 'Categories' is a string and handle empty or invalid categories
    categories = str(row['Categories']) if pd.notna(row['Categories']) else ""
    
    # Insert the song into the 'songs' table
    cursor.execute("INSERT INTO songs (song_name, link) VALUES (?, ?)", (song_name, link))
    song_id = cursor.lastrowid  # Get the last inserted song ID

    # Check if there are categories to process
    if categories:
        # Proceed only if categories are not empty
        category_list = categories.split(', ')  # Split categories by comma

        # Now, handle the categories (w, i, v, c, etc.) and link them to the song
        for category in category_list:
            category = category.strip()  # Clean any extra spaces
            
            # Split the category string if it contains multiple values (e.g., w639,c15,v11)
            sub_categories = category.split(',')
            
            for sub_category in sub_categories:
                # Check the category type and process it accordingly
                if sub_category.startswith('w'):  # Vocal category
                    try:
                        vocal_id = int(sub_category[1:])
                        cursor.execute("INSERT INTO composers_songs (song_id, composer_id) VALUES (?, ?)", (song_id, vocal_id))
                    except ValueError:
                        print(f"Skipping invalid vocal category: {sub_category}")
                elif sub_category.startswith('i'):  # Instrument category
                    try:
                        instrument_id = int(sub_category[1:])
                        cursor.execute("INSERT INTO songs_instruments (song_id, instrument_id) VALUES (?, ?)", (song_id, instrument_id))
                    except ValueError:
                        print(f"Skipping invalid instrument category: {sub_category}")
                elif sub_category.startswith('c'):  # Genre category
                    try:
                        genre_id = int(sub_category[1:])
                        cursor.execute("INSERT INTO songs_genre (song_id, genre_id) VALUES (?, ?)", (song_id, genre_id))
                    except ValueError:
                        print(f"Skipping invalid genre category: {sub_category}")
                elif sub_category.startswith('v'):  # Another vocals category
                    try:
                        vocals_id = int(sub_category[1:])
                        cursor.execute("INSERT INTO songs_vocals (song_id, vocals_id) VALUES (?, ?)", (song_id, vocals_id))
                    except ValueError:
                        print(f"Skipping invalid vocals category: {sub_category}")

    # Commit after each song
    conn.commit()

# Close the connection
conn.close()
