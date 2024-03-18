import requests
from bs4 import BeautifulSoup
import re

# URL of the webpage to scrape
url = "https://www.scoopwhoop.com/design/quotes-from-fight-club-movie/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

#Find all figures 
all_figures = soup.find_all('figure')
# find image links within the figures

all_links = []
for figure in all_figures:
    img = figure.find('img')
    if img:
        src = img.get('src')
        all_links.append(src)
for link in all_links:
    print(link)
    
# Download the images
for i, link in enumerate(all_links):
    response = requests.get(link)
    with open(f'img_{i}.jpg', 'wb') as file:
        file.write(response.content)
