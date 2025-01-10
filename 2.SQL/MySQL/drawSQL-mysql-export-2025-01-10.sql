CREATE TABLE `songs`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL,
    `album` VARCHAR(255) NOT NULL,
    `key` VARCHAR(255) NOT NULL,
    `quality` VARCHAR(255) NOT NULL,
    `meter` VARCHAR(255) NOT NULL,
    `language` CHAR(2) NOT NULL,
    `link` TEXT NOT NULL
);
CREATE TABLE `composers`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `date_of_birth` DATE NOT NULL,
    `biography` TEXT NOT NULL,
    `style` VARCHAR(255) NOT NULL
);
CREATE TABLE `genre`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `genre_name` VARCHAR(255) NOT NULL
);
CREATE TABLE `composers_songs`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `song_id` INT NOT NULL,
    `composer_id` INT NOT NULL
);
CREATE TABLE `songs_genre`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `song_id` INT NOT NULL,
    `genre_id` INT NOT NULL
);
CREATE TABLE `instruments`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `instruments_name` INT NOT NULL
);
CREATE TABLE `songs_instruments`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `song_id` INT NOT NULL,
    `instrument_id` INT NOT NULL
);
CREATE TABLE `songs_vocals`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `song_id` INT NOT NULL,
    `vocals_id` INT NOT NULL
);
CREATE TABLE `vocals`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `vocals_name` VARCHAR(255) NOT NULL
);
ALTER TABLE
    `songs_instruments` ADD CONSTRAINT `songs_instruments_instrument_id_foreign` FOREIGN KEY(`instrument_id`) REFERENCES `instruments`(`id`);
ALTER TABLE
    `composers_songs` ADD CONSTRAINT `composers_songs_song_id_foreign` FOREIGN KEY(`song_id`) REFERENCES `songs`(`id`);
ALTER TABLE
    `composers_songs` ADD CONSTRAINT `composers_songs_composer_id_foreign` FOREIGN KEY(`composer_id`) REFERENCES `composers`(`id`);
ALTER TABLE
    `songs_vocals` ADD CONSTRAINT `songs_vocals_vocals_id_foreign` FOREIGN KEY(`vocals_id`) REFERENCES `vocals`(`id`);
ALTER TABLE
    `songs_genre` ADD CONSTRAINT `songs_genre_genre_id_foreign` FOREIGN KEY(`genre_id`) REFERENCES `genre`(`id`);
ALTER TABLE
    `songs_instruments` ADD CONSTRAINT `songs_instruments_song_id_foreign` FOREIGN KEY(`song_id`) REFERENCES `songs`(`id`);
ALTER TABLE
    `songs_vocals` ADD CONSTRAINT `songs_vocals_song_id_foreign` FOREIGN KEY(`song_id`) REFERENCES `songs`(`id`);
ALTER TABLE
    `songs_genre` ADD CONSTRAINT `songs_genre_song_id_foreign` FOREIGN KEY(`song_id`) REFERENCES `songs`(`id`);