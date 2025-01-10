import requests
from bs4 import BeautifulSoup
import os
from langdetect import detect, DetectorFactory
import pandas as pd  # Import pandas for Excel functionality
from concurrent.futures import ThreadPoolExecutor, as_completed  # For concurrent requests
import requests_cache  # For caching requests

# Set seed for consistency in language detection
DetectorFactory.seed = 0

# Set up requests cache
requests_cache.install_cache('scraping_cache', expire_after=3600)  # Cache expires after 1 hour

# Function to scrape the title and categories from a node URL
def scrape_song_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')  # Use lxml for faster parsing

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
        if not tag.find(['div', 'h2', 'a']):  # Check for valid category tags
            categories_text = tag.text.strip()
            categories.extend([line.strip() for line in categories_text.splitlines() if line.strip()])

    return title, categories, language

# Function to find all node links from the main URL
def find_node_links(main_url):
    response = requests.get(main_url)
    soup = BeautifulSoup(response.content, 'lxml')  # Use lxml for faster parsing
    node_links = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if '/node/' in href:
            full_url = f"https://noty-bratstvo.org/{href}"  # Replace with the actual domain
            node_links.append(full_url)
    return node_links

# Function to get the download link (now just the node URL) without downloading
def get_download_links(node_url):
    return [node_url]  # Return the node URL in a list

# Function to normalize filenames (unchanged)
def normalize_filename(title):
    return ''.join(c if c.isalnum() or c in (' ', '_') else '_' for c in title)

# Main function to scrape titles, categories, and store data in Excel
def main():
    main_urls = [
        'https://noty-bratstvo.org/glossary/1',
        'https://noty-bratstvo.org/glossary/2',
        'https://noty-bratstvo.org/glossary/3',
        'https://noty-bratstvo.org/glossary/4',
        'https://noty-bratstvo.org/glossary/5',
        'https://noty-bratstvo.org/glossary/6',
        'https://noty-bratstvo.org/glossary/7',
        'https://noty-bratstvo.org/glossary/9',            
        'https://noty-bratstvo.org/glossary/a',
        'https://noty-bratstvo.org/glossary/b',
        'https://noty-bratstvo.org/glossary/e',
        'https://noty-bratstvo.org/glossary/f',
        'https://noty-bratstvo.org/glossary/g',
        'https://noty-bratstvo.org/glossary/h',
        'https://noty-bratstvo.org/glossary/i',
        'https://noty-bratstvo.org/glossary/j',
        'https://noty-bratstvo.org/glossary/k',
        'https://noty-bratstvo.org/glossary/l',
        'https://noty-bratstvo.org/glossary/m',
        'https://noty-bratstvo.org/glossary/n',
        'https://noty-bratstvo.org/glossary/o',
        'https://noty-bratstvo.org/glossary/p',
        'https://noty-bratstvo.org/glossary/q',
        'https://noty-bratstvo.org/glossary/r',
        'https://noty-bratstvo.org/glossary/s',
        'https://noty-bratstvo.org/glossary/t',
        'https://noty-bratstvo.org/glossary/u',
        'https://noty-bratstvo.org/glossary/v',
        'https://noty-bratstvo.org/glossary/w',
        'https://noty-bratstvo.org/glossary/x',
        'https://noty-bratstvo.org/glossary/y',
        'https://noty-bratstvo.org/glossary/z',
        'https://noty-bratstvo.org/glossary/Є',
        'https://noty-bratstvo.org/glossary/%D1%94',
        'https://noty-bratstvo.org/glossary/%D1%96',
        'https://noty-bratstvo.org/glossary/%D0%B0',
        'https://noty-bratstvo.org/glossary/%D0%B1',
        'https://noty-bratstvo.org/glossary/%D0%B2',
        'https://noty-bratstvo.org/glossary/%D0%B3',
        'https://noty-bratstvo.org/glossary/%D0%B4',
        'https://noty-bratstvo.org/glossary/%D0%B5',
        'https://noty-bratstvo.org/glossary/%D0%B6',
        'https://noty-bratstvo.org/glossary/%D0%B7',
        'https://noty-bratstvo.org/glossary/%D0%B8',
        'https://noty-bratstvo.org/glossary/%D0%B9',
        'https://noty-bratstvo.org/glossary/%D0%BA',
        'https://noty-bratstvo.org/glossary/%D0%BB',
        'https://noty-bratstvo.org/glossary/%D0%BC',
        'https://noty-bratstvo.org/glossary/%D0%BD',
        'https://noty-bratstvo.org/glossary/%D0%BE',
        'https://noty-bratstvo.org/glossary/%D0%BF',
        'https://noty-bratstvo.org/glossary/%D1%80',
        'https://noty-bratstvo.org/glossary/%D1%81',
        'https://noty-bratstvo.org/glossary/%D1%82',
        'https://noty-bratstvo.org/glossary/%D1%83',
        'https://noty-bratstvo.org/glossary/%D1%84',
        'https://noty-bratstvo.org/glossary/%D1%85',
        'https://noty-bratstvo.org/glossary/%D1%86',
        'https://noty-bratstvo.org/glossary/%D1%87',
        'https://noty-bratstvo.org/glossary/%D1%88',
        'https://noty-bratstvo.org/glossary/%D1%89',
        'https://noty-bratstvo.org/glossary/%D1%8D',
        'https://noty-bratstvo.org/glossary/%D1%8E',
        'https://noty-bratstvo.org/glossary/%D1%8F',
    ]

    songs_data = []  # List to store song data for Excel

    # Using ThreadPoolExecutor for concurrent requests
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = {}

        # Iterate over main URLs and find node links
        for main_url in main_urls:
            print(f"Accessing: {main_url}")
            node_links = find_node_links(main_url)
            for node_url in node_links:
                future = executor.submit(scrape_and_store_data, node_url)
                future_to_url[future] = node_url

        # Collect results as they complete
        for future in as_completed(future_to_url):
            node_url = future_to_url[future]
            try:
                title, categories, language = future.result()
                download_links = get_download_links(node_url)
                download_links_str = ', '.join(download_links)

                # Store the data
                songs_data.append({
                    'Title': title,
                    'Categories': ', '.join(categories),
                    'Language': language,
                    'Links': download_links_str,  # Store node link
                })
                print("-" * 40)
            except Exception as e:
                print(f"Error processing {node_url}: {e}")

    # Create a DataFrame and save to Excel
    df = pd.DataFrame(songs_data)
    df.to_excel('songs_data.xlsx', index=False)
    print("Data saved to songs_data.xlsx")

# Helper function to scrape and store data
def scrape_and_store_data(node_url):
    title, categories, language = scrape_song_page(node_url)
    return title, categories, language

if __name__ == "__main__":
    main()
