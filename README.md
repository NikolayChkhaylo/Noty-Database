# Problem(s):
As a musican/choir conductor/singer, I want the capability to quickly and easily find sheet music for various songs with specific styles that fit the occasion at hand(i.e. Thanksgiving, Christmas, wedding, funeral, etc.). While many websites such as noty-bratstvo.org have the option to search with filters like so:
![image](https://github.com/user-attachments/assets/8edca3c8-4613-4576-93a6-63ed27e68eca)

there are still some filters that are not avaliable that would be nice to have. 
  
  For example, there is no filter for composers, language, and the key the music is written in. The capability to search by a specific composer is important because each composer has a certain style. By knowing which composer you prefer, it becomes easier to find songs that not only fit the occasion, but also fulfill the preference of the musican, choir conductor, or the singer(s). Searching by the proper langauge eliminates the time you have to look through the various search results that are mixed with various languages. Searching by key is more of a quality of life feature for the musicans, because typically you would want to pick a song in keys such as A,B,C,D,E,F,and G to avoid sharp or flat key signitures that may be troublesome for beginners, specifically muscians in this case, to play in (unless you have the luxury to personally rewrite the song and tranpose it to a favorable key). Aside from that, we can look to just specify if the key is in major or minor in order to narrow down the style and mood of a song that we are looking for. 

  While there is no filter for searching by a specific composer, this can still be "technically" accomplished by using the general search bar in noty-bratstvo.org. 
![image](https://github.com/user-attachments/assets/e3760ce7-003a-476f-9814-379ba6a00c93)
Moreover, we can use the "site:" operator that Google provides us with so we can look up a composer along with the category like so: "Composer name" "Occasion" site:noty-bratstvo.org. A real example looks like this "Бальжик Петр Жатвенные site:noty-bratstvo.org," which basically translates to looking for harvest songs written by Бальжик. Unfortunately, when I started this project and got myself familiarized with the data, I noticed a glaring inconsistency across the board. The names of the composers were not always in the same format. Here is an example of the various ways the same name of a composer was written: П. Б., Петр Бальжик, П. Бальжик, П Б, and some other variations. There is no consistency in how the name is written with regards to whether the initials are used, full name, partial initials, initials with and without the periods, etc.. Of course, you can still adjust your search results to include these cases like so:
  
("П. Б." OR "Петр Бальжик" OR "П. Бальжик" OR "П Б") site:noty-bratstvo.org

However, this takes too much time, lacks simplicity, and we can't be sure that covers the whole database unnless we go through the whole data ourselves and account for all the cases. Therefore, the only option we have left is to make our own relational database and make sure it is normalized before we even consider adding our own filters and categories. 

# Goal(s): 
1.The first goal I aimed to accomplish is to extract the data with a webscraper and normalize the data with the help of a python script and excel. The data needs to be able to satisfy 5NF(5th normal form). To my dismay, I've encountered some cases where there are two composers with the same first and last initials but have different names and there is no way to tell apart which one is which when we receieve only the initals. These cases will require even more effort by forcing us to look into the file to find the composers full name (which isn't always there).

2.The 2nd goal will be to put this data into a relational database(SQlite3 or MySQL).

3.In the last step we will be testing our database making sure that it was proplery implmeneted and use Tableau along or powerBI to visualize our data. 

# The database at first glance
After I sorted the data I began working on the database
![image](https://github.com/user-attachments/assets/d23af0cc-e558-4753-b625-753dd58229ae)

Then based on the model above we followed up with another more detailed and correct ER diagram
![image](https://github.com/user-attachments/assets/4591ed7a-a960-4d01-8def-9466112ad04f)

Once I implmented the database I ran a couple of test to make sure the data lines up with what I have on my excel spreadsheet. After going back and forth and fixing some mistakes, I was able to get all the songs accounted for and procceded to visualize the data.

# Visualizing the data
After the database was made I procceded to make some reports to analyze composers that composed the most songs to see what type of songs genre they stuck to composing in and this is what I found out: 

# Advanced Problem:
  Upon creating the database I noticed there are cases where the file provided isn't a single song but rather a collection of songs(sometimes beings 1000+ pages long). Therefore, if someone wants to look for a song in that collection, they would have to download the whole pdf and look though the file to find their song. A solution to this would be to split the pdf into smaller pdfs that each contain a single song and then rename each corresponding pdf to the name of the song that it contains, along with the name of author, key, etc., so that it can be properly integrated into the database. 


# How to actually run this program for yourself:
First you'll need to install python

Then you will need to install all the dependencies:

pip install requests beautifulsoup4 langdetect pandas openpyxl

Finally, you can just run the build_db.py script.

