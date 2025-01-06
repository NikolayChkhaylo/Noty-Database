# Web scraper approach:
The first issue I came across when writing the script is finding out a consistent way to tell apart the title, category, and the composer(s) of the song. The title was relatively simple because it was always a larger font than the rest of the text and appeared first. I pulled that information from the HTML of the website. Unfortunately, the categories and composers were the same font, color, and would never have a consistent order in which they appear. Sometimes the author would be in the middle of the categories, other times there were a couple of authors on a single line, etc. I made the decision to just merge the categories and composers into one group of the Excel column opting to sort them out later. 

This script will take a while to run(about 20min), however I made sure to account for all the edge cases for this website once I ran through it once. I was able to pinpoint where the issues occur by looking at the Excel file and then only web scraping a single specific page until the issue was fixed for each letter of the alphabet category.

How the script formats the data:
In the first column the name of the title will be recorded. In the 2nd column, the categories,composers, and other info will be listed. In the 3rd column the language type will be listed. In the last column will be the link(s) to the file with the notes. 

# Fixing the data from Excel:
This process probably took the most out of all of the parts of this project and also required the utmost attention to details. I started by using the find and replace feature of Excel. I decided it would only be logical to start with sorting the categories as the webiste already has filters for them. I decided to make another Excel spreadsheet and list all name of the categories. But before we start sorting the categories, we can get rid of a couple of entries that were entered. The data you will receive from running the script will contain some parts where there is no categories or composers to be seen.  

There were times where I adjusted the data and accidentally included the nearby columns in the Excel file. I didn't notice that I applied changes to other column unintentionally until several days later when there was no way to revert the data. Furthermore, this accident occurred more then once which gave me the habit of making backups of data which I actually ended up using. I was able to save an enormous amount of time, even when I made a mistake, by having backups.  

# The 3 scripts
The first script named "1normalizer" makes sure all of the data follows a specific format and spelling of the index. I could have opted out of normalizing the data and instead go ahead to direclty labeling it. However, I suspected that it would be useful for debugging and making sure that the (actually I was able to replace certain phrases that way )
