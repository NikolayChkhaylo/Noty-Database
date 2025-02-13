# Web scraper approach:
The first issue I came across when writing the script is finding out a consistent way to tell apart the title, category, and the composer(s) of the song. The title was relatively simple because it was always a larger font than the rest of the text and appeared first. I pulled that information from the HTML of the website. Unfortunately, the categories and composers were the same font, color, and would never have a consistent order in which they appear. Sometimes the author would be in the middle of the categories, other times there were a couple of authors on a single line, etc. I made the decision to just merge the categories and composers into one group of the Excel column opting to sort them out later. 

The song_scrape script will take a while to run(about 20min), however I made sure to account for all the edge cases for this website once I ran through it once. I was able to pinpoint where the issues occur by looking at the Excel file and then web scraped that single page until the issue was fixed for each letter title pages.

How the script formats the data:
In the first column of the excel sheet the name of the title will be recorded. In the 2nd column, the categories,composers, and other info will be listed. In the 3rd column the language type will be listed. In the last column will be the link(s) to the file with the notes. 

# Fixing the data from Excel:
This process took the most out of all of the parts of this project and also required the utmost attention to details. I started by using the find and replace feature of Excel. I decided it would only be logical to start with sorting the categories as the webiste already has filters for them. I made another Excel spreadsheet and listed all the names of the categories. 

I encountered a challenge when I adjusted the data and accidentally included the nearby columns in the Excel file without knowing. I didn't notice that I applied changes to other columns unintentionally until several days later when there was no way to revert the data. Furthermore, this accident occurred more than once which gave me the habit of making backups of data that I eventually ended up using. I was able to save an enormous amount of time, even when I made a mistake, by having backups.  

# The 3 scripts
The first script is named "1normalizer" makes sure all of the data follows a specific format and spelling of the index. I could have opted out of normalizing the data and instead go ahead to direclty labeling it. However, there are plenty of cases which prevented me from normalizing everything from start to fininsh. Here is an example translated to english:

violin - composers name

This is a case where the composer is acknowledged by mentioning which instrument they wrote for. The problem is the dash. What we want to do is seperate these two words with a comma, just how we decided to sperate every other catergory. However, we can't do that as some categories have dashes in them like "Вокал - 2-т." This simply translates to "Vocal - 2 - uet." This calls for multiple normalizations. Therefore, the first time we run the normalizer script, it will sort everything it was told. Then the next script will replace all dashes ONLY after we have normalized the categories where the dashes are part of the catergorys name. After that, the 2nd time we normalize, we go for the rest of the new catergories that were created from the normalization of the dash.

There are also cases such as:
"Album name" - 574
where some album names or names of a collection of music were followed by a number. Most people associate the songs with their name and not their number in the collection. Furthermore, there are some inconsistencies between these albums as to what song is attached to what number. Therefore, the normalizer sciript gets rid of the number and only keeps the album/collection name. 

The 3nd script is named the deleter. This was used to delete unnessesary words such as "Music and words by." etc.. This was redundant information as people would be able to find who did what based on the music pdf itself. Furthermore, when the script cleaned the data, it would completely isolate the composers and writers names allowing for smoother normalization.

The 1st script is the sorter. It names each catergory and composer based on the index, so when it starts sorting songs_data excel file, it will, for example, replace the name of a composer with c2 for example. C stands for "composer," and 2 tells us which row to look at it in the index to find out the full name of composer we are referencing. Labeling everything in this format allowed me to easily check my work and find out if my scripts were actually doing what they are suppose to be doing.

The 4th script removes stray slashes(/), colons(:), semicolons(;), and other symbols that we have no use from. This allows us to further split up names and catgories that occasionally have awkward formats.

Finally, this is the order of the scripts we end up running
1.sorter: converts what it can that shows up in the index
2.deleter:
deleter, sorter

