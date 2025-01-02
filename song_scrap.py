import requests
from bs4 import BeautifulSoup
import os
from langdetect import detect, DetectorFactory
import pandas as pd  # Import pandas for Excel functionality

# Set seed for consistency in language detection
DetectorFactory.seed = 0

# Function to scrape the title and categories from a node URL
def scrape_song_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Get the title from the second <div>
    divs = soup.find_all('div', class_='col-md-12')
    title = divs[1].find('h1').text.strip() if len(divs) > 1 else 'No Title Found'

    # Detect the language of the title
    if title and len(title) > 3 and title != 'No Title Found':
        try:
            language = detect(title)
        except Exception as e:
            print(f"Language detection error for title '{title}': {e}")
            language = 'Unknown'
    else:
        print(f"Title too short or not found for URL: {url}")
        language = 'Unknown'

    # Find all category tags
    category_tags = soup.find_all('div', class_='field-item even')
    categories = []
    for tag in category_tags:
        if not tag.find(['div', 'h2', 'a']):
            categories.append(tag.text.strip())

    return title, categories, language

# Function to find all node links from the main URL
def find_node_links(main_url):
    response = requests.get(main_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    node_links = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if '/node/' in href:
            full_url = f"https://noty-bratstvo.org/{href}"  # Replace with the actual domain
            node_links.append(full_url)
    return node_links

# Function to get the download link without downloading
def get_download_links(node_url, title):
    response = requests.get(node_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Normalize title for filenames
    valid_title = normalize_filename(title)

    # Check for "Скачать все файлы"
    download_all_link = soup.find('a', string='Скачать все файлы')
    if download_all_link:
        download_url = download_all_link['href']
        full_download_url = f"https://noty-bratstvo.org{download_url}"
        return [full_download_url]  # Return a list with a single download link

    # Check for zip files and pdf links
    zip_links = soup.find_all('a', href=True, string=lambda s: s and 'zip' in s)
    pdf_links = soup.find_all('a', href=True, string=lambda s: s and 'pdf' in s)

    download_urls = []

    for zip_link in zip_links:
        zip_name = zip_link.text.strip()
        if zip_name == f"{valid_title}.zip":
            full_zip_url = zip_link['href']
            download_urls.append(full_zip_url)

    for pdf_link in pdf_links:
        full_pdf_url = pdf_link['href']
        download_urls.append(full_pdf_url)

    return download_urls

def normalize_filename(title):
    # Replace illegal characters with underscores
    return ''.join(c if c.isalnum() or c in (' ', '_') else '_' for c in title)

# Main function to scrape titles, categories, and store data in Excel
def main():
    main_urls = [
        'https://noty-bratstvo.org/glossary/1',
        
        # Add more URLs as needed
    ]

    songs_data = []  # List to store song data for Excel

    for main_url in main_urls:
        print(f"Accessing: {main_url}")
        node_links = find_node_links(main_url)

        for node_url in node_links:
            print(f"Accessing node link: {node_url}")
            title, categories, language = scrape_song_page(node_url)
            print(f"Title: {title}")
            print(f"Categories: {categories}")
            print(f"Detected Language: {language}")

            # Get download links based on the specified conditions
            download_links = get_download_links(node_url, title)
            download_links_str = ', '.join(download_links)  # Join links into a single string
            
            # Store the data
            songs_data.append({
                'Title': title,
                'Categories': ', '.join(categories),
                'Language': language,
                'Download Links': download_links_str,
            })
            print("-" * 40)

    # Create a DataFrame and save to Excel
    df = pd.DataFrame(songs_data)
    df.to_excel('songs_data.xlsx', index=False)
    print("Data saved to songs_data.xlsx")

if __name__ == "__main__":
    main()
