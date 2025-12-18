# Get request module from url library.
# pip install urllib3 (doesn't come out of the box)
from urllib import request
# This one has handy tools for scraping a web page.
# pip install beautifulsoup4 (doesn't come out of the box)
from bs4 import BeautifulSoup

# Sample page for practice.
page_url = 'https://www.bbc.co.uk/news/my'

# Open that page
raw_page = request.urlopen(page_url)

# Make a BeautifulSoup object from the html page.
soup = BeautifulSoup(raw_page, 'html5lib')

# Isolate the main content block
content = soup.main

# Create an empty list to hold a dictionary for each item.
links_list = []

# Loop through all the links in the article.
for link in content.find_all('a'):
    # Try to get the href, image url, and text.
    try:
        url = link.get('href')
        img = link.img.get('src')
        text = link.span.text
        links_list.append({'url' : url, 'img': img, 'text': text})
    # If the row is missing anything…
    except AttributeError:
        #… skip it, don't blow up.
        pass