# Planning the database
After sorting the data I started mapping the relationships of the songs. I decided that a song can have multiple composers, writers, genres, instruments, and vocals. These would be the many to many relationships. We satisfy the first normal form because there is no information that is implied with the row order, we have a primary key, and we don't mix types such as int and strings together in one column. We also don't have any repeating groups for the songs because we store the genres, vocals, and other categories in a separate row within a join table.

For the second normal form, we are able to avoid update, delete, and insertion anomalies by giving each non-key attriubute their own table if it doesn't fit with the initial song table we already have. 

We don't have a dependency of a non-key attribute on another non-key attribute so we don't run into problem with satisfying third normal form.
