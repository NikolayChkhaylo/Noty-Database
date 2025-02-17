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

# 1.Sorting the data
![image](https://github.com/user-attachments/assets/763e9bca-97a3-410d-92b1-a4a78e8ec040)
The image above is a fragment of the data we are working with. On the top left is the list of titles of the songs along with the composers names and categories in the column right next to it. Below is how the data looks when we run our first script to convert applicable names and categories into code names like c23, g45, etc..

![image](https://github.com/user-attachments/assets/544dde50-5ab8-43d9-9458-3da8e5be1c84)
Next we run a script that will clean up words we have no use for, such as "Words and music by" as we only care about the name of the composer for our sake. Below is what we achieve:

![image](https://github.com/user-attachments/assets/2bdf3eae-8c8e-45eb-943c-63b3773f4e16)
Now what we have left are words and phrases that mean the same thing but are spelled different. To fix this we run a script that normalizes the words into the word that is located in the index which is used to convert the words to code names, just like in the beggining. 

![image](https://github.com/user-attachments/assets/084e132d-45bf-4674-baf9-21ce9e409b45)
We can procced and run the same script that we ran at the very beggining to convert the words to code names since they will now match our index:

![image](https://github.com/user-attachments/assets/97ae48e4-0760-4e3e-9c03-709be3285aa3)
Almost everything is sorted except for some unique cases left. Before we tackle those, we can safely run a script that gets rid of stray colons, semicolons, and dashes. The reason we are doing this step just now is because there are some dashes that are part of the words and phrases that the index uses. If we try removing the dashes at the beggning, we will end up with words that are not in our index.

![image](https://github.com/user-attachments/assets/c6a790b8-f3d4-40e0-9fff-6b92b9c50aff)
Here we have discovered one of the problems with this data and that is the various ways the composers name is spelled. We tackle this by matching their first or last name across all the composers we have logged and then, unfortunately, semi-manually decide if the last names are just a coincidence or are they actually the same person.  

![image](https://github.com/user-attachments/assets/48f25212-cf23-418c-a1b7-275f06a0452d)
Finally, the longest part of this project is complete and it is time to put the data into a database


# 2.The database at first glance
Our first rough sketch of the database
![image](https://github.com/user-attachments/assets/d23af0cc-e558-4753-b625-753dd58229ae)

Then based on the model above we followed up with another more detailed and correct ER diagram
![image](https://github.com/user-attachments/assets/4591ed7a-a960-4d01-8def-9466112ad04f)

Once I implmented the database I ran a couple of test to make sure the data lines up with what I have on my excel spreadsheet. After going back and forth and fixing some mistakes, I was able to get all the songs accounted for and procceded to visualize the data.

![image](https://github.com/user-attachments/assets/78727a2f-6560-4f2c-8e4d-c6d49391bfa4)

As we can see, we have all nine tables with the exact names as on the diagrams previously displayed.

Now here are the 15 songs from the songs tables
![image](https://github.com/user-attachments/assets/2185afd7-ff67-4a2a-bda5-52163507f6ff)

Notice how the first song is a placeholder. This is done for the purpose of helping with debugging and checking the database with the excel spread sheet to make sure the songs are being inserted in the right order.

Lets quickly look at the excel file with the songs below to double check:
![image](https://github.com/user-attachments/assets/330c1ecf-b5a9-489f-a754-6da65322cff1)

As we can see, the first song is located in the 2nd row, which is why we have a placeholder in our database.

# 3.Visualizing the data
After the database was made I procceded to make some reports. The first problem I encountered was that I couldn't export directly from sqlite3 so I loaded the database into DB Browser and exported it as a CSV file. With Power BI, I was able to setup the proper relationships:

![image](https://github.com/user-attachments/assets/2f6e7f40-25e7-4138-a3de-6474a5ab5de5)

The first report I decided to do is analyze what genre of songs popped up the most. 

![image](https://github.com/user-attachments/assets/f694364d-e0fc-4a47-9c78-5208d049d584)

My prediction was that holidays would definatly be in the top 5. The most open ended, and hence dominant, genre is named "Christan life"(Христианская жизнь). This genre exceeds the rest by a significant margin, contributing slightly more than 20% to the whole followed by Chrismas which contributes only 8.9%. Among the top 10, we have genres like Chrismas, Easter, and other holidays which was to be expected, with Chrismas taking the first place amongst those holidays.

![image](https://github.com/user-attachments/assets/e64f151d-3b26-41f9-80f9-19a7f7e097ed)

The barchart above ranks the authors based on the most contributions. The number each author holds doesn't nessarily mean that they composed many songs but rather how much their name popped up in the data for each particular song. So If a composer was mentioned for writing the words but not the melody, there would be no distinction in the data between the two. Everything counts as 1 contribution from writing the melody, arranging for instruments or voices, or even translating.


![image](https://github.com/user-attachments/assets/a4bcfe14-ed2e-488d-bb34-032576cf4450)

In the diagram above, I used some of the previously mentioned top composers and decided to analyze how much of their compositions contain the most dominat genre. As expected, the data made sense with the top contributors displaying the most contributions in the "Christan life" genre.

# Actual use disscussion and Advanced Problem:
Now that we have everything setup, we can start adding more information into the database. The majority of the information that is yet to be added is tedious and has to be done semi-manually, such as determining the key of the song (whether it is in major or minor). At best, AI has a 50% chance of determining the right key because of relative major and minor cases in music. Furthermore, what if the musical introduction is in one key, but when the singers comes in, the music changes to a different key? These cases are trival for a musican but I figured this was far from the case when it comes to AI. 

Fortunately, there is an AI that can determine what key a song is in with sufficient accuracy by audio to make me consider using it. Unfortunately, this means I have to provide a MIDI recording of some sorts or any audio recording. After I analyzed the database for MIDI recordings and formats like MusicXML(that can be easily converted to MIDI), I realized that they were scarce and the majority of songs only had notes without audio. This means that I will have to personally make piano recordings of the song, which is very time consuming, and feed them to the AI. Alternatively, I can convert the PDFs into a music format(MusicXML) that can automatically be used in music software to directly play it back or make a midi recording. ScanScore is an excellent software that scans PDFs of music and converts them to MusicXML formats. This software is basically a PDF converter but for music. Here's an example:
![image](https://github.com/user-attachments/assets/bf77c49b-2a8d-4275-bfef-f9768020952a)

![image](https://github.com/user-attachments/assets/ba68e311-4680-4699-b801-204ad3435ce1)

However, with each new solution comes another new problem. The accuracy of ScanScore depends on the clarity of the PDF of the sheet music. Sometimes the PDF can clearly distinguish an export coming from some music software(our best case scenario). Other times, the PDF can be clearly seen to have been taken from a book which introduces awkward orientation of the page, dark spots from shadows, uneven lighting, and in some rare cases we have notes being cut off.

The next problem I encountered upon creating the database is that I noticed there are cases where the file provided isn't a single song but rather a collection of songs(sometimes being 1000+ pages long). Therefore, if someone wants to look for a song in that collection, they would have to download the whole PDF and look through the file to find their song. A solution to this would be to split the PDF into smaller PDFs that each contain a single song and then rename each corresponding PDF to the name of the song that it contains, along with the name of author, key, etc., so that it can be properly integrated into the database. This problem is further explored in the "4.Advanced problem" folder(work in progress).

# How to actually run this program for yourself(work in progress):
First you'll need to install python

Then you will need to install all the dependencies:

pip install requests beautifulsoup4 langdetect pandas openpyxl

Finally, you can just run the build_db.py script.

