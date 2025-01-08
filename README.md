# Noty-Database
# Problem(s):
As a musican/choir conductor/singer, I want the capability to quickly and easily find sheet music for various songs with specific styles that fit the occasion at hand(i.e. Thanksgiving, Christmas, wedding, funeral, etc.). While many websites such as noty-bratstvo.org, slavoslovie.kz, and mscmusic.org have the option to search with filters by instruments and occasions, such as those mentioned prior, there are some filters that are not avaliable that would be nice to have. 
  
  For example, there is no filter for composers, language, and the key the music is written in. The capability to search by a specific composer is important because each composer has a certain style. By knowing which composer one prefers, it becomes easier to find songs that not only fit the occasion, but also fulfill the preference of the musican,choir conductor, or the singer(s). Searching by the proper langauge elimainates the time you have to look through the various search results that are mixed with various languages. The last one is more of a quality of life feature for the musicans, because typically you would want to pick a song in keys such as A,B,C,D,E,F,and G to avoid sharp or flat key signitures that may be troublesome for begginers, specifically muscians in this case, to play in(unless you have the luxury to personally rewrite the song and tranpose it to a favorable key). Aside from that, we can look to just specify if the key is in major or minor in order to narrow down the style and mood of a song that we are looking for. 

  While there is no filter for searching by a specific composer, this can still be "technically" accomplished by using the general search bar in noty-bratstvo.org. Moreover, we can use the "site:" operator that Google provides us with so we can look up a composer along with the category like so: "Composer name" "Occasion" site:noty-bratstvo.org. A real example looks like this "Бальжик Петр Жатвенные site:noty-bratstvo.org," which basically translates to looking for harvest songs written by Бальжик. Unfortunately, when I started this project and got myself familiarized with the data, I noticed a glaring inconsistency across the board. The names of the composers were not always in the same format. Here is an example of the various ways the same name of a composer was written: П. Б., Петр Бальжик, П. Бальжик, П Б, and some other variations. The point is that there is no consistency in how the name is written with regards to whether the initials are used, the full name, partial initials, initials with and without the periods, etc. Of course, you can still adjust to your search results to include these cases like so:
  
("П. Б." OR "Петр Бальжик" OR "П. Бальжик" OR "П Б") site:noty-bratstvo.org

However, this takes too much time, lacks simplicity, defeats our initial goal of being quick and efficient, and we won't even be sure if that covers the whole database unlness we go through the whole data ourselves. Therefore, the only option we have left is to make our own relational database and make sure it is normalized before we even consider adding our own filters and categories. 

# Goal(s): 
1.The first goal we aim to accomplish is to extract the data with a webscraper and normalize the data with the help of a script and excel. The data needs to be able to satisfy 5NF(5th normal form). Unfortunately there is one problem. There will be some rare cases where there are two composers with the same first and last initials but have different names.

2.The 2nd goal will be to put this data into a relational database.

3.In the last step we will be testing our database making sure that it was proplery implmeneted and use Tableau to visualize our data. This will allow us to get a bigger and better picture of the data that we are dealing with.

# Advanced Problem:
  Upon creating the database I noticed there are cases where the file provided isn't a single song but rather a collection of songs(sometimes beings 1000+ pages long). Therefore, if someone wants to look for a song in that collection, they would have to download the whole pdf and look though the file to find their song. A solution to this would be to split the pdf into smaller pdfs that each contain a single song and then rename each corresponding pdf to the name of the song that it contains, along with the name of author, key, etc., so that it can be properly integrated into the database. 

Unfortuantley, there is one more last tedious problem that we will encounter. Lets assume we are working with the collection of songs that is 1000 pages long. Assuming each song is 2 pages long, we would have 500 pdfs right? Turns out that about 80% of the cases, the songs overlap onto one another, meaning, that the pdfs are taken from a book and the way the book is written is to conserve as much space as possible which is why we end up with pdfs where we will have an ending of one song and the beggning of another all on the same page. Essentially all of this comes down to sorting and determining where each song starts and were each song ends, as well as figuring out who is the author by reading the pdf. While AI can help with recognizing the titles and names of authors, there still has to be someone who goes through all the data to make sure the AI properly wrote out the name and title. In the end, there will still be words on the pdf that are unrecognizable due to the poor quality of the pdf.

# The database at first glance
![image](https://github.com/user-attachments/assets/bc21a794-e58f-40ac-b9dd-68a80f0311a8)




