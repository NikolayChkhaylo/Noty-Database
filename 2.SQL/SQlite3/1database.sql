PRAGMA foreign_keys = ON; 

CREATE TABLE songs(
    id INTEGER PRIMARY KEY,
    song_name TEXT NOT NULL,
    album TEXT,
    song_key TEXT,
    quality TEXT,
    meter TEXT,
    lang TEXT,
    link TEXT NOT NULL
);
CREATE TABLE composers(
    id INTEGER PRIMARY KEY,
    composers_name TEXT,
    date_of_birth DATE,
    biography TEXT,
    style VARCHAR(255)
);
CREATE TABLE genre(
    id INTEGER PRIMARY KEY,
    genre_name VARCHAR(255) NOT NULL
);
CREATE TABLE vocals(
    id INTEGER PRIMARY KEY,
    vocals_name TEXT NOT NULL
);
CREATE TABLE instruments(
    id INTEGER PRIMARY KEY,
    instruments_name TEXT NOT NULL
);
CREATE TABLE composers_songs(
    id INTEGER NOT NULL PRIMARY KEY,
    song_id INTEGER NOT NULL,
    composer_id INTEGER NOT NULL,
    FOREIGN KEY(song_id) REFERENCES songs(id),
    FOREIGN KEY(composer_id) REFERENCES composers(id)
);
CREATE TABLE songs_genre(
    id INTEGER NOT NULL PRIMARY KEY,
    song_id INTEGER NOT NULL,
    genre_id INTEGER NOT NULL,
    FOREIGN KEY(song_id) REFERENCES songs(id),
    FOREIGN KEY(genre_id) REFERENCES genre(id)
);
CREATE TABLE songs_instruments(
    id INTEGER NOT NULL PRIMARY KEY,
    song_id INTEGER NOT NULL,
    instrument_id INTEGER NOT NULL,
    FOREIGN KEY(song_id) REFERENCES songs(id),
    FOREIGN KEY(instrument_id) REFERENCES instruments(id)
);
CREATE TABLE songs_vocals(
    id INTEGER NOT NULL PRIMARY KEY,
    song_id INTEGER NOT NULL,
    vocals_id INTEGER NOT NULL,
    FOREIGN KEY(song_id) REFERENCES songs(id),
    FOREIGN KEY(vocals_id) REFERENCES vocals(id)
);

