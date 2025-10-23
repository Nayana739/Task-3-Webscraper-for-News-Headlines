# Import required libraries
import requests
from bs4 import BeautifulSoup

# Choosing a news website 
URL = 'https://www.bbc.com/news'

# Fetch the HTML content
response = requests.get(URL)
html_content = response.text

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract headlines 
headlines = []
for tag in soup.find_all(['h1', 'h2', 'h3']):
    text = tag.get_text(strip=True)
    if text and len(text) > 10:  # Filter out short or empty headlines
        headlines.append(text)

# Save headlines to a .txt file
with open('top_headlines.txt', 'w', encoding='utf-8') as f:
    for i, headline in enumerate(headlines, 1):
        f.write(f"{i}. {headline}\n")

print(f"{len(headlines)} headlines saved to 'top_headlines.txt'")